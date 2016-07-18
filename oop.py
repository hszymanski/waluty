#!/usr/bin/python


class Kontakty:
    def __init__(self, imie, telefon, mail):
	self.imie = imie
	self.telefon = telefon
	self.mail = mail
    def znaki(self):
	print self.imie, self.telefon, self.mail


a = Kontakty("Stefan", "123-345-678", "stefan@xyz.com")
b = Kontakty("Adam", "987-654-321", "adam@com.pl")
c = Kontakty("Sebix", "997-997-997", "fakdepolis@jp100.pl")


a.znaki()
b.znaki()
c.znaki()
