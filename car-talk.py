##########################
# Name: Lucas Liu
# UNI: yl3433
#
# Files contain a function that yiled the solution to problem 2
##########################################################

# number = ab----
# first mile: a-----
# second mile:a----f
# third mile:------
def car_talk(x):    
    '''This function is to find the exact number that fits the requirements of problem 2'''

    for num in range(0,x):
        # Format the number into a 6-digit string     
        number = "0" * (6 - len(str(num))) + str(num)
        
        # Check if only the last 4 digits of the number consititute a palindrome
        # If so, check number + 1
        if number[2] == number[-1] and number[3] == number[-2]\
           and number[1] != number[-1]:   
                    
              number_plus1 = "0" * (6-len(str(num + 1))) + str(num + 1)
            
              # Check if the last 5 digits of the number_plus1 constitute  a palindrome
              # If so, check number + 2
              if number_plus1[1] == number_plus1[-1] and number_plus1[2] == number_plus1[-2]:
                
                  number_plus2 = "0" * (6-len(str(num + 2))) + str(num + 2)
                
                  # Check if the middle 4 digits of the number_plus2 constitute  a palindrome
                  # If so, check number + 3
                  if number_plus2[1] == number_plus2[-2] and number_plus2[2] == number_plus2[-3]:

                    number_plus3 = "0"*(6-len(str(num + 3))) + str(num + 3)
                    
                    # Check if the number_plus3 is a palindrome
                    
                    if  number_plus3[0] == number_plus3[-1] and  number_plus3[1] ==  number_plus3[-2]\
                        and number_plus3[2] ==  number_plus3[-3]:
                        
                        # print the original number to the console
                        print (num)

   

car_talk(999999)
                
            