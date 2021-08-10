import math
A=raw_input("enter name of player 1..")
C=raw_input("enter name of player 2..")
score=0
score2=0
s=2
print ("'s turn")
print ("chance 1."),
a=input("enter your guess..")
import random
b=random.randint(1,100)
while a!=b:
  if a>b:
    print ("your guess is higher then the number.......")
    print ("chance ") , s,
    a=input("enter another")
    s=s+1
  elif  a<b:
    print ("your guess is lower then the number.......")
    print ("chance") , s,
    a=input("enter another")
    s=s+1
  elif  a==b:
    print ("absolutely ..............correct")
    break
print ("you have taken " ,  s-1  ," chance and the random number is......................................." , b)

print ("now its ",C,"'s turn")
print ("To win you have to guess in " ,s-2 ,"turns")
s2=2
print ("chance 1.")
a=input("enter your guess..")
import random
b=random.randint(1,100)
while a!=b:
  if a>b:
    print ("your guess is higher then the number.......")
    print ("chance ")
    print(s2)
    a=input("enter another")
    s2=s2+1
  elif  a<b:
    print ("your guess is lower then the number.......")
    print ("chance" , s2)
    a=input("enter another")
    s2=s2+1
  elif  a==b:
    print ("absolutely ..............correct")
    break
print ("you have taken " ,  s2-1  ," chance and the random number is......................................." , b)
x=0
x2=0

if s2-1>s-1:
  x=x+1
  print ("                                          ",A," win..")
  print ("""                                 ....score card..""")
  print  ("                                        ")
  print (A)
  print("  : ") 
  print (x) 
  print ("                                        ",C,":  " , x2 )
elif s2-1<s-1:
  x2=x2+1
  print ("                                         ",C,"win")
  print ("                                         score card...")
  print  ("                                        ",A, " : " ,x)
  print ("                                         ",C, ": "  ,x2)

else:
  print ("match draw.......")
  print("                                        ",A,"  : " ,x)
  print ("                                         ",C,": " ,   x2)
print ("_________________________________________________________________________________________")


#LEVEL 2
#level 2
#guessing game one on one
print("you have 3 chances . ")
import random
b=random.randint(0,10)
for i in range(3):
  print (A) 
  a=input("enter a guess.....")
  print (C) 
  c=input("ENTER YOUR GUESS......")
  if i==0 or i==1:
    if a>b and c>b:
      print (A) 
      print("your guess is  HIGHER than the number")
      print (C ,"your guess is  HIGHER than the number")
    elif a<b and c<b:
      print (A ,"your guess is  LOWER than the number")
      print (C ,"your guess is  LOWER than the number")
    elif a>b and c<b:
      print (A ,   "your guess is  HIGHER than the number")
      print (C , "your guess is  LOWER than the number")
    elif a<b and c>b:
      print (A ,"your guess is  LOWER than the number")
      print (C ,"your guess is  LOWER than the number")
    elif a==b and c!=b:
      x=x+1
      print  (A ," wins")
      print ("random number is .. " , b)
      print ("""                                                score card..""")
      print  ("                                        player 1  : " ,A,":", x )
      print ("                                         player 2 :  " , C,":",x2) 
      
      break
    elif c==b and a!=b:
      x2=x2+1
      print  (C , "wins")
      print ("random number is .. " , b)
      print ("""score card..""")
      print ( "           player 1  : " ,A,":" ,x )
      print ("                                         player 2 :  " , C,":" ,x2 )
      break
    elif a==b and c==b:
      print ("game  draw ...................")
      print ("random number is .. " , b)
      print ("""score card..""")
      print  ("                                        player 1  : " ,A,":" ,x )
      print ("                                         player 2 :  " , C,":" ,x2) 
      break
  elif i==2 :
     if a!=b and c!=b:
       print ("MATCH DRAW>>>> BOTH ARE WRONG.......")
       print (" random number is ",b)
       print ("score card")
       print (A,":",x)
       print (C,":",x2)

#level 3
print ("now you both are playing for different random numbers but will play simuntaneously..")

print ("you have 3 chances . ")
import random
b=random.randint(0,10)
B=random.randint(1,10)
for i in range(3):
  print (A)
  a=input("enter a guess.....")
  print (C)
  c=input("ENTER YOUR GUESS......")
  if i==0 or i==1:
    if a>b and c>B:
      print (A ,"your guess is  HIGHER than the number")
      print (C ,"your guess is  HIGHER than the number")
    elif a<b and c<B:
      print (A ,"your guess is  LOWER than the number")
      print (C ,"your guess is  LOWER than the number")
    elif a>b and c<B:
      print (A ,   "your guess is  HIGHER than the number")
      print (C , "your guess is  LOWER than the number")
    elif a<b and c>B:
      print (A ,"your guess is  LOWER than the number")
      print (C ,"your guess is HIGHER than the number")
    elif a==b and c!=B:
      x=x+1
      print  (A ," wins")
      print ("you random number is .. " , b)
      print (C,"your random number is..",B)
      print ("""                                                score card..""")
      print  ("                                        player 1  : " ,A,":", x )
      print ("                                         player 2 :  " , C,":",x2 )
      
      break
    elif c==B and a!=b:
      x2=x2+1
      print  (C , "wins")
      print ("your random number is .. " , B)
      print (A,"your random was..",b)
      print ("""score card..""")
      print  ("                                        player 1  : " ,A,":" ,x )
      print ("                                         player 2 :  " , C,":" ,x2) 
      break
    elif a==b and c==B:
      print ("game  draw ...................")
      print ("random number of  .. ",A ,"is", b)
      print ("random number of ",C,"",B)
      print ("""score card..""")
      print  ("                                        player 1  : " ,A,":" ,x )
      print ("                                         player 2 :  " , C,":" ,x2)
      break
  elif i==2:
      if a!=b and c!=B:
        print (A,"your random number is",b)
        print (C,"your random number is",B)
        print ("MATCH DRAW>>>")
        print (A,":",x)
        print (C,":",x2)


