from django.db import models

ESTADOS = [
    ('PR', 'PARANVAI'),
    ('SP', 'SÃO PAULO'),
    ('RJ', 'RIO DE JANEIRO'),
]


class Cidade(models.Model):
    nome = models.CharField(max_length=50)
    estado = models.CharField(max_length=2, choices=ESTADOS)

    def __str__(self):
        return "{}  ({})".format(self.nome, self.estado)

class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=50, verbose_name="Qual o seu nome?", help_text="Digite seu nome completo")
    nascimento = models.DateField(verbose_name="Data de nascimento")
    email = models.EmailField(max_length=50)

    cidade = models.ForeignKey(Cidade, on_delete = models.PROTECT)

    def __str__(self):
        return "{} + {} + {} + {}".format(self.nome_completo, self.nascimento, self.email, self.cidade)
# Create your models here.
