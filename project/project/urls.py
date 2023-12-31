from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('admin/', admin.site.urls),
   path('pages/', include('django.contrib.flatpages.urls')),

   path('products/', include('simpleapp.urls')),
   path('news/', include('simpleapp.news_urls')),

   path("accounts/", include("allauth.urls")),

   path('', include('simpleapp.urls')),

]
