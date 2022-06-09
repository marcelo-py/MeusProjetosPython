import json
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .models import Post
from django.db.models import Q, Count, Case, When
from comentarios.forms import FormComentario
from comentarios.models import Comentario
from django.contrib import messages
import requests
from json import loads


class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 6
    context_object_name = 'posts'

    def get_queryset(self):
        qs =  super().get_queryset()
        qs = qs.order_by('-id').filter(publicado_post=True)
        qs = qs.annotate(
            numero_comentarios=Count(
                Case(
                    When(comentario__publicado_comentario=True, then=1)
                )
            )
        )
        return qs


class PostBusca(PostIndex):
    template_name = 'posts/post_busca.html'
    def get_queryset(self):
        qs = super().get_queryset()

        termo = self.request.GET.get('termo')
        if not termo:
            return qs

        #autor é uma foreignKey entãoprecisa ser usado __iexact
        qs = qs.filter(
            Q(titulo_post__icontains=termo) | 
            Q(autor_post__first_name__iexact=termo) | 
            Q(conteudo_post__icontains=termo) | 
            Q(excerto_post__icontains=termo) | 
            Q(categoria_post__nome_da_categoria__iexact=termo)
        )
        
        return qs


class PostCategoria(PostIndex):
    template_name = 'posts/post_categoria.html'

    def get_queryset(self):
        qs = super().get_queryset()

        categoria = self.kwargs.get('categoria', None)
        if not categoria:
            return qs
        
        qs = qs.filter(categoria_post__nome_da_categoria__iexact=categoria)

        return qs

class PostDetalhes(UpdateView):
    template_name = 'posts/post_detalhes.html'
    model = Post
    form_class = FormComentario
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        post = self.get_object()
        comentarios = Comentario.objects.filter(publicado_comentario=True, post_comentario=post.id)

        contexto['comentarios'] = comentarios #aqui adcionamos o post e os comentarios, tudo pelo context

        return contexto

    def form_valid(self, form):
        post = self.get_object()
        comentario = Comentario(**form.cleaned_data)
        comentario.post_comentario = post


        captcha_token = self.request.POST.get('g-recaptcha-response')
        cap_url ='https://www.google.com/recaptcha/api/siteverify'
        cap_secret = '6LesJW0fAAAAALbPLaFk-Y83CcKzQRU_8RZPAq-S'
        cap_data = {'secret': cap_secret, 'response': captcha_token}
        cap_server_response = requests.post(url=cap_url, data=cap_data)
        cap_json = loads(cap_server_response.text)
        if not cap_json['success']:
            messages.error(self.request, 'Erro no Captcha')
            return redirect('post_detalhes', pk=post.id)

        if self.request.user.is_authenticated:
            comentario.usuario_comentario = self.request.user
        
        comentario.save()
        messages.success(self.request, 'Comentario enviado!')
        return redirect('post_detalhes', pk=post.id)

