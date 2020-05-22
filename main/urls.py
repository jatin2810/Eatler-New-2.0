from django.conf.urls import url
from .views import homepage
from django.urls import path
<<<<<<< HEAD
# from .views import ProductFormView,RestaurantFormView
from .views import RestaurantCreateView,RestaurantListView
=======

>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866
app_name='main'

urlpatterns = [
    path('',homepage,name='homepage'),
<<<<<<< HEAD
    # path('add_product/',ProductFormView,name="add_product"),
    # path('add_restaurant/',RestaurantFormView,name="add_restaurant"),
    path('list/',RestaurantListView.as_view(),name="list_restaurant"),
    path('create/',RestaurantCreateView.as_view(),name="create_restaurant"),
    # path('<int:pk>/',RestaurantDetailView.as_view(),name="detail_restaurant"),
=======
>>>>>>> 8340de6a7036a5ac611f29420cac6d13e4726866
]
