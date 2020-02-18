print("Hellow World")

##
##
##
##
##
##


################_MY_CODE_####################


def digitAdder(number):
    finalnumber=0
    number=str(number)
    listOfNumber=list(number)
    for j in range(len(listOfNumber)):
        temp=listOfNumber[j]
        temp=int(temp)
        finalnumber +=temp
    return finalnumber








print("give a 16-digit number OR a 15-digit number")



while True:
    try:
        thecard = int(input("Please enter a number: "))
        thecard =str(thecard)
        if(len(thecard)==16):
           break
        elif(len(thecard)==15):
           break
        else:
            continue


        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    
   
        

print(thecard)


def Luhn_algorithm(card):

    basic_card=list(card)

    product_card=[]
    print(basic_card)

    for i in range(len(basic_card)):
        if ((i % 2)==0):
            c=basic_card[i]
            c=int(c)
            c=2*c
            if (c>=10):
                c=digitAdder(c)



            product_card.append(c)
        else:
            product_card.append(basic_card[i])
    print(product_card)


    string_card=""

    for z in range(len(product_card)):
        product_card[z]=str(product_card[z])
        string_card +=product_card[z]

    print(string_card)

    card_result=digitAdder(string_card)
    print (card_result)





    if (len(basic_card)==16):

    
        if (card_result % 10 ==0):
            print("this is a valid card number")
        else:
            print("this is NOT a valid card number")

    else:

        for t in range(10):
            if((card_result+t)%10==0):
                break
        print("last number must be")
        print(t)

    return 0

Luhn_algorithm(thecard)

