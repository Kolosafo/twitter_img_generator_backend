from django.urls import path
from django.views.generic import TemplateView
from . import views

from django.conf import settings
from django.conf.urls.static import static
from . views import design_profile


app_name = 'build'
urlpatterns = [
    path('', views.design_profile, name="design_profile"),
    path('getViewCount/', views.getViewCount, name="getViewCount"),
    path('getRealCount/', views.getRealCount, name="getRealCount"),
    path('updateViewCount/', views.updateViewCount, name="updateViewCount"),
    path('contactUs/', views.contactUs, name="contactUs"),
    path('receipt/', views.TransactionReceiptFunc, name="receipt"),
    path('realCount/', views.realDownloadsCount, name="realCount"),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
