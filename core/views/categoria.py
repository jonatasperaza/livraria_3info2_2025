from rest_framework import viewsets
from core.models import Categoria
from core.serializers import CategoriaSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Categoria model.
    """
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer