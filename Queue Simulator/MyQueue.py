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

class MyQueue:

  def __init__(self):
    self.items = []

  def __str__(self):
    output = ""
    for x in self.items:
      output = output + str(x) + " "
    return "[ " + output + "]"

  def __len__(self):
    return len(self.items)

  def isEmpty(self):
    return self.items == []

  def enqueue(self, item):
    self.items.insert(0, item)

  def dequeue(self):
    return self.items.pop()