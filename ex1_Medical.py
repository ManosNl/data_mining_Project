import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def CountryDeathsContinentCases():
    # read the CSV file into a pandas dataframe
    df = pd.read_csv('data.csv') # replace 'file.csv' with the name of your file

    # group the data by country and get the maximum number of deaths for each country
    max_deaths = df.groupby(['Entity', 'Continent'])['Deaths'].max()
    max_cases = df.groupby(['Entity', 'Continent'])['Cases'].max()
    
    # create a 2D numpy array with the country, continent, and maximum number of deaths for each country
    data = np.empty((len(max_deaths), 4), dtype=object)
    for i, ((country, continent), deaths) in enumerate(max_deaths.iteritems()):
        data[i, 0] = country
        data[i, 1] = continent
        data[i, 2] = deaths
    for i, ((country, continent), cases) in enumerate(max_cases.iteritems()):
        data[i, 3] = cases
    # print the 2D numpy array
    #print(data)
    data2 = data[np.argsort(data[:, 1])]
    return data2

def CountryDeathsContinentChart(data):
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
        labels = i[:, 0]
        values = i[:, 2].astype(int)


        # create a bar chart using matplotlib
        plt.gca().set_xticklabels(labels, rotation=90)
        plt.bar(labels, values)
        plt.xlabel('Country')
        plt.ylabel('Deaths')
        plt.title(str(i[0][1]))
        plt.show()
#working
#sorted by beds ratio
def CountryContinentBedsDeathsCases():
    # read the CSV file into a pandas dataframe
    df = pd.read_csv('data.csv') # replace 'file.csv' with the name of your file

    # group the data by country and get the maximum number of deaths for each country
    max_deaths = df.groupby(['Entity', 'Continent', "Hospital beds per 1000 people"])['Deaths'].max()
    max_cases = df.groupby(['Entity', 'Continent'])['Cases'].max()
    
    # create a 2D numpy array with the country, continent, and maximum number of deaths for each country
    data = np.empty((len(max_deaths), 5), dtype=object)
    for i, ((country, continent, hospitalBeds), deaths) in enumerate(max_deaths.iteritems()):
        data[i, 0] = country
        data[i, 1] = continent
        data[i, 2] = hospitalBeds
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
#sorted by beds ratio
def CountryContinentBedsDeathsCasesChart(data):
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
#sorted by beds ratio
#RATIOS
def CountryContinentBedsDeathsCasesRatioChart(data):
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
        plt.gca().set_xticklabels(countries, rotation=90)
        plt.bar(countries, values)
        plt.xlabel('Country')
        plt.ylabel('Deaths to Cases %')
        plt.title(str(i[0][1]))
        plt.show()
  
#working
#sorted by beds ratio
#RATIOS
def MedianCountryContinentBedsDeathsCasesRatioChart(data):
    # divide the array based on the value of the second column
    Africa = data[data[:, 1] == 'Africa']
    Asia = data[data[:, 1] == 'Asia']
    Europe = data[data[:, 1] == 'Europe']
    NAmerica = data[data[:, 1] == 'North America']
    Oceania = data[data[:, 1] == 'Oceania']
    SAmerica = data[data[:, 1] == 'South America']
   


    continents = [ Africa, Asia, Europe, NAmerica, Oceania,  SAmerica]
    medians =[]



    for i in continents:
        # extract the labels and values from the array
    
        values = i[:, 5].astype(float)
        median = round(np.median(values),2)
        medians.append(median)
        print(medians)
    
    continents2 = [ "Africa", "Asia", "Europe", "North America", "Oceania",  "South America"]
    values = medians


    # create a bar chart using matplotlib
    plt.gca().set_xticklabels(continents2, rotation=45)
    plt.bar(continents2, values)
    plt.xlabel('Continents')
    plt.ylabel('Deaths to Cases %')
    plt.title("Continents Comparison")
    plt.show()

#working
#sorted by beds ratio
#RATIOS
def CountryContinentBedsDeathsCasesRatio():
    # read the CSV file into a pandas dataframe
    df = pd.read_csv('data.csv') # replace 'file.csv' with the name of your file

    # group the data by country and get the maximum number of deaths for each country
    max_deaths = df.groupby(['Entity', 'Continent', "Hospital beds per 1000 people"])['Deaths'].max()
    max_cases = df.groupby(['Entity', 'Continent'])['Cases'].max()
    
    # create a 2D numpy array with the country, continent, and maximum number of deaths for each country
    data = np.empty((len(max_deaths), 6), dtype=object)
    for i, ((country, continent, hospitalBeds), deaths) in enumerate(max_deaths.iteritems()):
        data[i, 0] = country
        data[i, 1] = continent
        data[i, 2] = hospitalBeds
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
#sorted by docs ratio
#RATIOS
def CountryContinentDocsDeathsCasesRatio():
    # read the CSV file into a pandas dataframe
    df = pd.read_csv('data.csv') # replace 'file.csv' with the name of your file

    # group the data by country and get the maximum number of deaths for each country
    max_deaths = df.groupby(['Entity', 'Continent', "Medical doctors per 1000 people"])['Deaths'].max()
    max_cases = df.groupby(['Entity', 'Continent'])['Cases'].max()
    
    # create a 2D numpy array with the country, continent, and maximum number of deaths for each country
    data = np.empty((len(max_deaths), 6), dtype=object)
    for i, ((country, continent, Docs), deaths) in enumerate(max_deaths.iteritems()):
        data[i, 0] = country
        data[i, 1] = continent
        data[i, 2] = Docs
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
#sorted by docs ratio
#RATIOS
#practicaly the same as before. Do we need it?? SOSSS
def CountryContinentDocsDeathsCasesRatioChart(data):
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
        plt.gca().set_xticklabels(countries, rotation=90)
        plt.bar(countries, values)
        plt.xlabel('Country')
        plt.ylabel('Deaths to Cases %')
        plt.title(str(i[0][1]))
        plt.show()
        
  

if __name__ == '__main__':
    
    #print("the data by bed w/out ratio")
    #data2 = CountryContinentBedsDeathsCases()
    #CountryContinentBedsDeathsCasesChart(data2)
    #print("the data by bed w/ ratio")
    #data3 = CountryContinentBedsDeathsCasesRatio()
    #CountryContinentBedsDeathsCasesRatioChart(data3)
    #print("the data by docs w/ ratio")
    #data4 = CountryContinentDocsDeathsCasesRatio()
    #CountryContinentDocsDeathsCasesRatioChart(data4)
    #move this to another file
    print("this shoud be moved to another file")
    print("the data country / conitnents / deaths /cases")
    data1 = CountryDeathsContinentCases()
    CountryDeathsContinentChart(data1)