from django.urls import path

from short_url import views

urlpatterns = {
    path('', views.IndexView.as_view(), name='index_page'),
}