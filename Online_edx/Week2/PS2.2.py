# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 14:12:49 2018

@author: dfadeeff
"""


# Paste your code into this box
balance = 3329
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12.0
minimum_payment = 0
newbalance = balance


while newbalance > 0:
    minimum_payment += 10
    newbalance = balance
    months = 0
    
    while months < 12 and newbalance > 0:
        
        newbalance -= minimum_payment
        interest = monthlyInterestRate*newbalance 
        newbalance += interest
        months += 1
        
        #print(months, newbalance, minimum_payment) 
    
print("Lowest Payment:", minimum_payment)