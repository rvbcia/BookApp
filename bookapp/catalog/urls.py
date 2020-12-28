from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('add_book/', views.add_book, name='add_book'),
]

urlpatterns += [
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
]

urlpatterns += [
    path('catalog/', views.index, name='catalog'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path('edit_book/<int:pk>', views.edit_book, name='edit_book'),
]
