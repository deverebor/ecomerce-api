from rest_framework import generics, permissions

from .models import User
from .serializers import UsersSerializer


class UsersListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

    def perform_create(self, serializer):
        last_name = serializer.validated_data.get('last_name') or None
        product = serializer.validated_data.get('product') or None
        if last_name is None:
            last_name = "Não disponível"
        serializer.save(last_name=last_name)
        
        if product is None:
            product = "Produto indisponível"
        serializer.save(product=product)

users_list_create_view = UsersListCreateAPIView.as_view()


class UsersDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

users_detail_view = UsersDetailAPIView.as_view()


class UsersUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.DjangoModelPermissions]

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.last_name:
            instance.last_name = instance.name

users_update_view = UsersUpdateAPIView.as_view()


class UsersDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

users_destroy_view = UsersDestroyAPIView.as_view()