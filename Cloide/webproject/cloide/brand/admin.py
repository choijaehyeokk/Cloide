from django.contrib import admin
from .models import Brand
from .models import Agesex, Stylekind
from .models import Yvideo
from embed_video.admin import AdminVideoMixin

# Register your models here.
admin.site.register(Brand)
admin.site.register(Agesex)
admin.site.register(Stylekind)

class YvideoAdmin(AdminVideoMixin, admin.ModelAdmin): 
    list_display = ('title', 'video')
    
admin.site.register(Yvideo, YvideoAdmin)


