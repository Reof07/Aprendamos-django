from django.db import models

# Importamos RichTextDield para sustitir el campo TextFiel del attr contenido en el modelo.
from ckeditor.fields import RichTextField

# Create your models here.
class Categorias(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre de la Categoria',
        max_length = 100,
        null = False,
        blank = False
        )
    estado = models.BooleanField('Categoria Act/Deact', default = True )
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now = False,
        auto_now_add= True
        )

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return '{}'.format(self.nombre)    


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField('Nombres',
        max_length=255,
        null= False,
        blank= False
        )
    apellidos = models.CharField('Apellidos',
        max_length = 255,
        null = False,
        blank = False 
        )
    facebook = models.URLField('Facebook', null = True,
        blank = True)
    twiter = models.URLField('Twitter', null = True,
        blank = True
        )
    instagram = models.URLField('Instagram', null = True,
        blank = True
        )
    web = models.URLField('web', null = True,
        blank = True
        )  
    correo = models.EmailField('Correo Electronico', null = False,
        blank = False
        )
    estado = models.BooleanField('Estado Autor Act/Deact',
        default = True
        )                      
    fecha_creacion = models.DateField('Fecha de Creacion',
        auto_now= False,
        auto_now_add= True
        )     

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural ='Autores'

    def __str__(self):
        return '{} {}'.format(self.apellidos,
            self.nombres) 

class Post(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField('Titulo', max_length = 90,
        blank = False,
        null = False
        )
    slug = models.CharField('Slug', max_length = 100,
        blank = False,
        null = False
        )
    descripcion = models.CharField('Descripcion', 
        max_length = 110,
        blank = False,
        null = False
        )
    contenido = RichTextField() # Este campo es herdad de ckeditor.
    imagen = models.URLField(max_length = 255,
        blank = False,
        null = False
        )
    autor = models.ForeignKey(Autor,
        on_delete = models.CASCADE)   
    categoria = models.ForeignKey(Categorias,
        on_delete = models.CASCADE)
    estado = models.BooleanField('Estado', default = True)
    fecha_creacion = models.DateField('Fecha de Creacion', 
        auto_now = False,
        auto_now_add = True )

    class Meta: 
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return '{}'.format(
            self.titulo
        )    