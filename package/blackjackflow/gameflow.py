from typing import Dict, List

class SittingPerson :
    name = 'name'
    bet  = 0
    cardlist = []
    
    def __init__(self, name : str):
        self.name = name

    def newcard(self, card) :
        self.cardlist.append(card)

class Settings :
    def __init__(self, number_of_person) :
        self.person = number_of_person


class Bet:
    def __init__(self, settings) :
        self.settings = settings


class NoBetPlease :
    def __init__(self) :
        pass