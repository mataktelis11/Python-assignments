##python3.8
##am:p19100
##aristotelis matakias

#################################





print("Hellow World")
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

    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)
       
    return a*d-b*c
    




while True:

    try:


        all_numbers=[]

        fin=open("file.txt","r")

        lines=fin.readlines()

        if(len(lines)==3):

            
            for line in lines:
                ##print(line)

                numbers=line.split(" ")
                

                all_numbers.append(numbers)

                
            if (len(numbers)==3): 
                fin=fin.close()


                print (all_numbers)

                





                answer1=(int(all_numbers[0][0]))*(det_of_2x2(all_numbers[1][1],all_numbers[1][2],all_numbers[2][1],all_numbers[2][2]))

                answer2=(int(all_numbers[0][1]))*(det_of_2x2(all_numbers[1][0],all_numbers[1][2],all_numbers[2][0],all_numbers[2][2]))

                answer3=(int(all_numbers[0][2]))*(det_of_2x2(all_numbers[1][0],all_numbers[1][1],all_numbers[2][0],all_numbers[2][1]))


                final_answer=answer1-answer2+answer3

                ##print(answer1)
                ##print(answer2)
                ##print(answer3)

                print("matrix is: ")
                print("")
                for z in range(3):
                    print('|',all_numbers[z][0],all_numbers[z][1],int(all_numbers[z][2]),"|")
               



                print("det is: ")
                print(final_answer)
            else:
                fin=fin.close()
                print("Invalid format:each line must contain exactly 3 integers")

        else:
            print("Invalid format:file must contain exactly 3 lines")
        
        break


    except FileNotFoundError:
        print("No such file exsists.  Try again...")
        break
    except ValueError:
        print("The file must only contain 9 integers")
        break



