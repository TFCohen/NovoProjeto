from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('outro', views.outro, name='outro'),


    #Alunos
    path('listar_alunos', views.listarAlunos, name='listar_alunos'),
    path('incluir_alunos', views.incluirAlunos, name='incluir_alunos'),
    path ('editar_aluno/<int:id>', views.editarAluno, name='editar_aluno'),

    path ('excluir_aluno/<int:id>', views.excluirAluno, name='excluir_aluno'),

    #Cursos
    path('listar_cursos', views.listarCursos, name='listar_cursos'),
    path('incluir_curso', views.incluirCursos, name='incluir_cursos'),
    path ('editar_curso/<int:id>', views.editarCurso, name='editar_curso'),#o name que aparece no url dentro do HTML

    path ('excluir_curso/<int:id>', views.excluirCurso, name='excluir_curso'),
]