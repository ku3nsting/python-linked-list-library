#!/usr/bin/env python

##########################################
# LINKED LIST LIBRARY                    #
# A script to practice python linked     #
# lists. A utility to add, search,       #
# remove, and change the state of items  #
# in a library.                          #
# March 29, 2017                         #
##########################################

import types

#******************************************#
#DEFINE BOOK CLASS
#******************************************#

class Book:
    def __init__(self, t, a, pD):
            self.title = t
            self.author = a
            self.pubDate = pD
            self.out = False

#******************************************#
#DEFINE NODE CLASS
#******************************************#
class Node:
    def __init__(self, p, n, book):
            self.prev = p
            self.next = n
            self.data = book

#******************************************#
#DEFINE LIBRARY (container) CLASS
#******************************************#
class Library:
        
    def __init__(self):
            self.sentinel = Node(None, None, None)
            self.sentinel = Node(self.sentinel, self.sentinel, None)
            self.currentNode = self.sentinel
            self.numNodes = 0
            
    def addNode(self, book):
            newNode = Node(self.currentNode, self.sentinel, book)
            self.currentNode.next = newNode
            self.numNodes = self.numNodes + 1
            self.currentNode = newNode

    def printLibrary(self):
            printNode = self.sentinel
            for index in range(self.numNodes):
                print str(index + 1) + "\tTitle:\t\t\t" + str(printNode.next.data.title)
                print "\tAuthor:\t\t\t" + str(printNode.next.data.author)
                print "\tPublication Date:\t" + str(printNode.next.data.pubDate) + "\n"
                printNode = printNode.next


#******************************************#
#INITIALIZE BOOKS
#******************************************#
a = Book("Harry Potter and the Sorcerer's Stone",
        "J.K. Rowling",
        1998,)
b = Book("The Hunger Games",
        "Suzanne Collins",
        2005,)
c = Book("Ramona Quimby",
        "Judy Blume",
        1990,)
d = Book("The Handmaid's Tale",
        "Margaret Atwood",
        1970,)
e = Book("The Giver",
        "Lois Lowry",
        1999,)

#******************************************#
#INITIALIZE LIBRARY
#******************************************#
newLibrary = Library()
#print "Library Created"

#******************************************#
#ADD BOOKS
#******************************************#
newLibrary.addNode(a)
newLibrary.addNode(b)
newLibrary.addNode(c)
newLibrary.addNode(d)
newLibrary.addNode(e)
#print "books added"

#******************************************#
#ADD BOOKS
#******************************************#
newLibrary.printLibrary()




