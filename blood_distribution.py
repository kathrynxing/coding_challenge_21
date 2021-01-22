import sys
from pandas import DataFrame, Series

# kathryn xing 
# solution to AccessAlly Coding challenge Q2
# 2021.Jan.21

# read input 
filename = sys.argv[1]
f = open(filename, 'r')
# f = open('Blood-Distribution/s4.3.in','r')

blood_supply = Series(f.readline().strip().split(' '), index=['O-','O+','A-','A+','B-','B+','AB-','AB+']).astype(int)
blood_demand = Series(f.readline().strip().split(' '), index=['O-','O+','A-','A+','B-','B+','AB-','AB+']).astype(int) 

# blood_supply = Series([5,5,3,1,2,11,5,12],index=['O-','O+','A-','A+','B-','B+','AB-','AB+'])
# blood_demand = Series([2,4,9,2,3,9,7,3], index=['O-','O+','A-','A+','B-','B+','AB-','AB+'])

# preprocessing 
# reciever_of[t] gives the list of patients who can use type t blood
receiver_of = {
    'O-': ['AB+', 'AB-', 'B+', 'B-', 'A+', 'A-', 'O+', 'O-'],
    'O+': ['AB+','B+','A+', 'O+'],
    'A-': ['AB+', 'AB-','A+', 'A-'],
    'A+': ['AB+', 'A+'],
    'B-': ['AB+','AB-','B+', 'B-'],
    'B+': ['AB+', 'B+'],
    'AB-':['AB+','AB-'],
    'AB+':['AB+']
}

rules = {
    'O-': ['O-'],
    'O+': ['O+', 'O-'],
    'A-': ['A-', 'O-'],
    'A+': ['A+','A-','O+','O-'],
    'B-': ['B-', 'O-'],
    'B+': ['B+','B-','O+','O-'],
    'AB-':['AB-','B-','A-', 'O-'],
    'AB+':['AB+', 'AB-', 'B+', 'B-', 'A+', 'A-', 'O+', 'O-']
}
def max_patients_filled_strategy1():
    # returns the max number of patients that can recieve blood
    max_patients = 0
    order = ['AB+', 'AB-', 'B+', 'B-', 'A+', 'A-', 'O+', 'O-']
    for t in order:
        t1 = receiver_of[t]
        t1.reverse() #return a list of potential users of blood t
        # blood_demand[t1] #the actual demand multiple colomns 
        # blood_supply[t] #the amount of type t blood available
        
        # t1 is max 8 elemets - loop is bounded O(1) 
        for tx in t1:
            # from actual demands we prioritize negative types 
            if tx[-1] == '-':
                # greedy: because who gets the blood does not change the outout
                amt = min(blood_supply[t], blood_demand[tx])
                blood_supply[t] -= amt
                blood_demand[tx]-= amt
                max_patients += amt
        
        # remaining type t blood for the remaining demand 
        for tx in t1:
            if tx[-1] == '+':
                amt = min(blood_supply[t], blood_demand[tx]) 
                blood_supply[t] -= amt
                blood_demand[tx]-= amt
                max_patients += amt
        
        
    return max_patients

def max_patients_filled_strategy2():
    # not optimal / not used 
    # tried greedy from two directions divide and conqure
    max_patients = 0
    order1 = ['AB+', 'AB-', 'B+', 'A+','B-', 'A-', 'O+', 'O-']
    order2 = ['O-', 'O+', 'A-', 'B-']
    for t in order2:
        for tx in rules[t]:
            amt = min(blood_demand[tx], blood_supply[tx])
            blood_demand[tx] -= amt
            blood_supply[tx] -= amt
            max_patients+=amt
    
    for t in order1:
        # receiver_of[t]
        for tx in receiver_of[t]:
            amt = min(blood_demand[tx], blood_supply[tx])
            blood_demand[tx] -= amt
            blood_supply[tx] -= amt
            max_patients+=amt
        # blood_supply[t]
        # blood_demand[t]
    return max_patients
    


# print (receiver_of('O-', 'AB+'))
a1 = max_patients_filled_strategy1()
print(a1)
# output one number to cmd line 