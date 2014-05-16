#  Files: MyQueue.py, WidgetWorks.py
#
#  Description: This program will simulate placing an online ordering system using queues
#
#  Student's Name: Andrew Baldwin
#
#  Student's UT EID: amb4437
#
#  Course Name: CS 313E 
#
#  Date Created: 10/02/11
#
#  Date Last Modified:  10/02/11

from MyQueue import *
import string


class Order:

  def __init__(self):
    self._items = []
    
  def __str__(self):
    return str(self._items)
  
  def number(self, num):
    return self.number
  
  def name(self, name):
    return self.name
    
  def color(self, col):
    return self.color
  
  def quantity(self, quan):
    return self.quantity



def main():

  i = 0
  y= MyQueue()
  x = Order()
  
  while True:
  
    end = False
    
    print ("Welcome to the Waskelly Wabbit Widget Works automated ordering system!")
    print ('')
  
    name = input ("Please input customer name (or exit) ")
    if (name == "exit"):
      print ('')
      print ("Now processing orders: ")
      break
    else:
      x.name=name
      
      
    
    color = input ("Please select desired widget color (red, white, blue) ")    ## Ask the user for a color
    color=color.lower()
    if (color == "red"):
      x.color=color
    elif (color == "white"):
      x.color=color
    elif (color == "blue"):
      x.color=color
    else:
      end = True
    if end == True:    ##If the color is invalid, start the ordering process over
      print ("Sorry, that's not a color we offer. Order cancelled.")
      print ('')
      continue
      
      
      
    quan = input (("Excellent choice, how many %s widgets do you want? ") % (x.color))
    if (quan.isdigit()):			#Ask for the quantity and make sure that the input is valid
      x.quantity=quan
      print ("Order confirmed!  Please shop with us again.")
      print ('')
    else:
      end = True
    if end == True:					## If the input is invalid, restart the ordering process
      print ("Bad quantity. Order cancelled")
      print ('')
      continue
    
    
    
    
    i = i + 1				##Keep track of the number of orders
    x.number= i
  
  
  
    ## Add the successful order to the queue
    toenq=(("Order %s: customer %s requests %s %s widgets") % (x.number, x.name, x.quantity, x.color))
    y.enqueue(toenq)
    
    
  while not (y.isEmpty()):  
    print (("Order shipped:         %s") % (y.dequeue()))
  else:
    print ("Queue empty")
  
  
main()