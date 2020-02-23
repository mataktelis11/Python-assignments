##am:p19100
##aristotelis matakias

#################################






##
##
##
##
##
##
##
##
#####################_MY_CODE_#####################




#
##
###
####
#####
#######NOTICE:THE FILE MUST BE CALLED:file.txt
#####
####
###
##
#















def det_of_2x2(a,b,c,d):
   return a*d-b*c
    




try:








    fin=open("file.txt","r")
    lines=fin.readlines()
    allnumbers=[]

    j=0
    

    for line in lines:
         numbers=line.split(" ")
         

         for x in reversed(numbers):
                
               if ((x=='') or(x=='\n')):
                  numbers.remove(x)
            
         for i in range(len(numbers)):
               try:
                  numbers[i]=int(numbers[i])
               except ValueError:
                    
                  j+=1
                    
         if len(numbers)!=0:           
            allnumbers.append(numbers)
                   
            


    if(j==0):
        print("Array is:")
        print(allnumbers)
        if((len(allnumbers)==3)and (len(allnumbers[0])==3)and (len(allnumbers[1])==3)and (len(allnumbers[2])==3)):
            print("The array is valid")




            print("matrix is: ")
            print("")
            for k in range(3):
                print('|',allnumbers[k][0],allnumbers[k][1],int(allnumbers[k][2]),"|")







            answer1=(allnumbers[0][0])*(det_of_2x2(allnumbers[1][1],allnumbers[1][2],allnumbers[2][1],allnumbers[2][2]))

            answer2=(allnumbers[0][1])*(det_of_2x2(allnumbers[1][0],allnumbers[1][2],allnumbers[2][0],allnumbers[2][2]))

            answer3=(allnumbers[0][2])*(det_of_2x2(allnumbers[1][0],allnumbers[1][1],allnumbers[2][0],allnumbers[2][1]))


            final_answer=answer1-answer2+answer3





            print("The determinant of the matrix is:")
            print(final_answer)
            fin=fin.close()










        else:
            print("The array is invalid: The file must have 3 lines and 3 integers in every line")
            fin=fin.close()        

         

        





    else:
        print("Something went wrong:The file must contain 3 lines and 3 integers in every line and NO letters")
        fin=fin.close()

except FileNotFoundError:
    print("File doesnt exist! Please create a file named file.txt")
