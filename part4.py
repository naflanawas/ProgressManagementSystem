
# I declare that my work contains no examples of misconduct, such as plagiarism or collusion.
# Any code taken from sources is referenced within my code solution.

# Student ID : 20220352
# Date :30/11/2022


# Creating variables to count all the  progression outcomes
progress = 0
trailer = 0
retriever = 0
excluded = 0
python_dict={} 
python_list=[]  #to makesure that key value of dictionary is unique


# Creating Function for the validation
def validation(number):
    
    while True:
        try:
            value: int = int(input(number))
            if value % 20 != 0 or value > 120:
                 # Requesting to enter an integer in range 0 to 20 and times of 20
                print("Out of Range")
            else:
                break
        except ValueError:
            print("Integer Required")
    return value #saved the value


while True:
    uowid=(input('Please enter the Student ID: '))
    if uowid in python_list: #condition to check whether the uowid is unique 
        print('Student ID already exists!.please try agian')
        continue
    else:
        python_list.append(uowid)
    # Asking for credits
    c_pass = validation("Please enter your total credits at pass: ")
    c_defer = validation("Please enter your total credits at defer: ")
    c_fail = validation("Please enter your total credits at fail: ")

    # Requesting that the total credits should be 120
    t_credit =c_pass+c_defer+c_fail
    
    if t_credit == 120:
        # Creating conditions for progression outcomes
        if c_pass == 120:
            progression="Progress"
            progress+= 1
            python_dict[uowid]=progression+'-'+str(c_pass)+','+str(c_defer)+','+str(c_fail)
            
        elif c_pass == 100:
            progression="Progress- Module Trailer"
            trailer += 1
            python_dict[uowid]=progression+'-'+str(c_pass)+','+str(c_defer)+','+str(c_fail)
            
        elif c_pass < 100 and c_fail <= 60:
            progression="Do not Progress - Module Retriever"
            retriever+=1
            python_dict[uowid]=progression+'-'+str(c_pass)+','+str(c_defer)+','+str(c_fail)
        else:
            progression="Exclude"
            excluded += 1
            python_dict[uowid]=progression+'-'+str(c_pass)+','+str(c_defer)+','+str(c_fail)
    else:
        print("Total Incorrect")


   # Asking whether to continue or quit
    while True:
         valid = input("Would you like enter another set of data? Enter (y) for yes or (q) to quit and view results: ")
         valid=valid.lower()
         if valid=='y':
             break
         elif valid=='q':
             print('part 4:')
             for (keys,values)in python_dict.items():
                 print(keys+' '+':'+' '+values,end='  ')
             break #to stop the loop
         else:
             print('invalid!please try again')
        
        
        



    
        

        






    


   






   
     



     















