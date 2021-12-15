"""
    * Author - Nitin Chandrakant Babar
    * Date -  14-12-2021
    * Time -  9.30pm
    * Title - Leap Year 
"""

try:
    year= int(input("Enter a year:"))
        
    if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print("is a leap year".format(year))
                else:
                    print("is not a leap year".format(year))
            else:
                print("is a leap year".format(year))
    else:
        print("is not a leap year".format(year))
except Exception as e:
    print("Enter Correct Value:" ,e)  


try:
    def is_leap(year):
    
        year = int(input("Enter year:"))
        return year%4 ==0 and (year%100 != 0 or year%400==0)
        print(is_leap(year))
except Exception as e:
    print("Enter Integer Value",e)
