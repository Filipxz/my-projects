#!/usr/bin/env python
# coding: utf-8

# DATA SCIENCE FOUNDATIONS
# Python Control Flow: Medical Insurance Project
# In this project, you will examine how factors such as age, sex, number of children, and smoking status contribute to medical insurance costs.
# 
# You will apply your knowledge of Python control flow to write code that gives people advice on how to lower their medical insurance costs.
# 
# Let’s get started!

# 1. 
# First, take a look at the code in script.py.
# 
# The function estimate_insurance_cost() estimates the medical insurance cost for an individual, based on four variables:
# 
# age: age of the individual in years
# sex: 0 for female, 1 if male
# num_of_children: number of children the individual has
# smoker: 0 for a non-smoker, 1 for a smoker
# These variables are used in the following formula to estimate an individual’s insurance cost:
# 
# insurance_cost=400∗age
# −128∗sex+425∗num_of_children
# +10000∗smoker−2500
# 
#  
# Click “Save” to see the estimated medical insurance cost for Keanu, a 29 year-old male smoker with three children.

# In[2]:


def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  return estimated_cost


# 2.Currently, our function prints out the estimated insurance cost based on the values passed into the function. But it doesn’t do much beyond that.
# 
# It would be much more helpful if our function could provide more insight into how we can lower our insurance cost. We’ll learn to do exactly that by using control flow – if, elif, and else statements – in our code.
# 
# When you’re ready, move on to the next step.

#    
# 3.In general, insurance costs are higher for smokers. We can use data from the smoker variable to provide advice on how to lower insurance costs.
# 
# Let’s create a function that analyzes an individual’s smoking status.
# 
# At the top of your code, define a function called analyze_smoker() that takes an input smoker_status. For now, the function should print smoker_status.

# In[3]:


def analyze_smoker(smoker_status):


# 4. Now that we’ve written the analyze_smoker() function, let’s make use of it.
# 
# In the estimate_insurance_cost() function, go to the line of code that prints the estimated insurance cost. On the next line, make a function call to analyze_smoker(), passing in the smoker variable as an argument.
# 
# Click “Save” to see the result.

# In[5]:


def analyze_smoker(smoker_status):
  if smoker_status == 1:
    print("To lower your cost, you should consider quitting smoking.")
  else:
    print("Smoking is not an issue for you.")


# In[ ]:


Now that we’ve estimated and analyzed Keanu’s insurance cost, let’s see if we can do the same for our own!

At the bottom of your code, create a new insurance cost variable for yourself, similar to how we did it for Keanu.

Set the variable equal to a function call to estimate_insurance_cost(), passing in your own age, sex, number of children, and smoker status.

get_ipython().run_line_magic('pinfo', 'cost')


# In[6]:


estimate_insurance_cost("FIlip", 28, 1, 26, 0, 0)

