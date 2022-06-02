from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.validation import *
from passagens.models.passagem import Passagem
from passagens.models.pessoa import Pessoa


class PassagemForm(forms.ModelForm):
    data_pesquisa = forms.DateField(
        label="Data da Pesquisa", disabled=True, initial=datetime.today,
        widget=DatePicker())

    class Meta:
        model = Passagem
        fields = '__all__'
        labels = {
            'data_ida': 'Data de Ida',
            'data_volta': 'Data de Volta',
            'informacoes': 'Informações',
            'classe_viagem': 'Classe do Vôo'
        }
        widgets = {
            'data_ida': DatePicker(),
            'data_volta': DatePicker(),
        }

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')

        lista_erros = {}

        origem_destino_iguais(origem, destino, lista_erros)
        campo_tem_algum_numero(origem, 'origem', lista_erros)
        campo_tem_algum_numero(destino, 'destino', lista_erros)
        data_ida_maior_que_data_volta(data_ida, data_volta, lista_erros)
        data_ida_menor_que_data_pesquisa(data_ida, data_pesquisa, lista_erros)

        for campo, erro in lista_erros.items():
            self.add_error(campo, erro)

        return self.cleaned_data


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['nome']
