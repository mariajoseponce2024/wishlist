from django.contrib import admin
from django.urls import path, include
from blog.views import post_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_list, name='home'),
    path('blog/', include('blog.urls')),
]
