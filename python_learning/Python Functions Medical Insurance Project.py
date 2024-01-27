#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Python Functions: Medical Insurance Project


# First, take a look at the code in script.py.
# 
# In this code, we estimate the medical insurance costs for two individuals, Maria and Omar, based on five variables:
# 
# age: age of the individual in years
# sex: 0 for female, 1 for male
# bmi: individual’s body mass index
# num_of_children: number of children the individual has
# smoker: 0 for a non-smoker, 1 for a smoker
# These variables are used in the following formula to estimate an individual’s insurance cost (in USD):

# 
# The code used to estimate insurance costs for Maria and Omar looks quite similar – in both cases we calculate the insurance cost using the same formula and then print the output.
# 
# This code is a great candidate for a function because it involves repeating almost identical commands in multiple places.
# 
# Let’s start by defining a function called calculate_insurance_cost() on line 2. For now, your function should not have any parameters or output.

# In[2]:


def calculate_insurance_cost():


# Let’s outline the behavior we want our function to have. Inside of calculate_insurance_cost(), do the following:
# 
# Create a variable called estimated_cost. For now, set this variable equal to a value of 1000. You’ll add the full formula in the next step.
# Add a print statement that prints estimated_cost. You should output a message similar to: "The estimated insurance cost for this person is xxx dollars."
# Return estimated_cost

# In[6]:


def calculate_insurance_cost():
    estimated_cost = 1000
    print("The estimated insurance cost for", str(person), str(estimated_cost), "dollars")
    return estimated_cost


# 
# Nice job – you’ve created a simple Python function that we’ll use to estimate medical insurance costs.
# 
# However, the function currently returns a value of 1000. We want it to return our insurance cost formula instead.
# 
# Modify the function definition so that it contains five parameters:
# 
# age
# sex
# bmi
# num_of_children
# smoker

# In[7]:


def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker):
    estimated_cost = 1000
    print("The estimated insurance cost for", str(person), str(estimated_cost), "dollars")
    return estimated_cost


# 
# Now that we have set up the function to take inputs for each of the values needed in the insurance formula, we can make use of them inside of our function.
# 
# In calculate_insurance_cost(), change the value of estimated_cost from 1000 to our formula for insurance cost.
# 
# Remember that the formula for insurance cost is:

# In[8]:


def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
    print("The estimated insurance cost for person is ", str(estimated_cost), "dollars")
    return estimated_cost


# he function is now properly set up to calculate an individual’s medical insurance costs based on the five variables passed into it. Let’s test this out!
# 
# Go to the section of code that estimates Maria’s insurance cost.
# 
# Rename insurance_cost as maria_insurance_cost and set it equal to calculate_insurance_cost() with the appropriate values for Maria as arguments.

# In[9]:


#Initial varibales for Maria
age = 28
sex = 0  
bmi = 26.2
num_of_children = 3
smoker = 0 


# In[10]:


insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500


# In[11]:


maria_insurance_cost = calculate_insurance_cost(age = 28, sex = 0, bmi = 26.2, num_of_children = 3, smoker = 0)


# Now, remove the print statement for Maria since our function will take care of printing the estimated cost for us.
# 
# Additionally, remove the five lines of code defining the initial variables for Maria, as we are now passing in these values directly in the function call.

# In[12]:


def calculate_insurance_cost(age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
    print("The estimated insurance cost for person is ", str(estimated_cost), "dollars")
    return estimated_cost


# In[20]:


omar_insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500


# In[17]:


# Initial variables for Omar
age = 35
sex = 1 
bmi = 22.2
num_of_children = 0
smoker = 1  


# In[18]:


omar_insurance_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500


# In[21]:


omar_insurance_cost = calculate_insurance_cost(age = 35, sex = 1, bmi = 22.2, num_of_children = 0, smoker = 1)


# In[24]:


def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
    print("The estimated insurance cost for", str(name), "is", str(estimated_cost), "dollars")
    return estimated_cost


# In[25]:


maria_insurance_cost = calculate_insurance_cost(name = "Maria", age = 28, sex = 0, bmi = 26.2, num_of_children = 3, smoker = 0)


# In[26]:


omar_insurance_cost = calculate_insurance_cost(name = "Omar", age = 35, sex = 1, bmi = 22.2, num_of_children = 0, smoker = 1)

