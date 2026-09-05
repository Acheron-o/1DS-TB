from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=1024)
    ativa = models.BooleanField(default=True)

    def __str___(self):
        return self.nome