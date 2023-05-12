from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    cate=Categoria.objects.all()
    masc=Mascota.objects.filter(publicar=True).order_by("-idMascota")[:3]
    data={'categorias':cate,'mascotas':masc}
    return render(request,"index.html",data)

def galeria(request):
    mascotas= Mascota.objects.filter(publicar=True)
    cantidad= Mascota.objects.all().count()
    data={'mascotas':mascotas}
    data['cantidad']=cantidad
    return render(request,"galeria.html",data)

def quienes(request):
    return render(request,"quienes_somos.htm")

def formulario(request):
    return render(request,"formulario_perris.html")

def admin_mascota(request):
    cate= Categoria.objects.all()
    data={'categorias':cate}
    if request.POST:
        id= request.POST.get("txtId")
        nom= request.POST.get("txtNombre")
        ed= request.POST.get("txtEdad")
        desc= request.POST.get("txtDesc")
        img = request.FILES.get("txtImg")
        cat = request.POST.get("cboCategoria")
        obj_cat= Categoria.objects.get(nombre=cat)
        mas = Mascota(
            idMascota=id,
            nombre=nom,
            edad=ed,
            descripcion=desc,
            foto=img,
            categoria=obj_cat
        )
        mas.save()
        data['mensaje']="Grabo"
    return render(request,"admin_mascotas.html",data)

def ficha_mascota(request,id):
    mas = Mascota.objects.get(idMascota=id)
    data={"item":mas}
    return render(request,"ficha_mascota.html",data)

def buscar_nombre(request):
    cate=Categoria.objects.all()
    data={'categorias':cate}
    if request.POST:
        nombre = request.POST.get("txtNombre")
        mascotas = Mascota.objects.filter(nombre__contains=nombre)
        data={'mascotas':mascotas}
        return render(request,"galeria.html",data)
    return render(request,"index.html",data)

def buscar_descripcion(request):
    cate=Categoria.objects.all()
    data={'categorias':cate}
    if request.POST:
        desc = request.POST.get("txtNombre")
        mascotas = Mascota.objects.filter(descripcion__contains=desc)
        data={'mascotas':mascotas}
        return render(request,"galeria.html",data)
    return render(request,"index.html",data)

def buscar_categoria(request,id):
    cate=Categoria.objects.get(nombre=id)
    mascotas = Mascota.objects.filter(categoria=cate)
    data={'mascotas':mascotas}
    return render(request,"galeria.html",data) 

def formulario_colaborador(request):
    if request.POST:
        nom=request.POST.get("txtNombre")
        ape=request.POST.get("txtApellido")
        p = request.POST.get("pwdPass1")
        nom_usu= request.POST.get("txtNombreUser")
        usu=User()
        usu.first_name=nom
        usu.last_name=ape
        usu.username=nom_usu
        usu.set_password(p)
        usu.save()
    return render(request,"formulario.html")   
