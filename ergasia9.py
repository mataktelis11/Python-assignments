##python3.8
##am:p19100
##aristotelis matakias

#################################

print("Hellow World")
##
##
##
##
#############_MY_CODE_###############


s=0
while True:
    try:
        a = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

print("Number is:")
print(a)





counter=0




def myFunction(x):
    global counter
    s=0

    print("multiply by 3:")
    x=3*x
   
    print(x)

    print("add 1:")
    x +=1
    print(x)

    print("take the digits:")
    x=str(x)

    list1=list(x)
    if (list1[0]=="-"):
        list1.pop(0)
    
    print(list1)
    print("add them:")
    for i in range(len(list1)):
        b=list1[i]
        b=int(b)
        s +=b
    print(s)
    counter +=1
    return s





while True:
    print("Apply the algorithm")
    a=myFunction(a)
    
    if (a<10):
        print("the answer is:")
        print(a)
        print("completed in ",counter,"step(s)")
        break
    





