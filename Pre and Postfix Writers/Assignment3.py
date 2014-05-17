#  File: Assignment3.py
#
# Description: This program calculates both infix and postfix expressions
#
# Student's Name: Andrew Baldwin
#
# Student's UT EID: AMB4437	
#
# Course Name: CS 313E 
#
# Date Created: 9/23/11
#
# Date Last Modified: 9/23/11

import string

class Stack:
  """Define a Stack ADT with operations: Stack, isEmpty,
  push, pop, peek, and size."""
  
  def __init__(self):
    self._items = []
    
  def __str__(self):
    return str(self._items)
    
  def isEmpty(self):
    return self._items == []
    
  def push(self, item):
    self._items.append(item)
    
  def pop(self):
    return self._items.pop()
    
  def peek(self):
    return self._items[len(self._items) - 1]
    
  def size(self):
    return len(self._items)
    
    
  def applyOp(self, c, arg1, arg2):
    if c == "+":
      return (arg1 + arg2)
    elif c == "-":
      return (arg1 - arg2)
    elif c == "*":
      return (arg1 * arg2)
    elif c == "/":
      return (arg1 / arg2)
    
  def postEval0(self, symbolString):
    """Given a postfix expression, evaluate it"""
    stack = Stack()
    
    symbolString = (symbolString.split())
    for c in symbolString:
      if c.isdigit():
        stack.push(int(c))
      else:
        if stack.isEmpty():
          return "Ill-formed expression or bad token input"
        else:
          arg1 = stack.pop()
          arg2 = stack.pop()
          val = stack.applyOp(c, arg1, arg2)
          stack.push(val)
    return stack.pop()
    
  def infixToPostfix(self, infixexpr):
  # First set up a dictionary mapping symbols to
  # precedence.
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()
    
    
    for token in tokenList:
    # allows both upper and lowercase
      if token in string.ascii_letters or token.isdigit():
        postfixList.append(token)
      elif token == "(":
        opStack.push(token)
      elif token == ")":
        topToken = opStack.pop()
        while topToken != "(":
          postfixList.append(topToken)
          topToken = opStack.pop()
      else:
        while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
          postfixList.append(opStack.pop())
        opStack.push(token)
    while not opStack.isEmpty():
      postfixList.append(opStack.pop())
    return (' '.join(postfixList))


def main():

  s=Stack()
  
  inf = True
  while True:
    if inf == True:
      entered = input ("Enter an infix expression: ")
      if entered == "":
        print ("Enter an infix expression: ")
      if entered == "postfix":
        inf = False
      if entered == "stop":
        break
      translated = (s.infixToPostfix(entered))
      if (entered != "postfix"):
        print (s.postEval0(translated))
      else:
        pass
    if inf == False:
      entered = input ("Enter a postfix expression: ")
      if entered == "":
        print ("Enter an infix expression: ")
      if entered == "infix":
        inf = True
      if entered == "stop":
        break
      if (entered != "infix"):
        print (s.postEval0(entered))
      else:
        pass
 
main()