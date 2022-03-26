from rest_framework import generics, permissions

from .models import Seller
from .serializers import SellersSerializer


class SellersListCreateAPIView(generics.ListCreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellersSerializer

    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        company_name = serializer.validated_data.get('company_name') or None
        product = serializer.validated_data.get('product') or None
        if company_name is None:
            company_name = f"{name}'s company"
        serializer.save(company_name=company_name)
        
        if product is None:
            product = "Produto indisponível"
        serializer.save(product=product)

sellers_list_create_view = SellersListCreateAPIView.as_view()


class SellersDetailAPIView(generics.RetrieveAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellersSerializer

sellers_detail_view = SellersDetailAPIView.as_view()


class SellersUpdateAPIView(generics.UpdateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellersSerializer
    permission_classes = [permissions.DjangoModelPermissions]

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.company_name:
            instance.company_name = instance.name

sellers_update_view = SellersUpdateAPIView.as_view()


class SellerDestroyAPIView(generics.DestroyAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellersSerializer

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

sellers_destroy_view = SellerDestroyAPIView.as_view()