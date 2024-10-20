#
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('accounts/', include('django.contrib.auth.urls')),  # Built-in auth URLs
    path('reviews/', include('reviews.urls')),  # Include your reviews app URLs
    path('', RedirectView.as_view(url='/reviews/')),
]

