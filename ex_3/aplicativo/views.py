from django.shortcuts import render, redirect
from aplicativo.forms import EmpresasForm
from aplicativo.models import Empresas

# Create your views here.


def home(request):
    data = {}
    data['db'] = Empresas.objects.all()
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = EmpresasForm()
    return render(request, 'form.html', data)


def create(request):
    form = EmpresasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {}
    data['db'] = Empresas.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Empresas.objects.get(pk=pk)
    data['form'] = EmpresasForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Empresas.objects.get(pk=pk)
    form = EmpresasForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


def delete(request, pk):
    db = Empresas.objects.get(pk=pk)
    db.delete()
    return redirect('home')
