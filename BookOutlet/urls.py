from . import views
from django.urls import path

urlpatterns = [
    path('',views.showBooKList),
    path('<int:id>',views.detailPage, name="detail-url")         # id is the slug for url
]
