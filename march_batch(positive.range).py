# Python program to print all positive numbers in a range.
list1 = [12,-7,5,64,-14]
for num in list1:
#positve number
      if num >= 0:
#end is used so that the output is in the same line          
       print(num, end = " ")
list2 = [12,14,-95,3]
num = 0   
#length is list2 is more than 0
while(num < len(list2)):
    if list2[num] >= 0:
        print(list2[num], end = " ")
#value is incremented by 1 in every iteration, so that there is no repetition of value
    num += 1
