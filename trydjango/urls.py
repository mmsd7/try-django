from django.contrib import admin
from django.urls import path
from .views import home_view
from articles.views import article_detail_view



urlpatterns = [
    path('', home_view),
    path('articles/<int:id>/', article_detail_view),
    path('admin/', admin.site.urls),
]
