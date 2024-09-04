# views.py
from .models import OrderItem 
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        # Extract the items data from the request
        items_data = self.request.data.get('items', [])

        # Create the order instance
        order = serializer.save()

        # Create related order items
        for item_data in items_data:
            OrderItem.objects.create(
                order=order,
                product_name=item_data['product_name'],
                sku=item_data['sku'],
                price=item_data['price'],
                quantity=item_data['quantity']
            )
class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer