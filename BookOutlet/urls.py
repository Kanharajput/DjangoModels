from . import views
from django.urls import path

urlpatterns = [
    path('',views.showBooKList),
    path('<int:id>',views.detailPage)         # id is the slug for url
]
