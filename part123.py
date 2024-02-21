
# I declare that my work contains no examples of misconduct, such as plagiarism or collusion.
# Any code taken from sources is referenced within my code solution.

# Student ID : 20220352
# Date :25/11/2022

# Creating variables to count all the  progression outcomes
progress = 0
trailer = 0
retriever = 0
excluded = 0
#emptylist
progress_list=[]
trailer_list=[]
retriever_list=[]
excluded_list=[]
condition = True
#create a text file and open it
data_file=open('py_datafile','w')

# Creating Function for the validation
def validation(number):
    while True:
        try:
            value= int(input(number))
            if value % 20 != 0 or value > 120:
                 # Requesting to enter an integer in range 0 to 20 and times of 20
                print("Out of Range")
            else:
                break
        except ValueError:
            print("Integer Required")
    return value #save the value

while condition == True:
    # Asking for credits
    c_pass = validation("Please enter your total credits at pass: ")
    c_defer = validation("Please enter your total credits at defer: ")
    c_fail = validation("Please enter your total credits at fail: ")

    # Requesting that the total credits should be 120
    t_credit =c_pass+c_defer+c_fail
    if t_credit == 120:
        # Creating conditions for progression outcomes
        if c_pass == 120:
            print("Progress")
            progress+= 1
            progress_list.append([c_pass,c_defer,c_fail])
        elif c_pass == 100:
            print("Progress( Module Trailer)")
            trailer += 1
            trailer_list.append([c_pass,c_defer,c_fail])
        elif c_pass < 100 and c_fail <= 60:
            print("Do not Progress - Module Retriever")
            retriever+=1
            retriever_list.append([c_pass,c_defer,c_fail])
        else:
            print("Exclude")
            excluded += 1
            excluded_list.append([c_pass,c_defer,c_fail])
    else:
        print("Total Incorrect")
        


    # Asking whether to continue or quit
    while True:
        valid = input("Would you like enter another set of data? Enter (y) for yes or (q) to quit and view results: ")
        valid=valid.lower()
        if valid=='y':
            break
        elif valid=='q':
        #part1D
            # Creating a horizontal Histogram
                print("--------------------------------------------------------------------------------------------")
                print("Histogram")
            # counting all the progression outcomes
                count = progress + trailer + retriever + excluded

            # Printing starts and progression count
                print("Progress ", progress, ":", "*" * progress)
                print("Trailer ", trailer, "    :", "*" * trailer)
                print("Retriever ", retriever, ":", "*" * retriever)
                print("Exclude ", excluded, "  :", "*" * excluded)

            # Printing the total count of progression
                print(count, "Outcomes in total")
                print("--------------------------------------------------------------------------------------------")
                #part2
                print('part 2:')
                for item in (progress_list):
                 #https://www.pythonpool.com/remove-brackets-from-list-python/
                    print('progress','-',str(item)[1:-1])
                for item in (trailer_list):
                    print('Progress- Module Trailer','-',str(item)[1:-1])
                for item in (retriever_list):
                    print('Do not Progress - Module Retriever','-',str(item)[1:-1])
                for item in (excluded_list):
                    print('exclude','-',str(item)[1:-1])
                


                #part3
                print("\n--------------------------------------------------------------------------------------------")
                print('\npart 3:')
                #access the text file to store the values
                for item in (progress_list):
                    w_progress=('Progress'+'-'+str(item)[1:-1])
                    data_file.write(w_progress)
                for item in (trailer_list):
                    w_trailer=('\nProgress- Module Trailer'+'-'+str(item)[1:-1])
                    data_file.write(w_trailer)
                for item in (retriever_list):
                    w_retriever=('\nDo not Progress - Module Retriever'+'-'+str(item)[1:-1])
                    data_file.write(w_retriever)
                for item in (excluded_list):
                    w_excluded=('\nExclude'+'-'+str(item)[1:-1])
                    data_file.write(w_excluded )
                data_file.close()   #close the text file


                #open the text file to print the output
                data_file=open('py_datafile','r')
                print(data_file.read())
                print("\n--------------------------------------------------------------------------------------------")
                data_file.close()#close the text file
                condition = False
                break
        else:
            print('invalid!please try again')
        
        
        

   




