
from mysite import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static

urlpatterns = [
    path('', TemplateView.as_view(template_name='welcome.html'), name='welcome'),
    path('admin/', admin.site.urls),
    path('reg/', include('reg.urls')),
    path('reg/', include('django.contrib.auth.urls')),
    path('line/', include('line.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)