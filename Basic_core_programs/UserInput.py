"""
    * Author - Nitin Chandrakant Babar
    * Date -  14-12-2021
    * Time -  10.30pm
    * Title - User Input and Replace String Template
"""



text=input("User Name:")
text=str(text)
text_length=len(text)
   
if text_length >= 3:
    print(text_length)
    print("Hello", text,"How are you?")
else:
    print("Inalid Name")