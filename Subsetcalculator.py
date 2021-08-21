#!/usr/bin/env python
# coding: utf-8

# In[14]:


# SUBSET CALCULATOR

#Function to create elements with an without the next element
def contloop(lst,num):
    temp = []
    if lst == []:
        temp.append(num)
        temp.append([])
    else:
        for a in lst:
            if a == []:
                temp.append(num)
                temp.append([])
            else:
                temp.append(a)
                if type(a) == list:
                    temp.append(a+[num])
                else:
                    temp.append([a]+[num])
    return temp    


#Entry form the user
a = input('Enter a series of numbers: ')
selection = eval(input('''Choose an operation to perform from below:
1 - Subsets of 2
2 - Substets of 3
3 - Subsets of 4 
4 - Subsets of n
5 - All subsets'''))

#Converting input string into list of integers
num1 = []
for i in a:
    if i != ' ':
        num1.append(int(i))

#Loop to create all subsets
subsets = []
for i in range(len(num1)):
    subsets = contloop(subsets,num1[i])

#Function to create subsets with specific number of elements 'n'
def subs(subsets,n):
    subsets_n = []
    for a in subsets:
        if type(a)!= int:
            if len(a) == n:
                subsets_n.append(a)
        elif n == 1 and type(a)==int:
            subsets_n.append(a)
    print(subsets_n)
    print('Total count is: ',len(subsets_n))
    
#Selection process for each operation chosen by the user
if selection == 1:
    n = 2
    subs(subsets,n)
elif selection == 2:
    n = 3
    subs(subsets,n)
elif selection == 3:
    n = 4
    subs(subsets,n)
elif selection == 4:
    n = eval(input("Enter n value:  "))
    subs(subsets,n)
elif selection == 5:
    print(subsets)
    print('Total count is: ',len(subsets))
else:
    print('Please enter a valid operation')

