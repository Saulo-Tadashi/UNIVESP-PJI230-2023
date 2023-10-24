from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('main.urls')),
    path('', RedirectView.as_view(url='/home/')),
    path('order/', include('order.urls')),
    path('auth/', include('authentication.urls')),
]

# incluir /media como caminho estático em modo DEBUG. Para produção deve ser configurado o servidor
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
