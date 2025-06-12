# # type: ignore
# # flake8: noqa

# # Comando:
# # python -c "import string as s;from secrets import SystemRandom as SR;print(''.join(SR().choices(s.ascii_letters + s.digits + s.punctuation, k=64)));"
# SECRET_KEY = 'HcGtB>DbLG`H!i/U-_^1v*fq8*fo["TK/F8,"`C6u{"8*U3fbaG7>m^T~^xr&v'

# # DEBUG DEVE SER False em produção
# DEBUG = False

# # Seu domínio ou IP devem vir aqui
# ALLOWED_HOSTS = [
#     'SEU_DOMINIO_OU_IP',
# ]  # Troque * para seu domínio ou IP

# # Config para postgresql
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'NOME_DA_BASE_DE_DADOS',
#         'USER': 'USUARIO_DA_BASE_DE_DADOS',
#         'PASSWORD': 'SENHA_DA_BASE_DE_DADOS',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }
