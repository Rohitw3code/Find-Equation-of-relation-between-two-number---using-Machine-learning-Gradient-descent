# Predict Equation Of given sample
#

import numpy as np
import math as mt

learning_rate = 0.01
epochs = 10000
bias = 1

w = np.random.rand(3)*10 #create a random weight
def Preceptator(x1,x2,output):

    outputP = w[0]+w[1]*x1+w[2]*x2
    
    error0 = learning_rate*(output - outputP)*bias
    error1 = learning_rate*(output - outputP)*x1
    error2 = learning_rate*(output - outputP)*x2
    
    w[0] += error0
    w[1] += error1
    w[2] += error2
    
def getClosestValue(k):
    b = int(k)
    lst = list(range(b-1,b+2,1)) # lst = [b-1,b,b+1] 
    return lst[min(range(len(lst)),key = lambda i : abs(lst[i]-k))] 
###########This return a value which is closest to k from the list lst = [b-1,b,b+1]

def Predict(x1,x2):
    value = w[0]+w[1]*x1+w[2]*x2

    if(value<0):
        print("value : ",int(value)-1)
    elif value == 0:
        print("value : ",value)        
    else:
        print("value : ",int(value))
        
    print("y  =  ",getClosestValue(w[0])," + ",getClosestValue(w[1])," * x1 + ",getClosestValue(w[2])," * x2")   
    

# training sets    
for i in range(epochs):    
    Preceptator(2,1,12) # 5 * 2 + (3 * 1) - 1 = 12  
    Preceptator(2,3,18)
    Preceptator(3,4,26)
    Preceptator(6,1,32)
    Preceptator(9,10,74)
    Preceptator(-1,-1,-8)

print("weights : ",w)

## Predicting value
Predict(0,6)
