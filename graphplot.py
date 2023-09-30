import csv
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
def graphplot_Temp():    
    with open("Temp_Data.csv","r") as f:        
        l=f.readlines()
    L=[]
    for i in l:        
        L.append(i[:len(i)-1].split(","))

    City_Name=[]
    Temp=[]
        
    for i in range(len(L)):
        City_Name.append(L[i][0])
        Temp.append(float(L[i][1])) 
    
    x = np.array(City_Name)
    y = np.array(Temp)
    plt.bar(x,y)
    plt.show()

def graphplot_AirP():    
    with open("AirPressure_Data.csv","r") as f:        
        l=f.readlines()
    L=[]
    for i in l:        
        L.append(i[:len(i)-1].split(","))

    City_Name=[]   
    Air_Pr=[]
    for i in range(len(L)):
        City_Name.append(L[i][0])          
        Air_Pr.append(float(L[i][1]))
    
    x = np.array(City_Name)
    y = np.array(Air_Pr)
    plt.bar(x,y)
    plt.show()