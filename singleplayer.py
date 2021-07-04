#snake and ladder
print("######### SNAKE AND LADDER ###########")
print("      single player    ")
n= input(" ###### enter player name ######")
position=0
player=[0]
i=0
while (player[0]!=30):
    print(n,  i+1, "turn")
    a=int(input("roll a die"))
    
    if(a==1):
        
        
        position+=a
        player[i]=position
        print("you are at position  :", position)
        
        
    elif(a==2):
        
        position+=a
        player[i]=position
        print("you are at  position  :", position)
    elif(a==3):
        
        position+=a
        player[i]=position
        print("you are at position  :", position)
    elif(a==4):
    
        position+=a
        player[i]=position
        print("you are at  position  :", position)
    elif(a==5):
        
        position+=a
        player[i]=position
        print("you are at  position :", position)
    elif(a==6):
        
        position+=a
        player[i]=position
        print("you are at position :", position)
    
    if( position==9 or position==19):
        print("**************>>>")
        print("------------------->>>")
        print("oops you are caught by snake and positon decrements from ", position)
        position=2
        print("now you are at :",position)
    elif( position==12 or position==17):
         print("/------/")
         print("/------/")
         print("/------/")
         print("/------/")
         print("WOW you got to climb a ladder and your poition increments  from  position ", position)
         position=28
         print("now you are at :",position)

if(player[0]==30):
    print("###### YOU WON  #######" , n)

    
    
