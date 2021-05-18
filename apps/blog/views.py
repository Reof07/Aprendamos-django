from django.shortcuts import render, get_object_or_404
# libreria ayuda a realizar las consultas en db.
from django.db.models import Q
# importamos paginator para la paginacion.
from django.core.paginator import Paginator


from .models import  ( Autor,
    Categorias,
    Post
)
# Create your views here.
def home(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado = True)
    if queryset:
        #filtramos de acuerdo a la barra de busqueda.
        #__icontains: indica que no importa May o min solo que esta en el contenido
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(descripcion__icontains = queryset)
        ).distinct() #Trae los que son distintos

    #creamos una instancia de paginator
    #paginator recibe dos parametros una lista y la catidad de item por pagina
    paginator = Paginator(posts, 2)
    #obtenemos la pagina actual.
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'index.html',{'posts':posts})

def detallePost(request, slug):
    post = get_object_or_404(Post,
        slug = slug
    )
    return render(request, 'post.html', {'post':post})
   

def articulos(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado = True,
        categoria = Categorias.objects.get(nombre__iexact = 'Articulos')) #__iexact: indica que el filtro no sea exactamente igual al string 
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categorias.objects.get(nombre__iexact = 'Articulos'),

        )
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'articulos.html', {'posts':posts})    

def tecnologia(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado = True,
        categoria = Categorias.objects.get(nombre__iexact = 'Tecnologia')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categorias.objects.get(nombre__iexact ='Tecnologia'),
            
        )
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'tecnologia.html', {'posts':posts})

def tutoriales(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(
        estado = True,
        categoria = Categorias.objects.get(nombre__iexact = 'Tutoriales')
    )
    if queryset:
            posts = Post.objects.filter(
            Q(titulo__icontains = queryset)|
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categorias.objects.get(nombre__iexact ='Tecnologia'),
        )
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'tutoriales.html', {'posts':posts})    