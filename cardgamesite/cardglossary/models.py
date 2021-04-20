from django.db import models
import json
# Create your models here.

class CardManager(models.Manager):
    def createCard(self, name, health, strength, type, ability, abilityProperty):
        card = self.create(name=name, health=health, strength=strength, type=type, ability=ability, abilityProperty=abilityProperty)
        return card

class Card(models.Model):
    class Type(models.TextChoices):
        human = "Human"
        demon = "Demon"
        animal = "Animal"
        omni = "Omni"
        sorcerer = "Sorcerer"
        demigod = "Demigod"

    class Ability(models.TextChoices):
        none = "None"
        taunt = "Taunt"
        shield = "Shield"
        poison = "Poison"
        frenzy = "Frenzy"
        battlecry = "Battlecry"
        overkill = "Overkill"
        active = "Active"
        windfury = "Windfury"

    

    name = models.CharField(max_length=100)
    health = models.PositiveSmallIntegerField(default=1)
    strength = models.PositiveSmallIntegerField(default=1)
    type = models.TextField(choices=Type.choices, default="Human")
    # amount = ?
    ability = models.TextField(choices=Ability.choices, default="None")
    abilityProperty = models.CharField(max_length=100, default="None")

    objects = CardManager()

with open('C:\\Users\\herpa\\Documents\\programming\\python\\cardgame\\monsters.json', 'r') as f:
    monsters = json.load(f)   

# for i in range(len(monsters)):

# card = Card.objects.createCard("Jerry", 1, 1, "Human", "", "")
    
# this is purely a code reference and nothing more, it does not serve a purpose in this code
# class BookManager(models.Manager):
#     def create_book(self, title):
#         book = self.create(title=title)
#         # do something with the book
#         return book

# class Book(models.Model):
#     title = models.CharField(max_length=100)

#     objects = BookManager()

# book = Book.objects.create_book("Pride and Prejudice")