from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    Django Rest Framework API View
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"error": "Invalid data"}, status=400)