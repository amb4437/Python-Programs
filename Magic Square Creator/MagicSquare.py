#  File: MagicSquare.py

#  Description: This program creates a magic square

#  Student Name: Andrew Baldwin

#  Student UT EID: Amb4437

#  Course Name: CS 313E

#  Unique Number: 53330

#  Date Created: 02/01/2011

#  Date Last Modified: 02/04/2010



def makeSquare(n):

  square = [ [ 0 for c in xrange(n) ] for r in xrange(n) ]

  ### Place one in the bottom middle
  col = n / 2
  row = n-1
  square[row][col] = 1

  ## define some variables:
  last = n -1
  num = 2
  row = 0
  col = col + 1
  r = (n **2) - 1

  ## Add more numbers to the square
  for i in range(r):
    if row > last:
      row = 0
    if col > last:
      col = 0
    if (square[row][col] > 0):
      row = row - 2
      col = col - 1
    square[row][col] = num
    
    num = num + 1
    row = row + 1
    col = col + 1
  
  return square


def printSquare (square, n, correctsum):

  print ('Here is a %d x %d magic square' % (n, n))
  for element in square:
    print element
  print 'Sum of rows = %s' % (correctsum)
  print 'Sum of columns = %s' % (correctsum)
  print 'Sum diagonal (UL to LR) = %s' % (correctsum)
  print 'Sum diagonal (UR to LL) = %s' % (correctsum)
  
  
  

def checkSquare (n, square):

  ## define correct sum
  correctsum= n * (n ** 2 + 1) / 2
  condition = True
  

  ## check sum of rows
  sum = 0
  for row in range(len(square)):
    for col in range(len(square)):
      sum = sum + square[row][col]
    if sum == correctsum:
      condition = True
    else:
      condition = False

  ## check sum of columns
  sum = 0
  for col in range(len(square)):
    for row in range(len(square)):
      sum = sum + square[row][col]
    if sum == correctsum:
      condition = True
    else:
      condition = False
    sum = 0

  ## Check sum of first diagonal
  sum = 0
  for col in range(len(square)):
    sum = sum + square[col][col]
  if sum == correctsum:
    condition = True
  else:
    condition = False
  sum = 0

  ## Check sum of second diagonal
  sum = 0
  r = len(square) -1
  for col in range(len(square)):
    sum = sum + square[col][r-col]
  if sum == correctsum:
    condition = True
  else:
    condition = False
  sum = 0
  return correctsum


def main():

  n = input ("Please enter an odd number greater than 1: ")
  while (n % 2 != 1 or n <3):
    n = input("Please enter an odd number greater than 1: ")
  square= makeSquare(n)
  correctsum= checkSquare(n, square)
  printSquare(square, n, correctsum)
main()