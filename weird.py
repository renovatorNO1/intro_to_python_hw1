##################
# Name: Lucas Liu
# UNI: yl3433
##################

#Initialize global variable
yes_or_no = 'y'

#Initialize helper function
def find_product(A,B):
    '''this function is to find the product of A and B, and ask the use
       whether they want to continue'''
       
    global yes_or_no
    number_A = A
    number_B = B 
 
    # The following code blocks are implementation
    # of the weird process of calculating a product   
    sum = 0
    while B != 0:
        if B % 2 == 1:
            sum += A
            A *= 2
            B = B // 2
        else:
            A *= 2
            B = B // 2
    print ("The product of {} and {} is: {}".format(number_A, number_B, sum))
    print ()
    
    # Ask the user if he or she wants to continue 
    # And store the answer into yes_or_no
    print ('If you want to calculate another product, Please enter "y"')        
    print ('If you want to quit, please enter "n"')
    print ()
    yes_or_no = input("What's your decision?")

    
    

    ''' This functio is to ask the user for number A and B and initialize the function'''
        
def start():
    ''' This functio is to ask the user for number A and B and initialize the function'''
    
    while yes_or_no != 'n':
        global yes_or_no
        # Ask the user for number A and B then execute the function find_product             
        if yes_or_no == 'y':
            print ("let's do some multiplication!")
            A = int(input("Please enter the first number"))
            B = int(input("Please enter the second number"))
            print ()
            find_product(A,B)
            
        # If the user input is other than 'y' and 'n', ask them for correct inputs
        else:
            print ('Please enter "y" or "n".')
            yes_or_no = input("What's your decision?")
            
    print ("Goodbye!")


start()


