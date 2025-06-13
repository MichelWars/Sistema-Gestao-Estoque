from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Inflow


@receiver(post_save, sender=Inflow)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:   # somente se for gerado um NOVO registro em Inflow
        if (
            instance.quantity > 0
        ):   # verifica se a quantidade de entrada é maior que zero
            product = (
                instance.product
            )   # verifica o produto na instancia de entrada
            product.quantity += (
                instance.quantity
            )   # altera a quantidade em product
            product.save()
