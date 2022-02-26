
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import path, include
#from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('document.urls')),
    #url(r'^download/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
