#!/usr/bin/env python3

class Book:
    def __init__(self, title, page):
        self.title = title
        self.page = page
        
    def title(self):
        return self._title
    
    def title(self, title):
        self._title = title
        
    def page(self):
        return self._page
    
    def page(self, page):
        if (page, int):
            self._page = page
        else:
            print("page must be an integer")
    
    def turn_page(self):
        print("Flipping the page...wow you read fast! ")

book = Book("And Then There Were None", 272)
print(book.title)
print(book.page)
print(book.turn_page)