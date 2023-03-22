from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import CartList, CartDetail, OrderList, OrderDetail, ProductList, ProductDetail, LogoutView



from .views import CartList, CartDetail, OrderList, OrderDetail, ProductList, ProductDetail
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/logout/', LogoutView.as_view(), name='logout'),
    path('products/', ProductList.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('carts/', CartList.as_view(), name='cart_list'),
    path('carts/<int:pk>/', CartDetail.as_view(), name='cart_detail'),
    path('orders/', OrderList.as_view(), name='order_list'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order_detail'),


    
]