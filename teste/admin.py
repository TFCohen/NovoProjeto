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
#git push -u origin master (ou o branch em uso, ou seja, a palavra que estiver entre parênteses)###