#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
      self.brand = brand
      self.size = size
        
    def brand(self):
        return self._brand
    
    def brand(self, brand):
        self._brand = brand
        
    def size(self):
        return self._size
    
    def shoe(self, size):
        if (size, int):
            self._size = size
        else:
            print("size must be an integer")
    
    def condition(self):
        return self._condition
    
    def cobble(self):
        self._condition = "New"
        print("Your shoe is brand new!")

stan_smith = Shoe("Adidas", 9)
print(stan_smith.brand)
print(stan_smith.size)
print(stan_smith.cobble)
print(stan_smith.condition)