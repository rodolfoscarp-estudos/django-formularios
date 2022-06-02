from django.http import HttpRequest
from django.shortcuts import render
from passagens.forms import PassagemForm, PessoaForm


def index(request: HttpRequest):
    form = PassagemForm()
    pessoa_form = PessoaForm()

    contexto = {
        'form': form,
        'pessoa_form': pessoa_form
    }

    return render(request, "index.html", contexto)


def revisao_consulta(request: HttpRequest):
    if request.method == "POST":
        form = PassagemForm(request.POST)
        pessoa_form = PessoaForm(request.POST)

        if form.is_valid():

            contexto = {
                'form': form,
                'pessoa_form': pessoa_form
            }

            return render(request, "minha_consulta.html", contexto)

        else:

            contexto = {
                'form': form,
                'pessoa_form': pessoa_form
            }

            return render(request, "index.html", contexto)
