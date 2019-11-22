#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1 Make a calculator using Python with addition , subtraction , multiplication ,division and power.

# Function to add two numbers 
def add(num1, num2): 
	return num1 + num2 

# Function to subtract two numbers 
def subtract(num1, num2): 
	return num1 - num2 

# Function to multiply two numbers 
def multiply(num1, num2): 
	return num1 * num2 

# Function to divide two numbers 
def divide(num1, num2): 
	return num1 / num2 

print("Please select operation -\n" 
		"1. Add\n" 
		"2. Subtract\n" 
		"3. Multiply\n" 
		"4. Divide\n") 


# Take input from the user 
select = input("Select operations form +, -, x, / :") 

number_1 = int(input("Enter first number: ")) 
number_2 = int(input("Enter second number: ")) 

if select == '+': 
    print(number_1, "+", number_2, "=",  add(number_1, number_2)) 

elif select == '-': 
    print(number_1, "-", number_2, "=",  subtract(number_1, number_2)) 

elif select == 'x': 
	print(number_1, "*", number_2, "=",  multiply(number_1, number_2)) 

elif select == '/': 
	print(number_1, "/", number_2, "=", divide(number_1, number_2)) 
else: 
    print("Invalid input") 


# In[26]:


# 2 Write a program to check if there is any numeric value in list using for loop

lists = ["apple", "banana",45,"Saylani","Phython", "cherry", 500 ]
for i in lists:
    try:
        a = int(i) 
        print("This is Numeric Value in list : ",  i)
    except ValueError:
         print("")


# In[27]:


# 3 Write a Python program to sum all the numeric items in a dictionary
score = {"Hafiz": 100, 2: 200, "Zain": 300}
print("Dictionary : ", score);
# Adding More Keyword in Dictionary
score.update({ 4 : 400, "Rex":5, "Rony": 6})
print("Add New Element in Dictionary : ",score);
print("\n-----------\n")
for key, value in score.items():
  print(key, "=", value)


# In[11]:


# 4 Write a Python program to sum all the numeric items in a dictionary

dictionary_value = {'Maths':70,'English':45,'Urdu':47}

for key, value in dictionary_value.items():
    print(key, "=", value)
    
print("\n All Sum Total : ", sum(dictionary_value.values()))


# In[19]:


# 5 Write a program to identify duplicate values from list
print ("Duplicate Numbers List")
my_list = [20,30,20,30,40,50,15,11,20,40,50,15]
my_list.sort()
for i in range (len (my_list) -1):
    
    if my_list[i] == my_list[i+1]:
        print (my_list[i])


# In[34]:


# 6 Write a Python script to check if a given key already exists in a dictionary
dict_key = input("Enter Dict Key = " )

def checkKey(dict, key): 
      
    if key in dict: 
        print("---------\nKey Enter ", dict_key) 
        print("value =", dict[key]) 
    else: 
        print("Key is not present") 


dict = {'a': 100, 'b':200, 'c':300,'d':400,'e':500,'f':600,'g':700,} 
  
key = dict_key
checkKey(dict, key) 


# In[ ]:




