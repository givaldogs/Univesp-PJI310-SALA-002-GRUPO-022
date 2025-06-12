#!/bin/bash

# Sai se algum comando falhar
set -e

echo "Instalando dependências..."
pip install -r requirements.txt

echo "Executando migrações..."
python manage.py migrate --noinput

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "Criando superusuário (se não existir)..."
python manage.py shell << END
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.getenv("DJANGO_SU_NAME")
email = os.getenv("DJANGO_SU_EMAIL")
password = os.getenv("DJANGO_SU_PASSWORD")

if username and email and password:
    if not User.objects.filter(username=username).exists():
        print(f"Criando superusuário: {username}")
        User.objects.create_superuser(username=username, email=email, password=password)
    else:
        print(f"Superusuário '{username}' já existe. Pulando criação.")
else:
    print("Variáveis de superusuário ausentes. Nenhum usuário criado.")
END

echo "Build completo!"
