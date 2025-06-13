from django.db import models

from products.models import Product
from suppliers.models import Supplier


class Inflow(models.Model):
    supplier = models.ForeignKey(
        Supplier, on_delete=models.PROTECT, related_name='inflows'
    )
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name='inflows'
    )
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # ordenação por registros mais recentes
    class Meta:
        ordering = ['-created_at']

    # caso a tabela não tenho registro sera retornado um objeto nulo convertido em string para evitar erros
    def __str__(self):
        return str(self.product)
