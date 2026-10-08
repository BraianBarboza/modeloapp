from django.db import models

class Client(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    first_name = models.CharField('nome', max_length=100)
    last_name = models.CharField('sobrenome', max_length=100)
    address = models.CharField('endereço', max_length=200)
    phone = models.CharField('telefone', max_length=20)
    email = models.EmailField('e-mail')
    gender = models.CharField('gênero', max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'