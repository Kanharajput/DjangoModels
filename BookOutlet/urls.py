from . import views
from django.urls import path

urlpatterns = [
    path('',views.showBooKList),
    path('<slug:slug_in_url>',views.detailPage, name="detail-url")         # id is the slug for url
]
