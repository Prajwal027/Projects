import random

def getvalue(comp,User):
    if comp==User:
        return None
    elif comp=="S":
        if User=="W":
            return "You Loose"
        elif User=='G':
            return "You Win"
    elif comp=="W":
        if User=="G":
            return "You Loose"
        elif User=="S":
            return "You Win"
    elif comp=="G":
        if User=="S":
            return "You Loose"
        elif User=="W":
            return "You Win"


print("Let the Computer choose:-Snake(S),Water(W),Gun(G) ?")
rand=random.randint(1,2)
 
if rand== 1:
    comp="S"
elif rand==2:
    comp="W"
else:
    comp="G"

#Now Time to user to pick his Symbol
# print("Let You choose:-Snake(S),Water(W),Gun(G) ?")
User=input("Let You choose:-Snake(S),Water(W),Gun(G) ?")
Result=getvalue(comp,User)

if Result == None:
    print("Its a tie, Thank You")
elif Result:
    print(f"Your Result is :{Result}")
else :
    print("No result")


