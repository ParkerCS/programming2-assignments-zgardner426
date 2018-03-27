# MATPLOTLIB PROBLEM # 1
# Chicago Public Library Computer Usage (15pts)
# open and read in the "Libraries_-_2018_Visitors_by_Location.csv" file into a list (use file located in the file folder, read in using csv library).
# calculate (and make a list of) the total visitors to Chicago libraries each month.  
# Do not plot every library individually.  Instead, find the total for all libraries each month and plot that.
# Make a BAR GRAPH with the total visitors on the y and month on the x.  
# label the x with the month.  Rotate the text so we can read it.  (see example problem).  Use the tight_fit command to show all text.
# label axes, title the graph as necessary.
import csv
import matplotlib.pyplot as plt

with open('files/Libraries_-_2017_Visitors_by_Location.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
total_visitors = []
month_names = data.pop(0)[1:-1]
month_values = [x for x in range(1, 13)]

for i in range(1, 13):
    visitors = [x[i] for x in data][1:-1]
    visitors = [int(x) for x in visitors]
    total_visitors.append(sum(visitors))

print(total_visitors)
plt.figure(1, figsize=(10,6), tight_layout=True)
plt.bar(month_values, total_visitors)
plt.xticks(month_values, month_names, rotation=90 )
plt.ylabel("Total Visitors")
plt.title("Visitors By Month Chicago Libraries")
plt.show()


# MATPLOTLIB PROBLEM # 2 
# Chicago Public Transit Usership Graph (20pts)
# go to https://data.cityofchicago.org/Transportation/CTA-Ridership-Annual-Boarding-Totals/w8km-9pzd
# download the CTA ridership data as a csv.
# Read the data into a list using the csv library.
# Make a plot of paratransit, bus, rail, and total numbers by year (all on the same graph).
# Make each line, points, and color different for the four graphs.
# Make a legend to identify each line.
# Label axes and give your graph a title.  Change it in any other way you see necessary to give it a clean look.
with open('files/CTA_-_Ridership_-_Annual_Boarding_Totals.csv') as f:
    reader = csv.reader(f)
    data = list(reader)


years = [x for x in range(1, 30)]
year_names = [x[0] for x in data][1:]

riders_bus = [x[1] for x in data][1:]
riders_bus = [int(x) for x in riders_bus]
riders_paratransit = [x[2] for x in data][1:]
riders_paratransit = [int(x) for x in riders_paratransit]
riders_train = [x[3] for x in data][1:]
riders_train = [int(x) for x in riders_train]
riders_total = [x[4] for x in data][1:]
riders_total = [int(x) for x in riders_total]




plt.figure(2, tight_layout=True)
plt.plot(years, riders_bus, c="red", label="Bus")
plt.plot(years, riders_train, c="blue", label="Train")
plt.plot(years, riders_paratransit, c="green", label="Paratransit")
plt.plot(years, riders_total, c="yellow", label="Total")
plt.xticks(years, year_names, rotation=90)
plt.ylabel("Number of Riders")
plt.xlabel("Years")
plt.title("CTA Ridership 1988-2016")
plt.legend(bbox_to_anchor=(.75, .35), loc="upper left")
plt.show()