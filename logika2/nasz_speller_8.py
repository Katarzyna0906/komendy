#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Config(object):
    def __init__(self):
        self.number_of_decisions = 8
        self.number_of_states = 15
        # A list of all configs defined for every single state.
        self.states_configs = ['state', 'letters', 'actions', 'letters_solver', 'actions_solver']
        # A list of all configs defined as globals, 
        # not assigned to any particular state.
        self.other_configs = []

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # !!! Only keys defined in states_configs and other_configs 
        # will be visible in your application.!!!
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        
        # States transition matrix
        self.state = self.number_of_states * [self.number_of_decisions * [0]]
        self.state[0] = [1, 2, 3, 4, 5, 6, 7, 9]
        self.state[1] = [1, 1, 1, 1, 1, 1, 1, 0]
        self.state[2] = [2, 2, 2, 2, 2, 2, 2, 0]
        self.state[3] = [3, 3, 3, 3, 3, 3, 3, 0]
        self.state[4] = [4, 4, 4, 4, 4, 4, 4, 0]
        self.state[5] = [5, 5, 5, 5, 5, 8, 5, 0]
        self.state[6] = [11, 12, 13, 14, 6, 6, 6, 0]
        self.state[7] = [7, 7, 7, 0, 7, 7, 0, 0]
	self.state[8] = [8, 8, 8, 8, 8, 5, 8, 0]
	self.state[9] = [9, 9, 9, 9, 9, 10, 9, 0]
	self.state[10] = [10, 10, 10, 10, 10, 9, 10, 0]
	self.state[11] = [11, 11, 11, 11, 11, 11, 11, 0]
	self.state[12] = [12, 12, 12, 12, 12, 12, 12, 0]
	self.state[13] = [13, 13, 13, 13, 13, 13, 13, 0]
	self.state[14] = [14, 14, 14, 14, 14, 14, 14, 0]


       # Letters definition for every state. Normally for every state it should be a collection of strings.
        self.letters = self.number_of_states * [self.number_of_decisions * [""]]
        self.letters[0] = [u"A B C\nD E F",u"G H I\nJ K L",u"M N O\nP R S",u"T U W Y\nZ SPACJA",u"POLSKIE ZNAKI", u"KOMUNIKATY\n! ?", u"AKCJE", u"CYFRY"]
        self.letters[1] = ["A","B","C","D","E","F","skasuj", u"wróć"]
        self.letters[2] = ["G","H","I","J","K","L","skasuj", u"wróć"]
        self.letters[3] = ["M","N","O","P","R","S","skasuj", u"wróć"]
        self.letters[4] = ["T","U","W","Y","Z", u"SPACJA","  skasuj", u"wróć"]
        self.letters[5] = [u"ą", u"ć", u"ę", u"ł", u"ń", u"następna\nstrona", "skasuj", u"wróć"]
        self.letters[6] = ["EMOCJE","DYSKOMFORT","JEDZENIE\nPICIE","ROZMOWA","?","!","skasuj", u"wróć"]
        self.letters[7] = [u"mów",u"wyczyść", u"skasuj", u"wróć", "", "", "", ""]
	self.letters[8] = [u"ó", u"ś", u"ź", u"ż", "", "poprzednia\nstrona", "skasuj", u"wróć"]
	self.letters[9] = ["0", "1", "2", "3", "4", u"następna\nstrona", "skasuj", u"wróć"]
	self.letters[10] = ["5", "6", "7", "8", "9", "poprzednia\nstrona", "skasuj", u"wróć"]
	self.letters[11] = [u"ŚWIETNIE", u"DOBRZE", u"KIEPSKO", u"ŹLE", "", "", "skasuj", u"wróć"]
	self.letters[12] = [u"NIEWYGODNIE", u"CIEPŁO", u"ZIMNO", u"BOLI", u"TOALETA", "", "skasuj", u"wróć"]
	self.letters[13] = [u"GŁODNA", u"SPRAGNIONA", u"PRZEKĄSKA", u"SERKI!!!", "", "poprzednia\nstrona", "skasuj", u"wróć"]
	self.letters[14] = [u"Cześć,\nco u Ciebie?", u"Jak Ci minął\nweekend?", u"Muszę lecieć!\nDo zobaczenia!", u"Słucham?", "", "poprzednia\nstrona", "skasuj", u"wróć"]

        self.letters_solver = self.number_of_states * [self.number_of_decisions * [""]]
        
        # actions[i][j] will be performed in state i when person is looking on square j
        # If you wish no action - leave it empty.
        # If you have a 'dynamic' state and you want the program to be chosen at runtime, set here a collection of programs - 
        # thanks to corresponding values from actions_solver obci will decide which program to use.
        self.actions = self.number_of_states * [self.number_of_decisions * [""]]
        self.actions[0] = ["", "", "", "", "", "", "", self._finish_action()] 
        self.actions[1] = ["msg('a')", "msg('b')","msg('c')", "msg('d')", "msg('e')", "msg('f')", "backspace()", ""] 
        self.actions[2] = ["msg('g')", "msg('h')", "msg('i')", "msg('j')", "msg('k')", "msg('l')", "backspace()", ""] 
        self.actions[3] = ["msg('m')", "msg('n')", "msg('o')", "msg('p')", "msg('r')", "msg('s')", "backspace()", ""] 
        self.actions[4] = ["msg('t')", "msg('u')", "msg('w')", "msg('y')", "msg('z')", u"msg(u' ')", "backspace()", ""] 
        self.actions[5] = [u"msg(u'ą')", u"msg(u'ę')", u"msg(u'ł')", u"msg(u'ń')", u"msg(u'ś')", "", "backspace()", ""]
        self.actions[6] = ["", "", "", "", "msg('?')", "msg('!')", "backspace()", ""]
        self.actions[7] = ["say()", "clear()", "backspace()", "", "", "", "", ""]
	self.actions[8] = [u"msg(u'ó')", u"msg(u'ś')", u"msg(u'ź')", u"msg(u'ż')", "", "", "backspace()", ""]
	self.actions[9] = [u"msg(u'0')", u"msg(u'1')", u"msg(u'2')", u"msg(u'3')", u"msg(u'4')", "", "backspace()", ""]
	self.actions[10] =[u"msg(u'5')", u"msg(u'6')", u"msg(u'7')", u"msg(u'8')", u"msg(u'9')", "", "backspace()", ""]
	self.actions[11] =[u"msg(u'Czuję się świetnie!')", u"msg(u'Czuję się dobrze.')", u"msg(u'Nienajlepiej się czuję.')", u"msg(u'Czuję się źle.')", "", "", "backspace()", ""]
	self.actions[12] =["choose_command('NIEWYGODNIE')", "choose_command('CIEPLO')", "Commandor.choose_command('ZIMNO')", "choose_command('BOLI')", "choose_command('TOALETA')", "", "backspace()", ""]
	self.actions[13] =["choose_command('GLODNA')", "choose_command('SPRAGNIONA')","choose_command('PRZEKASKA')", "choose_command('SERKI')", "", "", "backspace()", ""]
	self.actions[14] =["choose_command('CZESC')", "choose_command('COTAM')", "choose_command('PAPA')", "choose_command('SLUCHAM')", "", "", "backspace()", ""]

        self.actions_solver = self.number_of_states * [self.number_of_decisions * [""]]

    def _finish_action(self):
        return "finish()"
