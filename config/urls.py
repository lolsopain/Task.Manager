from django.contrib import admin
from django.urls import path
from tasks.views import home, easy, medium, hard

urlpatterns = [
    path('', home),
    path('easy/', easy),
    path('medium/', medium),
    path('hard/', hard),
    path('admin/', admin.site.urls),
]