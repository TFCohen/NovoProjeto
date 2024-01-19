
from django.shortcuts import render, redirect
from django.http import HttpResponse

from teste.forms import AlunoForm, CursoForm
from teste.models import Aluno, Curso
# Create your views here.
# Create your views Aluno
def index(request):
    return HttpResponse ("Olá, Mundo! Agora é na Web!")

def outro(request):
    return HttpResponse ("Isso é uma requisição!")

def listarAlunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'listar_aluno.html', 
       {'alunos': alunos})

def incluirAlunos(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')

    else:
        form = AlunoForm()
    return render(request, 'incluir_aluno.html', {'form' : form})

def editarAluno (request, id):
    aluno = Aluno.objects.get(id=id)
    form = AlunoForm(instance=aluno)
    
    if request.method =='POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')

    return render(request,'incluir_aluno.html', {'form' : form})

def excluirAluno (request, id):
    aluno = Aluno.objects.get(id=id)
    aluno.delete()
    return redirect('listar_alunos')

# Create your views Curso
def listarCursos(request):
    Cursos = Curso.objects.all() #modelo
    return render(request, 'listar_curso.html', 
       {'cursos': Cursos}) 

#primeiro cursos (laranja) associar ao for do HTML {% for a in cursos %} linha 15
#segundo Cursos (azul) associar o cursos da linha 45 ao 47 


def incluirCursos(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')

    else:
        form = CursoForm()
    return render(request, 'incluir_curso.html', {'form' : form})# o nome tem que bater com o do template

def editarCurso (request, id):
    curso = Curso.objects.get(id=id)
    form = CursoForm(instance=curso)
    
    if request.method =='POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')

    return render(request,'incluir_curso.html', {'form' : form})

def excluirCurso (request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect('listar_cursos')

