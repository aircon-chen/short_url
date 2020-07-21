from django.urls import path, re_path

from short_url import views

urlpatterns = [
    path('rest/v1/short', views.ShortUrlAPIView.as_view(), name='short_url_api'),
    path('', views.IndexView.as_view(), name='index_page'),
    path('<encode>', views.ShortUrlRedirectView.as_view(), name='redirect_page'),
]
