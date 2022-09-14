from django.contrib import admin

from AppCoder.models import Chat, Nosotros, Noticias, Productos, Selecciones  

admin.site.register(Selecciones)
admin.site.register(Noticias)
admin.site.register(Productos)
admin.site.register(Chat)
admin.site.register(Nosotros)


