from random import randint as r
from numpy import exp
import random as rand

#sigmoid function calculation
sigmoid = lambda x : 1.0 / (1.0 + exp(-x))

class neuron:
    def __init__(self, number_of_inputs, number_of_outputs, new_value_seed, mutation_chance):
        self.number_of_inputs = number_of_inputs
        self.number_of_outputs = number_of_outputs
        self.new_value_seed = new_value_seed
        rand.seed(self.new_value_seed)
        self.values = [r(-6,6) for a in range(self.number_of_inputs)]
        self.mutation_chance = mutation_chance
    def mutate(self):
        rand.seed(self.new_value_seed)
        for index, i in enumerate(self.values):
            if r(1, self.mutation_chance) == 1:
                self.values[index] = (i+r(-3,3)+rand.random())%7
        if r(1, self.mutation_chance) == 1:
            self.multiplier = (rand.random()+self.multiplier)%2
        self.new_value_seed = rand.random()
    def add_input(self):
        self.number_of_inputs += 1
        rand.seed(self.new_value_seed)
        self.values.append(r(-6,6))
        self.new_value_seed = rand.random()
    def del_input(self):
        self.number_of_inputs -= 1
        rand.seed(self.new_value_seed)
        self.values = self.values[0: len(self.values)-1]

