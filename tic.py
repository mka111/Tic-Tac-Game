c=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

d=[]
import random
def check(c):
    if c[0]==c[1]==c[2]==c[3]:
        return True
    
    elif c[4]==c[5]==c[6]==c[7]:
        return True
    
    elif c[8]==c[9]==c[10]==c[11]:
        return True
    
    elif c[12]==c[13]==c[14]==c[15]:
        return True
    
    elif c[0]==c[4]==c[8]==c[12]:
        return True
    
    elif c[1]==c[5]==c[9]==c[13]:
        return True
    
    elif c[2]==c[6]==c[10]==c[14]:
        return True
    
    elif c[3]==c[7]==c[11]==c[15]:
        return True
    
    elif c[0]==c[5]==c[10]==c[15]:
        return True
    
    elif c[3]==c[6]==c[9]==c[12]:
        return True
    
    elif c[1]==c[6]==c[11]:
        return True
    
    elif c[2]==c[5]==c[8]:
        return True
    
    elif c[4]==c[9]==c[14]:
        return True
    
    elif c[7]==c[10]==c[13]:
        return True
    else:
        return False
def p():
    o=random.randint(0,1)
    if o==0:
        return "computer"
    return "user"


print("Lets start the game")



def game(c,d):
    board = (" "+ str(c[0])+"|"+ " " + str(c[1])+ "|"+ " " +  str(c[2])+ "|"+ " " + str(c[3])+" \n" +
            " "+ str(c[4]) + "|" + " "+ str(c[5]) + "|" + " " + str(c[6]) + "|" + " " + str(c[7])+"\n"+
            " "+ str(c[8]) + "|" + str(c[9]) + "|" + str(c[10]) + "|"  + str(c[11])+"\n" +
             str(c[12]) + "|" + str(c[13]) + "|" + str(c[14]) + "|"  + str(c[15]))
    print(board)
    
    
    chance=p()
    print(chance,"will choose first")
    com=random.randint(0,16)
        
    while True:
        if chance=="computer":
           while com  in d:
              com=random.randint(1,16)
           if com not in d:
              
              print("computer chooses",com)
              d.append(com)
              if com>=10:
                 c[com-1]="X"
              else:
                 c[com-1]="X"
              board= (" "+ str(c[0])+"|"+ " " + str(c[1])+ "|"+ " " +  str(c[2])+ "|"+ " " + str(c[3])+" \n" +
                      " "+ str(c[4]) + "|" + " "+ str(c[5]) + "|" + " " + str(c[6]) + "|" + " " + str(c[7])+"\n"+
                      " "+ str(c[8]) + "|" + str(c[9]) + "|" + str(c[10]) + "|"  + str(c[11])+"\n" +
                      str(c[12]) + "|" + str(c[13]) + "|" + str(c[14]) + "|"  + str(c[15]))
              print(board)
              chance="user"
        
           if check(c)==True:
              print("computer is the winner")
              break
           chance="user"
           if len(d)==16:
              print("Its tie. Nobody wins")
              break
        
        if chance=="user":
           user=input("choose ur move now")
   
           
            
        
           while user.isnumeric()==False or (int(user) in d) or int(user)>16 or int(user)<0:
               user=input("choose ur move again")
                 
           user=int(user)
        
           if user not in d:
              d.append(user)
              if user>=10:
                 c[user-1]="O"
              else:
                 c[user-1]="O"
              board= (" "+ str(c[0])+"|"+ " " + str(c[1])+ "|"+ " " +  str(c[2])+ "|"+ " " + str(c[3])+" \n" +
                      " "+ str(c[4]) + "|" + " "+ str(c[5]) + "|" + " " + str(c[6]) + "|" + " " + str(c[7])+"\n"+
                      " "+ str(c[8]) + "|" + str(c[9]) + "|" + str(c[10]) + "|"  + str(c[11])+"\n" +
                      str(c[12]) + "|" + str(c[13]) + "|" + str(c[14]) + "|"  + str(c[15]))
              print(board)
              chance="computer"
           
           if check(c)==True:
              print("user is the winner")
              break
        
           if len(d)==16:
              print("Its tie. Nobody wins")
              break



def playagain():
    n=input("do you want to play again,yes or no?")
    
    while n[0]=="y" or n[0]=="Y":
       print("lets start game again") 
       c=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
       
       d=[]
       game(c,d)
       n=input("do you want to play again,yes or no?")
    print("thankhs for playing")
    
game(c,d)      
playagain()
    
    
    


        







