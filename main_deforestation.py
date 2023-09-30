import functions
from pathlib import Path
def write_deforestation():
    downloads=str(Path.home() / "Downloads")
    city_file=downloads+"\Deforestation.csv"
    with open(city_file,"r") as cityfile:
        index=cityfile.readline()
    index=str(int(index))
    functions.deforestation(index)
write_deforestation()