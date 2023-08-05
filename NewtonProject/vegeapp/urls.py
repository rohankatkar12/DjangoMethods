from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.addreceipes, name="addreceipes"),
    path('showreciepe/', views.showreciepe, name="showreciepe"),
    path('deletereciepe/<int:id>', views.deletereciepe, name="deletereciepe"),
    path('editreciepe/<int:id>', views.editreciepe, name="editreciepe")
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()