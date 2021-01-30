import magic
from django.core.exceptions import ValidationError


def validate(file_data, manual_text):

    try:
        # tenta abrir o cabeçalho do arquivo para verificar Seu MIME(extensão).
        mime = magic.from_buffer(file_data.read(1024), mime=True)

        # Verifica se o usuário enviou os dois campos.
        if file_data is not None and manual_text != '':
            raise ValidationError('Escolha Apenas um Campo Para Envio.')

        # Verifica se a extensão é a suportada no app.
        if 'text/plain' not in mime:
            raise ValidationError(f'{file_data}, Tipo de Arquivo Não Suportado.')

    except AttributeError:
        # Verifica se os dois campos estão vazios.
        if file_data is None and manual_text == '':
            raise ValidationError('Escolha Ao Menos Um Campo Para Enviar.')
