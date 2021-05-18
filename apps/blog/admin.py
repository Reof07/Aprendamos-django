from django.contrib import admin

# import modulos import/export
from import_export import resources
from import_export.admin import ImportExportModelAdmin


from .models import  (Categorias,
     Autor,
     Post)
# Register your models here.

class CategoriaResource(resources.ModelResource):
    '''
    Esta clase es usada para configurar el import y
    export files en la instancia Categorias desde
    mi sitio admin.
    '''
    class meta:
        model = Categorias

class AutorResource(resources.ModelResource):
    '''
    Esta clase es usada para config el import y
    export files en la instancia Autor desde mi
    sitio admin.
    '''
    class Meta:
        model = Autor        

class CategoriaAdmin( ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','estado','fecha_creacion',)
    resource_class = CategoriaResource

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombres','apellidos','correo']
    list_display = ('nombres', 'apellidos', 'facebook',
        'twiter', 'instagram', 'web', 'estado',
        'fecha_creacion'
        )
    resource_class = AutorResource    

admin.site.register(Categorias, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post)