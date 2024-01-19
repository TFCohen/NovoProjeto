from django.contrib import admin
from .models import Aluno, Curso

# Register your models here.


admin.site.register(Aluno)
admin.site.register(Curso)

#Inicializando o repositório
#git init

#Adicionando arquivos
#git add .

#Criando o commit 
#git commit -m "Mensagem"

#Configurações adicionais (apenas no primeiro commit após a instalação)
#git config --global user.email "O email do github"
#git config --global user.name "O usuário do github"

#Configurando o repositório remoto (Uma vez por projeto)
#git remote add origin "Endereço do repositório"

#Subindo para o github
#git push -u origin master (ou o branch em uso, ou seja, a palavra que estiver entre parênteses)

#atualizar arquivo no git hub
#git init
#git add .
#git commit -m " xxxx "
#git push -u origin

#para trocar o repositorio no git hub
#
#git remote -v
#git push -u origin main (pode ser main ou master ou...)
#
#git remote remove origin
#git remote add origin NOVO_ENDERECO

#rodar o servidor
#python manage.py runserver