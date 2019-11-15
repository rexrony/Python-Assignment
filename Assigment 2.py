#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Question 1 Answer
subject1=int(input("Enter marks of the Computer subject:" ))
subject2=int(input("Enter marks of the English subject: "))
subject3=int(input("Enter marks of the Maths subject: "))
subject4=int(input("Enter marks of the Urdu subject: "))
subject5=int(input("Enter marks of the Sindhi subject: "))

totalmarks = subject1+subject2+subject3+subject4+subject5
print("Total Marks =",totalmarks) 
avg=(totalmarks/500)*100
print("Total Avg =",avg) 
if(avg>=90):
    print("Grade: A")
elif(avg>=80 or avg<90):
    print("Grade: B")
elif(avg>=70 or avg<80):
    print("Grade: C")
elif(avg>=60 or avg<70):
    print("Grade: D")
else:
    print("Grade: F")


# 

# In[14]:


#Answer 2
userinput = int(input("Type Even OR ODD Number:  "))

if (userinput % 2) == 0:
   print("{0} is Even".format(userinput))
else:
   print("{0} is Odd".format(userinput))


# In[17]:


#Answer 3
listarry =["apple","Bannana","Cake","Pastary"]
print("String Length Is : ", len(listarry)) 


# In[18]:


#Answer 4
numbers = [15,20,33,45,50]
totalsum = sum(numbers)
print("Total Sum : ", totalsum)


# In[24]:


# Question : Write a Python program to get the largest number from a numeric list.
#Answer 5
numbers = [15788,20578,3355,4567,5099,54899,1000]
totalsum = max(numbers)
print("Largest Number in List : ", totalsum)


# In[38]:


# Question : write a program that prints out all the elements of the list that are less than 5.
#Answer 6

a = [33, 1, 2, 3,4, 5, 8, 13, 21, 34, 55, 89]
listlength = int(len(a))
print("Total Number of number in List : ",listlength,  "\n -----------------------------")

for i in range(listlength):
    if a[i]<=5:
        print(a[i])


# In[ ]:





# In[ ]:




