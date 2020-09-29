from django.contrib import admin
from .models import Brand
from .models import Agesex, Stylekind

# Register your models here.
admin.site.register(Brand)
admin.site.register(Agesex)
admin.site.register(Stylekind)