##############################################################
# Name:Yuxuan Liu
# UNI: yl3433

# File contains function that compute the age in terms of days
##############################################################

from datetime import date

#Get user's birthday
user_bir_year = int(input("What was the year you were born?"))
user_bir_month = int(input("What was the month you were born?"))
user_bir_day = int(input("What was the day you were born?"))
user_birthdate = date(user_bir_year, user_bir_month, user_bir_day)

#Get today's date
today = date.today()


#dealta = today - user_birthday
#dealta has an attribute named .days

def count_days():
    """Calculate the number of days from birthdate to today""" 
    return (today - user_birthdate).days
    
#Print out the user's age in terms of days
print ()
print ("Python says you are",count_days(),"days old.")
