from email.policy import default
from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    titulo_post = models.CharField(max_length=255, verbose_name='Titulo')
    autor_post = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Autor do Post')
    data_post = models.DateTimeField(default=timezone.now, verbose_name='Data do post')
    conteudo_post = models.TextField()
    excerto_post = models.TextField()
    categoria_post = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True)
    imagem_post = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True)
    publicado_post = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.titulo_post
