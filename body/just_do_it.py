from dataclasses import dataclass
from random import choice

@dataclass
class Basquets:
    def nike(file):
        file = file
        rand_items = []
        
        for items in file:
            while rand_items == len(20):
                rand_choice = choice(file)
                if rand_choice not in rand_items:
                    rand_items.append(rand_choice)
        return rand_items