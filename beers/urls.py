from django.urls import path

from .views import BeerListView

urlpatterns = [
    path('', BeerListView.as_view(), name='beer_list')
]
