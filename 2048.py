import os
import random

m = [[ "" for i in range(4)] for j in range(4)]

def pgrd(m):
    print ",-----.-----.-----.-----."
    for i in range(4):
        print "|%5s|%5s|%5s|%5s|"%(str(m[i][0]),str(m[i][1]),str(m[i][2]),str(m[i][3]))
        print "'-----'-----'-----'-----'"

def move_column(m,col,direction = "up"):
   if(direction == "up"):
      start = 0
      end = 4
      increment = 1
      print "up"
      
   elif (direction == "down"):
      start = 4 
      end = 0
      increment = -1
    
   for row in range (start,end):
      if(m[row][col] == ""):
         for i in range(row,end,increment):
            if(m[i][col] != ""):
               m[row][col] = m[i][col]
               m[i][col] = ""
   
    
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
            row = 0
            while(row < 4):
               merge = False
               if(m[row][col] != ""):
                  i = row+1
                  while(i < 4):
                     if(m[i][col] != ""):
                        if(m[row][col] == m[i][col]):
                           m[row][col] *= 2
                           m[i][col] = ""
                           merged = True
                           i += 2
                        break
                     i += 1 
               if(merge):
                  row = i + 1
               else:
                  row += 1
            move_column(m,col,"up")   

    elif act == '2':
        for k in range(3):
            rg = (7-k )%4
            for i in range(rg):
                for j in range(4):
                    rw = i
                    cl = j

                    dt = m[rw][cl]

                    if m[rw+1][cl] == "":
                        m[rw+1][cl] = m[rw][cl]
                        m[rw][cl] = ""
                    elif m[rw+1][cl] == dt:
                        m[rw+1][cl] = dt * 2
                        m[rw][cl] = ""
                    else:
                        pass
    elif act == '4':
        for k in range(3):
            rg = (7-k )%4
            for i in range(4):
                for j in range(rg):
                    rw = i
                    cl =(j + 5 )%4 

                    dt = m[rw][cl]

                    if m[rw][cl-1] == "":
                        m[rw][cl-1] = m[rw][cl]
                        m[rw][cl] = ""
                    elif m[rw][cl-1] == dt:
                        m[rw][cl-1] = dt * 2
                        m[rw][cl] = ""
                    else:
                        pass
    elif act == '6':
        for k in range(3):
            rg = (7-k )%4
            for i in range(4):
                for j in range(rg):
                    rw = i
                    cl = j 

                    dt = m[rw][cl]

                    if m[rw][cl+1] == "":
                        m[rw][cl+1] = m[rw][cl]
                        m[rw][cl] = ""
                    elif m[rw][cl+1] == dt:
                        m[rw][cl+1] = dt * 2
                        m[rw][cl] = ""
                    else:
                        pass
    else:
        pass

    ls = []

    for i in range(4):
        for j in range(4):
            if m[i][j] == "":
                #print "blank %d" % ((i * 4) + j)
                ls.append((i * 4) + j)
        
    a = random.choice(ls)    

    arw = a/4
    acl = a%4

    m[arw][acl] = 2
    
    pgrd(m)
    

