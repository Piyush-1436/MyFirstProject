# Syntax:

# if (condition1):              # if condition1 is True and it can be used lonely many times
      # print ("yes") 
# elif   (condition2):          # if condition2 is True and there can be any number of elif can not
                                # be functioned singly like if.
      # print("no") 
# else:                         # otherwise but it can't be used many times, it need (if)
      # print("maybe")


#Quick Quiz: Write a program to print yes when the age entered by the user is greater than or equal to 18.


a = int(input("Enter your age: "))
if(a>=18):
    print("You match the age of consent.")
elif(a<0):
    print("Age is invalid.")                        # The space before the print is known as indent.
    print("Try again.")                          
else:
    print("You are below the age of consent.")
