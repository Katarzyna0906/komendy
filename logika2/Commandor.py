# -*- coding: utf-8 -*-
# Author:
#     Zespol wzespol

class Commandor(object):
	import pygame
	def __init__(self)#, params):np glosnosc
		pass
	def choose_command(self, napis):#, sciezkaPlikuMp3):
		self.napis = napis
		self.clear()
		self.msg(napis)
		plikmp3 = napis + '.mp3'
		#pygame.init()
		#pygame.mixer.init()
		#pygame.mixer.music.load(plikmp3)
		#pygame.mixer.music.play()
		#while pygame.mixer.music.get_busy(): 
		#    pygame.time.Clock().tick(10)

		#po wybraniu pola z tekstem (komenda typu "mam katar"):
		#kasuje sie tekst z pola msg
		#zapisuje tekst z pola o danym numerze w polu msg
		#nastepnie puscza sciezke dzwiekowa odpowiadajaca danemu polu
