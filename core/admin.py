from django.contrib import admin

# Register your models here.
from .models import Produto, Cliente

admin.site.register(Produto)
admin.site.register(Cliente)