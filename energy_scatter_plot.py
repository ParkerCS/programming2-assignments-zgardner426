'''
Energy Efficiency of Chicago Schools (35pts)

https://data.cityofchicago.org/Environment-Sustainable-Development/Chicago-Energy-Benchmarking-2016-Data-Reported-in-/fpwt-snya\

Chicago requires that all buildings over 50000 square feet in the city comply with energy benchmark reporting each year.
The dataset at the link above is that data from 2016 which was reported in 2017.

We will use this data to look at schools.  We will visualize the efficiency of schools by scatter plot.  
We expect that the more square footage (sqft) a school is, the more greenhouse gas (ghg) emission it will produce.
An efficient school would have a large ratio of sqft to ghg.  
It would also be interesting to know where Parker lies on this graph???  Let's find out.

Make a scatterplot which does the following:  
- Plots the Total Greenhouse gas (GHG) Emmissions (y-axis), versus building square footage (x-axis) (13pts)
- Includes ONLY data for K-12 Schools. (3pts)
- Labelled x and y axis and appropriate title (3pt)
- Annotated labels (school name) for the 5 highest and 5 lowest GHG Intensities. (3pts)
- Label Francis W. Parker. (3pts)
- Create a best fit line for schools shown. (5pts)
- Customize your graph in a discernable way using any technique discussed or one from the API (matplotlib.org). (5pts)


Challenge (for fun):
- Make schools in top 10 percent of GHG Intensity show in green.
- Make schools in bottom 10 percent GHG Intesity show in red.
- Add colleges and universities (use a different marker type)

'''

import matplotlib.pyplot as plt
import csv
import numpy as np

with open('files/Chicago_Energy_Benchmarking_-_2016_Data_Reported_in_2017.csv') as f:
    reader = csv.reader(f)
    data = list(reader)



total_GHG_emissions = []
gHG_intensity = []
square_footage = []
school_names = []
data = [x for x in data if x[6] == "K-12 School"]
data = [x for x in data if x[21] != ""]
data.sort(key=lambda x: float(x[21]))

for i in range(len(data)):
        try:
            gHG_emission = float(data[i][20])
            gHG_intens = float(data[i][21])
            square_f = float(data[i][7])
            total_GHG_emissions.append(gHG_emission)
            gHG_intensity.append(gHG_intens)
            square_footage.append(square_f)
            names = data[i][2]
            school_names.append(names)
        except:
            print("failed", data[i][2])

print(school_names)
plt.figure(1, facecolor="lightgreen", figsize=(12,7))
plt.scatter(square_footage, total_GHG_emissions, edgecolors="black", alpha=.3)
plt.title("Greenhouse Gas Emissions in K-12 Schools by Square Footage", color="darkblue")
plt.ylabel("Total Greenhouse Gas Emissions", color="darkblue")
plt.xlabel("Square Footage", color="darkblue")
plt.annotate(school_names[0], xy=(square_footage[0], total_GHG_emissions[0]))
plt.annotate(school_names[-1], xy=(square_footage[-1], total_GHG_emissions[-1]))
m, b = np.polyfit(square_footage, total_GHG_emissions , 1)
x = [0, 1000000]
y = [point * m + b for point in x]
plt.plot(x, y)
a = school_names.index("Francis W Parker School")
plt.annotate(school_names[a], xy=(square_footage[a], total_GHG_emissions[a]))
plt.show()