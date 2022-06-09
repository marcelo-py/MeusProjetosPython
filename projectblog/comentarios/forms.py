from dataclasses import fields
from django.forms import ModelForm
from .models import Comentario


class FormComentario(ModelForm):
    def clean(self):
        data = self.cleaned_data
        nome = data.get('nome_comentario')
        email = data.get('email_comentario')
        comentario = data.get('comentario')

        if len(nome) < 3:
            self.add_error('nome_comentario', 'O nome precisa ter mais que 3 caractere')

        if not comentario:
            self.add_error(
                'comentario', 'O comentario não pode ficar vazio ao enviar'
            )


    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario')

