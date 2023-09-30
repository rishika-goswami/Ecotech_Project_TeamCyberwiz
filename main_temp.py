import csv
import functions
import graphplot
from pathlib import Path

def write_temp():
    downloads=str(Path.home() / "Downloads")
    city_file=downloads+"\Temp_Data.csv"
    with open(city_file,"r") as cityfile:
        reader=csv.reader(cityfile)
        for row in reader:
            cities=row
    cities[0]=cities[0].lstrip("undefined")
    cities.pop(-1)   
    for i in cities:
        i.title() 
    with open('Temp_Data.csv','w',newline='') as f:
        writer=csv.writer(f)
        
        for i in cities:
            temp_l=functions.temperature(i)
            writer.writerow(temp_l)
            print(temp_l)    

def temp():
    write_temp()
    graphplot.graphplot_Temp()

temp()