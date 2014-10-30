# coding: utf-8
from django.shortcuts import render
from django.views.generic.list  import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Hacer

# Función que usa un decorador para asignar un permiso, aplicado a una función
@method_decorator(permission_required('gactividades.listar_app_hacer'))
def listar(request):
    porhacer = Hacer.objects.all()
    return render(request, 'gactividades/listar.html', {'porhacer', porhacer})

class HacerList(ListView):
    model = Hacer

@method_decorator(permission_required('gactividades.agregar_app_hacer'))
class HacerCreate(CreateView):
    pass

@method_decorator(permission_required('gactividades.modificar_app_hacer'))
class HacerUpdate(UpdateView):
    pass

@method_decorator(permission_required('gactividades.eliminar_app_hacer'))
class HacerDelete(DeleteView):
    pass


