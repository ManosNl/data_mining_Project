import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#working
#incr X
#basically useess, MIGHT REMOVE LATER !!!
def CountryContinentXDeathsCases(variable):
    # read the CSV file into a pandas dataframe
    df = pd.read_csv('data.csv') # replace 'file.csv' with the name of your file

    # group the data by country and get the maximum number of deaths for each country
    max_deaths = df.groupby(['Entity', 'Continent', variable])['Deaths'].max()
    max_cases = df.groupby(['Entity', 'Continent'])['Cases'].max()
    
    # create a 2D numpy array with the country, continent, and maximum number of deaths for each country
    data = np.empty((len(max_deaths), 5), dtype=object)
    for i, ((country, continent, X), deaths) in enumerate(max_deaths.iteritems()):
        data[i, 0] = country
        data[i, 1] = continent
        data[i, 2] = X
        data[i, 3] = deaths
    for i, ((country, continent), cases) in enumerate(max_cases.iteritems()):
        data[i, 4] = cases
    # print the 2D numpy array
    #print(data)
    data2 = data[np.argsort(data[:, 1])]
    data3 = data[data[:, 2].argsort()]
    #print(data2)
    return data3
        
#working
#sorted by gdp ratio
def CountryContinentXDeathsCasesChart(data):
    # divide the array based on the value of the second column
    Africa = data[data[:, 1] == 'Africa']
    Asia = data[data[:, 1] == 'Asia']
    Europe = data[data[:, 1] == 'Europe']
    NAmerica = data[data[:, 1] == 'North America']
    Oceania = data[data[:, 1] == 'Oceania']
    SAmerica = data[data[:, 1] == 'South America']
   


    continents = [ Africa, Asia, Europe, NAmerica, Oceania,  SAmerica]




    for i in continents:
                
        # Create a sample 2D numpy array with 5 columns
        arr = i

        # Create a figure and axis object
        fig, ax = plt.subplots()

        # Define the x positions for the bars
        x = np.arange(arr.shape[0])

        # Define the widths for the bars
        width = 0.35

        # Plot the first bar for each row
        rects1 = ax.bar(x - width/2, arr[:, 3], width, label='Deaths')

        # Plot the second bar for each row
        rects2 = ax.bar(x + width/2, arr[:, 4], width, label='Cases')

        # Add some labels and a legend
        ax.set_ylabel('Number')
        ax.set_title(str(i[0][1]))
        ax.set_xticks(x)
        ax.set_xticklabels(arr[:, 2] )
        
        plt.xticks(rotation=90)
        ax.legend()

        # Show the plot
        plt.show()
        
#working
#sorted by X ratio
#RATIOS
def CountryContinentXDeathsCasesRatio(variable):
    # read the CSV file into a pandas dataframe
    df = pd.read_csv('data.csv') # replace 'file.csv' with the name of your file

    # group the data by country and get the maximum number of deaths for each country
    max_deaths = df.groupby(['Entity', 'Continent', variable])['Deaths'].max()
    max_cases = df.groupby(['Entity', 'Continent'])['Cases'].max()
    
    # create a 2D numpy array with the country, continent, and maximum number of deaths for each country
    data = np.empty((len(max_deaths), 6), dtype=object)
    for i, ((country, continent, X), deaths) in enumerate(max_deaths.iteritems()):
        data[i, 0] = country
        data[i, 1] = continent
        data[i, 2] = X
        data[i, 3] = deaths
    for i, ((country, continent), cases) in enumerate(max_cases.iteritems()):
        data[i, 4] = cases
    for i in range(len(data)):
        data[i, 5] = round(( data[i,3] / data[i,4] ) *100 , 2)
    # print the 2D numpy array
    #print(data)
    data2 = data[np.argsort(data[:, 1])]
    data3 = data[data[:, 2].argsort()]
    #print(data2)
    return data3
        
#working
#sorted by X ratio
#RATIOS
def CountryContinentXDeathsCasesRatioChart(data):
    # divide the array based on the value of the second column
    Africa = data[data[:, 1] == 'Africa']
    Asia = data[data[:, 1] == 'Asia']
    Europe = data[data[:, 1] == 'Europe']
    NAmerica = data[data[:, 1] == 'North America']
    Oceania = data[data[:, 1] == 'Oceania']
    SAmerica = data[data[:, 1] == 'South America']
   


    continents = [ Africa, Asia, Europe, NAmerica, Oceania,  SAmerica]




    for i in continents:
        # extract the labels and values from the array
        countries = i[:, 0]
        values = i[:, 5].astype(float)


        # create a bar chart using matplotlib
        plt.gca().set_xticklabels(i[:, 2], rotation=90)
        plt.bar(countries, values)
        plt.xlabel('Country')
        plt.ylabel('Deaths to Cases %')
        plt.title(str(i[0][1]))
        plt.show()

def MedianCountryContinentXDeathsCasesRatioChart(data):
    # divide the array based on the value of the second column
    Africa = data[data[:, 1] == 'Africa']
    Asia = data[data[:, 1] == 'Asia']
    Europe = data[data[:, 1] == 'Europe']
    NAmerica = data[data[:, 1] == 'North America']
    Oceania = data[data[:, 1] == 'Oceania']
    SAmerica = data[data[:, 1] == 'South America']
   


    continents = [ Africa, Asia, Europe, NAmerica, Oceania,  SAmerica]
    medians =[]
    mediansX = []



    for i in continents:
        # extract the labels and values from the array
    
        values = i[:, 5].astype(float)
        median = round(np.median(values),2)
        medians.append(median)
        #print(medians)
        values2 = i[:, 5].astype(float)
        medianX = round(np.median(values2),2)
        mediansX.append(medianX)
    
    continents2 = [ "Africa", "Asia", "Europe", "North America", "Oceania",  "South America"]
    values = medians


    # create a bar chart using matplotlib
    plt.gca().set_xticklabels(mediansX, rotation=45)
    #plt.gca().set_xticklabels(continents2, rotation=45)
    plt.bar(continents2, values)
    plt.xlabel('Continents')
    plt.ylabel('Deaths to Cases %')
    plt.title("Continents Comparison")
    plt.show()

def printCharts(data):
    CountryContinentXDeathsCasesChart(data)
    CountryContinentXDeathsCasesRatioChart(data)
    MedianCountryContinentXDeathsCasesRatioChart(data)
    
if __name__ == '__main__':
    print("For each Demographic statistic, we will print a bar chart based with both death-cases and one with the ratio deaths/cases. Also, one with comparison for all the continents")
    print("increasing GDP")
    dataGDP = CountryContinentXDeathsCasesRatio("GDP/Capita")
    printCharts(dataGDP)

    print("increasing Population")
    dataPopulation = CountryContinentXDeathsCasesRatio("Population")
    printCharts(dataPopulation)

    print("increasing Median age")
    dataMage = CountryContinentXDeathsCasesRatio("Median age")
    printCharts(dataMage)

    print("increasing Population aged 65 and over (%)")
    dataOver65 = CountryContinentXDeathsCasesRatio("Population aged 65 and over (%)")
    printCharts(dataOver65)







