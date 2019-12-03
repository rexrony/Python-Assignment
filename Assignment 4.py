#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Question 1
firstname = input("Your First Name Please  ");
lastname = input("Your Last Name Please  ");
age = int(input("Your Age Please  "));
city = input("Your City Please  ");

userdata = {
    'first_name': firstname,
    'last_name': lastname,
    'age': age,
    'city': city,
    }
print("\n----------------\n")
print(userdata['first_name'])
print(userdata['last_name'])
print(userdata['age'])
print(userdata['city'])


# In[3]:


#Question 2
dubai = {
    'country': 'UAE',
    'population': '3.137 million',
    'fact': 'The total population of Dubai is 3.1 million. Arabic is the official language. The currency is UAE dirham (AED).',
    }
karachi = {
    'country': 'PAKISTAN',
    'population': '14.91 million',
    'fact': 'In 1729, real settlements were founded, and it was named Kolachi after the name of an old woman, Mai Kolachi (Auntie Kolachi). She was the head of a village and was known for her fair decisions. However, there are many other tales about this city’s  former name ‘Kolachi.’',
    }

Mumbai = {
    'country': 'INDIA',
    'population': '13 million',
    'fact': 'Every day in Mumbai, more than 200 trains make over 2,000 trips along 300 kilometres of track, carrying more passengers per kilometre than any railway on earth.',
    }
#for key, value in Mumbai.items():
#  print(key, "=", value)

print("DUBAI");
for key, value in dubai.items():
  print(key, "=", value)
print("\n----------------\n")

print("PAKISTAN");
for key, value in karachi.items():
  print(key, "=", value)
print("\n----------------\n")

print("Mumbai");
for key, value in Mumbai.items():
  print(key, "=", value)


# In[1]:


#Question 3
ask_age = "How old are you?"
ask_age += "\nType 'end' when you are finished adding age. "

while True:
    age = input(ask_age)
    if age == 'end':
        break
    age = int(age)

    if age < 18:
        print("  You get in free!")
    elif age <= 19:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")        


# In[2]:


#Question 4

def favorite_book(title):

    print(title + " is one of my favorite books.");
fvrt_book = input("Enter your Favorite Book Name : ");
favorite_book(fvrt_book)


# In[2]:


#Question 5
import random
it=random.randint(1, 30)
def main():
    x=int(input('Guess a number between 1 and 30 =  '))
    if x == it:
        print("You got it!")
    elif x > it:
        print("too high")
        main()
    else:
        print("too low")
        main()
main()


# In[ ]:





# In[ ]:




