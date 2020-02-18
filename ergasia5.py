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
#######NOTICE:THE FILE MUST BE CALLED:new.txt
#####
####
###
##
#




print("--->(Try to)Open file with name: new.txt and read it")
while True:
    try:

        f = open("new.txt", "r")
        textall=f.read()


        if(textall==""):
            print("OH NO:The file is EMPTY!!Please use a non emplty file!")
        else:
            print("--->Print file new.txt")
            print("")
            print(textall)
            print("")
            print("--->Apply the algorithm")
            print("")
            
        f.close() 

        fin = open("new.txt", "r")
        lines=fin.readlines()

        for line in lines:
            text=line
            mylist=text.split(" ")
            ##print(mylist)
            for i in range (len(mylist)):
                temp=mylist[i]
                temp=list(temp)
                temp69=""
                temp70=""

                if (len(temp)>=3):
                    if ((temp[0]==",")or(temp[0]==".")or(temp[0]=="?")or(temp[0]=="!")or(temp[0]=="(")or(temp[0]=="'")or(temp[0]=="\n")):
                        temp69=temp[0]
                        temp.pop(0)
                        ##print(temp)
                        mylist[i]=temp
                
                    if ((temp[-1]==",")or(temp[-1]==".")or(temp[-1]=="?")or(temp[-1]=="!")or(temp[-1]==")")or(temp[-1]=="'")or(temp[-1]=="\n")):
                        temp70=temp[-1]
                        temp.pop(-1)
                        ##print(temp)
                        mylist[i]=temp

                retake=""
                for j in range (len(temp)):
                    retake += temp[j]
                       
                mylist[i]=retake
                
             ##using_built_in_function_isalpha_that_returns_'True'_only_if_the_str_is_only_made_of_letters
                if ((mylist[i].isalpha()) == True):
                        
                        ##print("ok")

                    ##turn_the_[i]_element_of_the_list_into_an_array
                        temp_list=list(mylist[i])
                        ##print(temp_list)
                        ##print(temp_list)

                        ##check_if_the_array_has_more_than_3_letters
                        if (len(temp_list)>3):
                            ##print("target")

                                ##take_the_first_letter
                                    
                            temp67=temp_list[0]

                                ##pop_it_out

                            temp_list.pop(0)

                                ##append_it

                            temp_list.append(temp67)

                                ##append_'ay'

                            temp_list.append("ay")


                                ##print(temp_list)

                                ##now_we_have_to_turn_the_result_into_a_str_and_place_it_in_the_list


                                ##create_empty_str
                                    
                            convert_into_string=""

                                ##simply_add_all_the_elements
                            for j in range (len(temp_list)):
                                convert_into_string +=temp_list[j]
                                    ##print(convert_into_string)

                                    ##put_the_string_in_the_same_place_of_the_uneddited_words

                                mylist[i]=convert_into_string
                                    
                        else:
                            continue

                                                      
                    

                mylist[i]=temp69+mylist[i]
                mylist[i]=mylist[i]+temp70
            ##print("--->Print the final resutl")
            print("")
            for z in range(len(mylist)): 
                print (mylist[z],end = ' ')



               
        fin.close()


            



        break       
    except FileNotFoundError: 
  
        print("No such file exsists.  Try again...")
        break
