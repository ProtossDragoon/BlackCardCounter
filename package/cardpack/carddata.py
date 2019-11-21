import sys

class NonExistenceError(Exception):
    def __init__(self, msg) :
        print(msg)
    pass


class Card :
    def __init__(self, number, shape, JQK = None) :
        self.number = number
        self.shape = shape

        if self.number == 1 :
            print('A!')
            self.JQK = None
        elif self.number == 10 :
            self.JQK = JQK
            if JQK == 'J' :
                print('J')
            elif JQK == 'Q' :
                print('Q')
            elif JQK == 'K' :
                print('K')
            else :
                raise NonExistenceError('J or Q or K card is number 10, but not specified.')
        elif self.number > 0 and self.number < 10 :
            self.JQK = None
        else :
            raise NonExistenceError('card number < 1 or > 10')
        

    def cardnumber(self) :
        return_list = []
        if self.number == 1 :
            return_list.append(1)
            return_list.append(11)
        else :
            return_list.append(self.number)
        return return_list
    
    def cardshape(self) :
        return self.cardshape



class Cardpack :

    heart = {}
    diamond = {}
    clova = {}
    spade = {}
    
    def __init__(self, number_of_cardpack = 1) :

        def cardinitHelper(number_of_cardpack) :
            card_dic = {1 : number_of_cardpack,
                        2 : number_of_cardpack,
                        3 : number_of_cardpack,
                        4 : number_of_cardpack,
                        5 : number_of_cardpack,
                        6 : number_of_cardpack,
                        7 : number_of_cardpack,
                        8 : number_of_cardpack,
                        9 : number_of_cardpack,
                        'J' : number_of_cardpack,
                        'Q' : number_of_cardpack,
                        'K' : number_of_cardpack}
            return card_dic

        self.heart = cardinitHelper(number_of_cardpack)
        self.diamond = cardinitHelper(number_of_cardpack)
        self.clova = cardinitHelper(number_of_cardpack)
        self.spade = cardinitHelper(number_of_cardpack)
