#Hello this is my secret language code 
#rule
'''In the sentences make odd indexes at first then even indexes
also put last letter of the word to 1st and add 2 random letters at the start and end of the word'''

def EnCode():
    import random
    Oddl,Evenl=[],[]
    alphabeds=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    Message=input("Enter the message:")
    l=Message.split()

    for i in range(len(l)):
        l[i]=f"{alphabeds[random.randint(0,25)]}"+f"{alphabeds[random.randint(0,25)]}"+l[i][-1]+l[i][:-1]+f"{alphabeds[random.randint(0,25)]}"+f"{alphabeds[random.randint(0,25)]}"
        if (i+1)%2!=0 :
            Oddl.append(l[i])
        else:
            Evenl.append(l[i])

    print("Your Encoded message is:")
    for j in Oddl:
        print(j,end=' ')
    for k in Evenl:
        print(k,end=' ')



def Decode():
    message=input("Enter message to decode:")
    Evenl,Oddl=[],[]
    l=message.split()
    for i in range(len(l)):
        l[i]=l[i][3:-2]+l[i][2]
    

    if len(l)%2==0:
        h=len(l)//2
        for i in range(len(l)):
            b=h+i
            if i>((len(l)//2)-1):
                break
            print(l[i],end=' ')
            if b!=len(l):
                print(l[b],end=' ')

    else:
        h=len(l)//2+1
        for i in range(len(l)):
            b=h+i
            if i>len(l)//2 :
                break
            print(l[i],end=' ')
            if b!=len(l):
                print(l[b],end=' ')
            
            


op=input("If you want to encode enter e \n If you want to decode enter d :")
if op=='e':
    EnCode()
elif op=='d':
    Decode()
else:
    raise TypeError("Enter 'e' or 'd' only!")

    
  