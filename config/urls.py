from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('auth/', include('apps.account.urls')),
        path('', include('apps.donate.urls'))
    ]))
]
