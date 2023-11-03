import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from order.models import Pedidos

class PedidosAtualizar(forms.ModelForm):    

    class Meta:
        model = Pedidos
        exclude = ('id_pedidos', 'nome', 'email', 'telefone', 'arquivo', 'mensagem', 'criacao')

    def clean_cpf_pagamento(self):
        data = self.cleaned_data['cpf_pagamento']

        if data:
            if data > 99999999999 or data < 100000000:
                raise ValidationError(_('Valor invalido de CPF'))

        return data

    def clean_cpf_envio(self):
        data = self.cleaned_data['cpf_envio']

        if data:
            if data > 99999999999 or data < 100000000:
                raise ValidationError(_('Valor invalido de CPF'))

        return data

    def clean_valor_produto(self):
        data = self.cleaned_data['valor_produto']

        if data:
            if data > 99999 or data < 0:
                raise ValidationError(_('Valor invalido para o produto'))

        return data

    def clean_valor_frete(self):
        data = self.cleaned_data['valor_frete']

        if data:
            if data > 999 or data < 0:
                raise ValidationError(_('Valor invalido para o frete'))

        return data

    def clean_prazo(self):
        data = self.cleaned_data['prazo']

        if data:
            if data < datetime.date.today():
                raise ValidationError(_('Selecione um dia maior do que hoje'))

        return data

    def clean_envio_orcamento(self):
        data = self.cleaned_data['envio_orcamento']

        if data:
            if data < datetime.date.today():
                raise ValidationError(_('Selecione um dia maior do que hoje'))
            elif (dprazo := self.cleaned_data['prazo']):
                if data > dprazo:
                    raise ValidationError(_('Data do envio do orcamento nao deve ser maior do que o prazo!'))
            else:
                raise ValidationError(_('Data do prazo deve ser superior a data do orcamento!'))

        return data

    def clean_pagamento(self):
        data = self.cleaned_data['pagamento']

        if data:
            if data < datetime.date.today():
                raise ValidationError(_('Selecione um dia maior do que hoje'))
            elif (dprazo := self.cleaned_data['envio_orcamento']):
                if data < dprazo:
                    raise ValidationError(_('Data do pagamento deve ser posterior a do envio do orcamento!'))
            else:
                raise ValidationError(_('Data do pagamento deve ser superior a data do orcamento!'))

        return data

    def clean_despacho(self):
        data = self.cleaned_data['despacho']

        if data:
            if data < datetime.date.today():
                raise ValidationError(_('Selecione um dia maior do que hoje'))
            elif (dprazo := self.cleaned_data['pagamento']):
                if data < dprazo:
                    raise ValidationError(_('Data do pagamento deve ser anterior a do despacho!'))
            else:
                raise ValidationError(_('Data do despacho deve ser superior a data do pagamento!'))
        return data

    def clean_conclusao(self):
        data = self.cleaned_data['conclusao']

        if data:
            if data < datetime.date.today():
                raise ValidationError(_('Selecione um dia maior do que hoje'))
            elif (dprazo := self.cleaned_data['despacho']):
                if data < dprazo:
                    raise ValidationError(_('Data de despacho deve ser anterior a da conclusao!'))
            else:
                raise ValidationError(_('Data da conclusao deve ser superior a data do despacho!'))
        return data