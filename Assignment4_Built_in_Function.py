
###1rst part###

list1=[]
while True:     #repeat until the user enters a valid list of numbers
    try:
        size=int(input("Enter a positive integer for the size of your list: "))
        if size <= 0:
            print("Please enter a positive integer.")
        else:
            break
    except ValueError:
        print("Please enter a valid list size")


for i in range(size):
    try:
        element=int(input(f"Enter element {i+1}: "))
        list1.append(element)     #add the entered element to the list
    except ValueError:
        print("Please enter a valid integer.")
        continue

    
print("The list you entered is:",list1)
average=round(sum(list1)/len(list1),2)              #rounding the average to 2 decimal places
print("The average of the elements in the list is:", average)
sorted_list = sorted(list1)       #sort the list in ascending order
print("the sorted list is:", sorted_list)
if len(sorted_list) % 2 == 0:       #if the length of the list is even, the median is the average of the two middle elements
    median1 = sorted_list[len(sorted_list)//2]
    median2 = sorted_list[len(sorted_list)//2 - 1]
    median = (median1 + median2)/2
else:
    median = sorted_list[len(sorted_list)//2]      #if the length of the list is odd, the median is the middle element
print("the median element of the list is:", median)

range_list=max(list1)-min(list1)                     #the range of the list is the difference between the max and min elements in the list
print("the range of the list is:", range_list)



######2nd part ###########
while True:  #repeat until the user enters a valid list of numbers 
    try:
        mystring = input("Enter a list of numbers separated by spaces: ")
        break
    except ValueError:
        print("Please enter a valid list of numbers.")
        continue


mylist = [int(x) for x in mystring.split()]  #convert the input string into a list of integers


message = ""
for i in range(len(mylist)): 
    if mylist[i] not in range(0, 256):   # if the number can't be written in ascii, list as a negative number.
        message += str("-" + str(mylist[i])) + " "   #assign negative number to message
    else:
        oct_value = oct(mylist[i])    #transform the list of integers into octal
        character = chr(int(oct_value[2:], 8))  #get the last character of the ascii representation
        message += character + " "    #transform the list of octal representations into ascii charecters

print("The message is:", message) 




