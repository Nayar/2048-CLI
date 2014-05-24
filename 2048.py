import os
import random

m = [[ "" for i in range(4)] for j in range(4)]

def pgrd(m):
    print ",-----.-----.-----.-----."
    for i in range(4):
        print "|%5s|%5s|%5s|%5s|"%(str(m[i][0]),str(m[i][1]),str(m[i][2]),str(m[i][3]))
        print "'-----'-----'-----'-----'"

def move_column(m,col,direction):
   if(direction == "up"):
      start = 0
      end = 3
      increment = 1
      print "up"
      
   elif (direction == "down"):
      start = 3 
      end = 0
      increment = -1
      print "up"
    
   for row in range(start,end+increment,increment):
      if(m[row][col] == ""):
         for i in range(row,end+increment,increment):
            if(m[i][col] != ""):
               m[row][col] = m[i][col]
               m[i][col] = ""
               break
   
def add_column(m,col,direction = "up"):
   if(direction == "up"):
      start = 0
      increment = 1
      print "up"
      
   elif (direction == "down"):
      start = 3
      increment = -1
      
   row = start
   while(row <= 3 and direction == "up" or row >= 0 and direction == "down"):
      merge = False
      if(m[row][col] != ""):
         i = row + increment
         while(i <= 3 and direction == "up" or i >= 0 and direction == "down"):
            print "r %d c %d" % (i,col)
            if(m[i][col] != ""):
               if(m[row][col] == m[i][col]):
                  m[row][col] *= 2
                  m[i][col] = ""
                  merged = True
                  i = i + 2 * increment
               #break
            i += increment
      if(merge):
         row = i + increment
      else:
         row += increment
    
ls = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

a = random.choice(ls)
ls.remove(a)
b = random.choice(ls)
ls.remove(b)

arw = a/4
acl = a%4

brw = b/4
bcl = b%4

m[arw][acl] = 2
m[brw][bcl] = 2
pgrd(m)
        
while True:

    act = raw_input("action num pad key : ")

    if act == '8':
        for col in range(4):
            add_column(m,col,"up")
            move_column(m,col,"up")   

    elif act == '2':
        for col in range(4):
            add_column(m,col,"down")
            move_column(m,col,"down") 
    
    else:
        pass

    ls = []

    for i in range(4):
        for j in range(4):
            if m[i][j] == "":
                #print "blank %d" % ((i * 4) + j)
                ls.append((i * 4) + j)
        
    if(len(ls) == 0):
       print "lose!!!!!!!!!!!!!!!"
       break
    
    a = random.choice(ls)

    arw = a/4
    acl = a%4

    m[arw][acl] = 2
    
    pgrd(m)
    

