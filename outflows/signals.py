from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Outflow


@receiver(post_save, sender=Outflow)
def update_product_quantity(sender, instance, created, **kwargs):
    if created:   # somente se for gerado um NOVO registro em Outflow
        if (
            instance.quantity > 0
        ):   # verifica se a quantidade de saida é maior que zero
            product = (
                instance.product
            )   # verifica o produto na instancia de saida
            product.quantity -= (
                instance.quantity
            )   # altera a quantidade em product
            product.save()
