from django.db import models


class Categoria(models.Model):
    """
    Model representing a category.
    """
    descricao = models.CharField(max_length=100, unique=True, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return f"Descrição da Categoria: ({self.id})-{self.descricao.lower()}"