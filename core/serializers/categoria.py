from rest_framework.serializers import ModelSerializer

from core.models import Categoria


class CategoriaSerializer(ModelSerializer):
    """
    Serializer for the Categoria model.
    """

    class Meta:
        model = Categoria
        fields = '__all__'
        read_only_fields = ['id']
