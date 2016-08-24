# import car data from https://think.cs.vt.edu/corgis/
import cars

cardata = cars.get_cars()

def yearOfCar(car):
    return car['Identification']['Year']


def horsepower(cardata):
    hp_list = []
    for i in range(len(cardata)):
        hp_list.append(cardata[i]['Engine Information']['Engine Statistics']['Horsepower'])
    return hp_list

hp_list = horsepower(cardata)

import matplotlib.pyplot as plt

from collections import defaultdict

def histogramify(data,bins):
	M = max(data)
	m = min(data)
	interval = (M-m)/bins
	hist = defaultdict(int)
	for d in data:
		for i in range(bins):
			
			#This line originally said: if d>m+i*interval:
			if d>m+i*interval and d<=m+(i+1)*interval:
				f=m+i*interval
		hist[f]+=1
	return hist

hist_HP = histogramify(hp_list,25)

def MPG(cardata):
    MPG_list = []
    for i in range(len(cardata)):
        MPG_list.append(cardata[i]['Fuel Information']['Highway mpg'])
    return MPG_list

MPG_list = MPG(cardata)

hist_MPG = histogramify(MPG_list,25)

if __name__=="__main__":
   print """
Try:

   cardata = cars.get_cars()

   len(cardata)
   cardata[0]
   cardata[0].keys()
   cardata[0]['some_key']

   """

   # You might add additional code below this comment if you want it to run
   # when you run the file.  Be sure to indent three spaces, just like these comments.
   
