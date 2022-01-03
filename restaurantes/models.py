from django.db import models
from django.db.models.deletion import CASCADE

class Restaurante(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Prato(models.Model):
    TAGS = (
        ('Aves', 'Aves'),
        ('Arroz','Arroz'),
        ('Doces', 'Doces'),
        ('Bolos', 'Bolos'),
        ('Caldos', 'Caldos'),
        ('Carne', 'Carne'),
        ('Alemã', 'Alemã'),
        ('Americana', 'Americana'),
        ('Árabe', 'Árabe'),
        ('Argentina', 'Argentina'),
        ('Australiana', 'Australiana'),
        ('Baiana', 'Baiana'),
        ('Capixaba', 'Capixaba'),
        ('Chinesa', 'Chinesa'),
        ('Colombiana', 'Colombiana'),
        ('Coreana', 'Coreana'),
        ('Cubana', 'Cubana'),
        ('Espanhola','Espanhola' ),
        ('Francesa', 'Francesa'),
        ('Gaúcha', 'Gaúcha'),
        ('Havaiana', 'Havaiana'),
        ('Indiana', 'Indiana'),
        ('Inglesa', 'Inglesa'),
        ('Italiana', 'Italiana'),
        ('Japonesa', 'Japonesa'),
        ('Judaica', 'Judaica'),
        ('Mexicana', 'Mexicana'),
        ('Mineira', 'Mineira'),
        ('Nordestina','Nordestina'),
        ('Pernambucana', 'Pernambucana'),
        ('Peruana', 'Peruana'),
        ('Simples', 'Simples'),
        ('Suíça', 'Suíça'),
        ('Tailandesa', 'Tailandesa'),
        ('Vegetariana', 'Vegetariana'),
        ('Natal', 'Natal'),
        ('Rápidas', 'Rápidas'),
        ('Frango', 'Frango'),
        ('FrutosdoMar', 'FrutosdoMar'),
        ('Lasanhas', 'Lasanhas'),
        ('Legumes', 'Legumes'),
        ('Massas', 'Massas'),
        ('Molhos', 'Molhos'),
        ('Peru', 'Peru'),
        ('Salada','Salada' ),
        ('Salmão', 'Salmão'),
        ('Sanduiches','Sanduiches'), 
        ('Light', 'Light'),
        ('Diet', 'Diet'),
        ('Portuguesas', 'Portuguesas'),
        ('-','-')
    )
    nome = models.CharField(max_length=50)
    tag = models.CharField(max_length=15, choices=TAGS, blank=False, null=False, default='-')
    imagem = models.ImageField(blank=True)
    descricao = models.TextField(max_length=500)
    restaurante = models.ForeignKey(Restaurante, on_delete=CASCADE)

    def __str__(self):
        return self.nome