import numpy as np 
from random import random, randint, choice
from shapes import circle

class DNA():
    def __init__(self, func, delta=10, **kwargs):
        self.func, self.best, self.genes = func, False, None
        for key, value in kwargs.items():
            if key == 'size':
                self.size = value
            if key == 'upper_bound_vector':
                self.upper_bound = value
            if key == 'lower_bound_vector':
                self.lower_bound = value
            if key == 'genes':
                self.genes = value
        if self.genes is None:
            self._CreatesGenes()

    def _CreatesGenes(self):
        self.genes = np.array([self._RandomU(self.upper_bound[i], self.lower_bound[i]) for i in range(self.size)])

    def _RandomU(self, sup, inf):
        return (sup - inf) * random() + inf
    
    def Fitness(self):
        return self.func(self.genes)

    def Mutation(self, mutation_rate):
        for i in range(len(self.genes)):
            if random() < mutation_rate:
                self.genes[i] = self._RandomU(self.upper_bound[i], self.lower_bound[i])

    def CrossOver(self, partner):
        if self.size > 4:
            r = randint(1, self.size)
        elif self.size == 2:
            r = 1
        elif self.size == 3:
            r = 2
        elif self.size == 1:
            r = 0
        genes = np.hstack((self.genes[0:r], partner.genes[r:self.size]))
        return DNA(func=self.func, size=self.size, upper_bound_vector=self.upper_bound, lower_bound_vector=self.lower_bound, genes=genes)

    def show(self, delta):
        if self.best:
            color = (0, 255, 0)
        else:
            color = (0, 0, 255)
        x = self.genes[0]*delta[1] + delta[0]
        y = self.genes[1]*delta[1] + delta[0]
        circle(x, y, radius=5, color=color)