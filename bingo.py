import random
import copy

class bingo_number_draw:
    def __init__(self,_number_balls=15*5):
        self.__number_balls__ = _number_balls
        self.__vec_number_drawn__ = []
        self.__random_draw_list__ = random.sample(range(1,self.__number_balls__+1),self.__number_balls__)
    
    def get_all_values_drawn(self):
        return(self.__random_draw_list__)
    
    def get_new_draw(self):
        self.__vec_number_drawn__ = []
        self.__random_draw_list__ = random.sample(range(1,self.__number_balls__+1),self.__number_balls__)
    
    def get_single_draw(self):
        number_drawn = self.__random_draw_list__.pop()
        self.__vec_number_drawn__.append(number_drawn)
        return(number_drawn)

class bingo_card:
    def __init__(self,_min=1,_max=15,_num_n=5):
        self.card = {}
        self.__number_draws_to_win__ = 0
        self.__number_max_per_dimension__ = _max
        self.__number_dimensions__ = _num_n
        self.__vec_number_drawn__ = []
        self.__get_card__(_min,self.__number_max_per_dimension__)

    def __str__(self):
        return('\n'.join('\t'.join((letter, *map(str,values))) for letter,values in self.card.items()))

    def __get_card__(self,_min=1,_max=15):
        self.card = {}
        self.__number_draws_to_win__ = 0
        self.__vec_number_drawn__ = []
        for letter in 'BINGO':
            self.card[letter] = random.sample(range(_min,_max),self.__number_dimensions__)
            _min += self.__number_max_per_dimension__
            _max += self.__number_max_per_dimension__
        self.card["N"][2] = "X"
        self.original_card = copy.deepcopy(self.card)
    
    def get_all_values_card(self):
        return(self.card)
    
    #Returns all the values the bingo thinks have been drawn...
    def get_all_values_drawn(self):
        return(self.__random_draw_list__)
    
    def get_number_of_markups(self):
        return(self.__number_draws_to_win__)
    
    def get_new_card(self,_min=1,_max=15):
        self.__get_card__(_min,_max)
    
    def reset_card_to_start(self):
        self.card = copy.deepcopy(self.original_card)
        self.__number_draws_to_win__ = 0
        self.__vec_number_drawn__ = []
    
    def markup_card(self,val_number):
        self.__vec_number_drawn__.append(val_number)
        self.__number_draws_to_win__ += 1
        for letter in self.card:
            # don't track an index here, use enumerate
            for i,number in enumerate(self.card[letter]):
                if(number==val_number):
                    self.card[letter][i] = "X"
                    break
    
    def markup_card_vector_draws(self,vec_numbers_drawn,is_print=False):
        for i,val_number_drawn in enumerate(vec_numbers_drawn):
            self.markup_card(val_number_drawn)
            if(self.check_win()):
                if(is_print):
                    print('WON After',self.__number_draws_to_win__,'Draws')
                break
    
    def check_win(self):
        # down to the right
        if all(self.card[key][idx]=='X' for idx,key in enumerate(self.card)):
            return(True)

        # up to the right
        elif all(self.card[key][idx]=='X' for idx,key in zip(reversed(range(self.__number_dimensions__)),self.card)):
            return(True)

        # horizontal condition
        for row in self.card.values():
            if all(item=='X' for item in row):
                return(True)

        # vertical condition
        for column in zip(*self.card.values()):
            if all(item=='X' for item in column):
                return(True)
        return(False)

    @staticmethod
    def check_line(values):
        for line in values:
            if all(val=='X' for val in values):
                return True
