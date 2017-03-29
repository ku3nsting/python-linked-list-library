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

    def removeNode(self, book):
            searchNode = self.sentinel
            for index in range(self.numNodes):
                if searchNode.data == book:
                    searchNode.prev.next = searchNode.next
                    searchNode.next.prev = searchNode.prev
                    self.numNodes = self.numNodes - 1
                    "Book removed from library"
                    return
                else:
                    searchNode = searchNode.next
            print "Book not found in library"

    def printLibrary(self):
            print "\n"
            print "  \tPrinting Library\n"
            printNode = self.sentinel
            #iterate through all existing books
            for index in range(self.numNodes):
                #Print index and title
                print str(index + 1) + "\tTitle:\t\t\t" + str(printNode.next.data.title)
                #Print author name
                print "\tAuthor:\t\t\t" + str(printNode.next.data.author)
                #Print publication date
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

#***********************************
# Input validation function:
# Loops for more input if user-
# supplied values are invalid.
#***********************************
def validate_ints(number):
    while True:
        number = input()
        try:
            number = int(number)
        except ValueError:
            print "Invalid Input. Please try again:\n"
            continue

        if (0 < number):
            return number
        else:
            print "Invalid Input. Please try again:\n"
            continue

def testLibrary():
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
        #PRINT BOOKS
        #******************************************#
        newLibrary.printLibrary()

        #******************************************#
        #ADD BOOKS
        #******************************************#
        newLibrary.removeNode(a)
        newLibrary.removeNode(c)
        print "books removed"

        #******************************************#
        #PRINT BOOKS
        #******************************************#
        newLibrary.printLibrary()

        #******************************************#
        #ADD BOOKS
        #******************************************#
        newLibrary.addNode(a)
        newLibrary.addNode(c)
        print "books added"

        #******************************************#
        #PRINT BOOKS
        #******************************************#
        newLibrary.printLibrary()


#******************************************#
#MAIN PROGRAM
#******************************************#

keepGoing = 2

while (keepGoing == 2):

    print "*** Linked List Library Program ***\t"

    print " 1.\t Run automated test"
    print " 2.\t Run interactive test"
    print " 3.\t Quit"

    print "\n Input your choice, then press ENTER:\n"

    choice = 0
    choice = validate_ints(choice)

    #******************************************#
    #AUTOMATED TEST
    #******************************************#
    if choice == 1:
        print "*** AUTOMATED TEST ***\n"
        testLibrary()

    #******************************************#
    #INTERACTIVE TEST
    #******************************************#
    if choice == 2:
        print "*** INTERACTIVE TEST ***"
        print "\n    Begin interactive test?"


    #-----------------------------
    # ASK USER WHETHER TO CONTINUE
    #-----------------------------
    if choice == 3:
        print "Are you sure you want to quit?"
        print "1. \tYes"
        print "2. \tNo\n"
        print "Input your selection, then press ENTER:\n"
        keepGoing = validate_ints(keepGoing);

print "Thanks for using Calendar Generator!"
print "\n"















        

