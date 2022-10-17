import random
#This is a game of Gussing the Correct Number
def getresult(no,randno):
    if no==randno:
        return True
    elif randno>no:
        return "Enter Greater than this "
    elif randno<no:
        return "Enter Lower than this"
    else:
        print("Error")
randno=random.randint(1,10)
print(randno)
no=int(input("Guss the Number:"))
H=getresult(no,int(randno))
count=0
while True:
    if H==True:
        print(f"Gussed correct with {count} Attempt ")
        exit()
    else:
        print(H)
        no=int(input("Guss the number again:"))
        count+=1
        print(count)
        H=getresult(no,randno)


