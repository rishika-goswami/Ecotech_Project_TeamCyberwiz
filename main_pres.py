import csv
import functions
import graphplot
from pathlib import Path
import ctypes
        
def write_pres():
    downloads=str(Path.home() / "Downloads")
    city_file=downloads+"\AirPressure_Data.csv"
    with open(city_file,"r") as cityfile:
        reader=csv.reader(cityfile)
        for row in reader:
            cities=row
    cities[0]=cities[0].lstrip("undefined")
    cities.pop(-1)  
    for i in cities:
        i.title() 
    with open('AirPressure_Data.csv','w',newline='') as f:        
        writer=csv.writer(f)
        for i in cities:            
            airp_l=functions.airpressure(i)
            if(airp_l[1].isdigit()):
                writer.writerow(airp_l)
            else:
                WS_EX_TOPMOST=0x40000
                windowTitle="Pressure Data Unavailable"
                message="Sorry! We have no air pressure data for {}".format(airp_l[0])
                ctypes.windll.user32.MessageBoxExW(None,message,windowTitle,WS_EX_TOPMOST)                
                exit()

def pres():
    write_pres()
    graphplot.graphplot_AirP()

pres()