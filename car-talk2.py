##########################
# Name: Lucas Liu
# UNI: yl3433
#
# Files contain a function that checks if a number is a palindrome
# And a car_talk solution that utilizes such function
##########################################################

def palindrome(num_str):
    '''Return True if the num_str is a palindrome'''
    num_list = list(num_str)
    num_list_reversed = num_list[::-1]
    
    #if num_str is a palindrome, then its reversal equals to itself.
    return (num_list == num_list_reversed)
    

def car_talk(max_mileage):
    '''This function is to find the exact number that fits the requirements of problem 2'''
    for num in range(0, max_mileage):
        # Format the number into a 6-digit string     
        mileage = "0" * (6 - len(str(num))) + str(num)
        
        # Check if only the last 4 digits of the number consititute a palindrome
        # If so, increment number by 1
        if palindrome(mileage[-4:]) and not palindrome(mileage[-5:]):
            mileage_plus1 = "0" * (6 - len(str(num+1))) + str(num+1)
            
            # Check if the last 5 digits of the number_plus1 constitute  a palindrome
            # If so, increment number by 2
            if palindrome(mileage_plus1[-5:]):
                mileage_plus2 = "0" * (6 - len(str(num+2))) + str(num+2)
                # Check if the middle 4 digits of the number_plus2 constitute  a palindrome
                # If so, increment number by 3
                
                if palindrome(mileage_plus2[-5:-1]):
                    mileage_plus3 = "0" * (6 - len(str(num+3))) + str(num+3)
                    
                    # Check if the number_plus3 is a palindrome
                    if palindrome(mileage_plus3):
                        print (num)
            
def main():
    car_talk(999999)
    

main()