from django.urls import path

from .views import ItemView, StoreView

app_name = 'store'
urlpatterns = [
    path('', StoreView.as_view(), name='store'),
    path('<int:pk>/', ItemView.as_view(), name='item'),
]
