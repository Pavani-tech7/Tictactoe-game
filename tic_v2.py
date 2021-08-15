from random import randrange

def DisplayBoard():
    a=0
    for i in range(3):
        print(("+"+7*"-")*3,"+",sep="",end="\n")
        print(("|"+7*" ")*4)
        print("|"+3*" ",lst[a],3*" "+"|",sep="",end="")
        a+=1
        print(3*" ",lst[a],3*" "+"|",sep="",end="")
        a+=1
        print(3*" ",lst[a],3*" "+"|",sep="")
        a+=1
        print(("|"+7*" ")*4)            
    print(("+"+7*"-")*3,"+",sep="")   

def EnterMove(o):
    if o in lst:
         lst1.remove(o)  
         lst[o-1]='O'
         olst.append(o)
         olst.sort()
         VictoryFor()        
         while True:
             x=randrange(1,10)
             #print(x)
             if x in lst1:
                 lst[x-1]='x'
                 break
             else:
                 x=randrange(1,10)
                 #print(x)
         xlst.append(x)
         xlst.sort()
         lst1.remove(x)        
         DisplayBoard()    
     
    else:
        print("The box is not available.Select from:",lst1)

def VictoryFor():
    while True:
        for i in Olst:
            for j in olst:
                if j in Olst:
                    l.append(j in Olst)            
         #print(all(l))

        

lst=[1,2,3,4,'x',6,7,8,9]
lst1=[1,2,3,4,6,7,8,9]
olst=[]
xlst=[5]
DisplayBoard()
while True:
    if len(lst1)!=0:
        o=int(input("Select your box:"))
        EnterMove(o)
        a=VictoryFor()
        if a==1:
            print("You won")
            break
        elif a==2:
            print("Computer won")
            break
    else:
        print("The Game is drawn")
        break

