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
#######NOTICE:THE FILE MUST BE CALLED:new.txt
#####
####
###
##
#


###FUNCTIONS###

def function_list_into_str(somelist):
    

    convert_into_string=""

    for k in range (len(somelist)):
        convert_into_string+=somelist[k]

        
    return convert_into_string

def function_edit_word(somewordlist):
    var1=somewordlist[0]+"ay"
    somewordlist.pop(0)
    somewordlist.append(var1)

    return somewordlist




all_edited_words=[]

print("--->(Try to)Open file with name: 'new.txt' and read it")
try:

    f = open("new.txt", "r")
    textarea=f.read()

    if(textarea==""):
        print("OH NO:The file is EMPTY!!Please use a non emplty file!")
    else:
        print("--->Print file new.txt")
        print("")

        print(textarea)

        print("")
        print("--->This is the file new.txt with the demanded changes:")
        print("")




        listtext=list(textarea)

        #print(listtext)
        word=[]
        for i in range (len(listtext)):
            if ((listtext[i].isalpha()) == True):
                word.append(listtext[i])
                
            else:
                
                #print(word)
                if (len(word)>3):
                    
                    temp=listtext[i-len(word)]
                    for j in range(len(word)-1):
                        listtext[i-len(word)+j]=listtext[i-len(word)+j+1]
                    temp+="ay"
                    listtext[i-1]=temp

                    nonedited=function_list_into_str(word)

                    edited=function_edit_word(word)
                    edited=function_list_into_str(edited)

                    final=nonedited+" --> "+edited

                    all_edited_words.append(final)
                    
                word=[]

            if (i==(len(listtext)-1)):
                if (len(word)>3):
                    
                    temp=listtext[i-len(word)+1]
                 

                    

                    for j in range(len(word)-1):
                        listtext[i-len(word)+j+1]=listtext[i-len(word)+j+2]
                    temp+="ay"
                    listtext[i]=temp

                    nonedited=function_list_into_str(word)
                    edited=function_edit_word(word)
                    edited=function_list_into_str(edited)

                    final=nonedited+" --> "+edited

                    all_edited_words.append(final)
                    








                word=[]
           



        ##print(listtext)


        print(function_list_into_str(listtext))

        print("")
        print("Here are the changes listed:")
 
        print("")
        

        for i in range(len(all_edited_words)):
            print(all_edited_words[i])
      

    f.close()

except FileNotFoundError: 
  
        print("No such file exsists. Please create a file named: new.txt and try again")
        

