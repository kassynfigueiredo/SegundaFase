from django.forms import ModelForm, fields
from aplicativo.models import Empresas


class EmpresasForm(ModelForm):
    class Meta:
        model = Empresas
        fields = ['nome', 'servicos', 'cnpj']
