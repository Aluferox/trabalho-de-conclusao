from django import forms
from validators import validate


class HomeForm(forms.Form):
    manual_text = forms.CharField(required=False, label='', widget=forms.Textarea)

    file_data = forms.FileField(required=False,
                                label='',
                                allow_empty_file=False,
                                help_text='Enviar arquivo .txt',
                                widget=forms.FileInput(),
                                )

    def clean(self):
        cleaned_data = super().clean()
        # Campo vazio retorna um valor de None, arquivo vem com \n
        file_data = cleaned_data['file_data']

        # texto digitado no text-area vem com o padrão de quebra de linha do windows \r\n
        manual_text = cleaned_data['manual_text']

        # validar os campos de formulário
        validate(file_data, manual_text)
