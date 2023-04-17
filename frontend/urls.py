from django.urls import path

from frontend import views
from django.utils.translation import gettext_lazy as _
urlpatterns = [
    path('graphics-cards/', views.IndexView.as_view(), name='index'),
    path(r'graphics-cards/<c_val_1>-vs-<c_val_2>/', views.CompareView.as_view(), name='compare'),
    path(r'graphics-cards/<selected>/', views.DetailView.as_view(), name='detail'),
]
