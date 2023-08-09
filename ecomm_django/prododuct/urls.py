from django.urls import path, include
from prododuct import views

urlpatterns = [
    path('latest-product/', views.LatestProductsList.as_view())
]