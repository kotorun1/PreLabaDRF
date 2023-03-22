from .models import Product, Cart, Order
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import ProductSerializer, CartSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from django.http import JsonResponse
class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

class CartList(ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Cart.objects.all()
        else:
            return Cart.objects.filter(user=self.request.user)


class CartDetail(RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Cart.objects.all()
        else:
            return Cart.objects.filter(user=self.request.user)

class OrderList(ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Order.objects.all()
        else:
            return Order.objects.filter(cart__user=self.request.user)

class OrderDetail(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return JsonResponse({'message': 'Successfully logged out', 'status': 200})
        except Exception:
            return JsonResponse({'message': 'Something went wrong'}, status=400)