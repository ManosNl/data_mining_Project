import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#working
def CountryDeaths():
    # read the CSV file into a pandas dataframe
    df = pd.read_csv('data.csv') # replace 'file.csv' with the name of your file

    # group the data by country and get the maximum number of deaths for each country
    max_deaths = df.groupby('Entity')['Deaths'].max()

    # create a 2D numpy array with the country and maximum number of deaths for each country
    CountryDeathsArr = np.empty((len(max_deaths), 2), dtype=object)
    for i, (country, deaths) in enumerate(max_deaths.iteritems()):
        CountryDeathsArr[i, 0] = country
        CountryDeathsArr[i, 1] = deaths

    # print the 2D numpy array
    print(CountryDeathsArr)
    return CountryDeathsArr

#working
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
    
#notworking
def CountryDeathsContinentCasesChart(data):
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
        values1 = i[:, 2].astype(int)
        values2 = i[:, 3].astype(int)
        # Set the bar width and offset for each group
        bar_width = 0.2
        offset = 0.2
        
        

        # Plot the bar charts
        plt.bar(np.arange(len(labels)) , values1, width=bar_width, align='center', alpha=0.5, label='deaths', color='r', edgecolor='black', linewidth=1.2)
        plt.bar(np.arange(len(labels))+offset , values2, width=bar_width, align='center', alpha=0.5, label='cases', color='g', edgecolor='black', linewidth=1.2)
        

        # Adjust the positions of the bars in each group
        plt.gca().set_xticklabels(labels, rotation=90)
        plt.xticks(labels, fontsize=12)
        plt.ylim(0, 7)
        plt.legend()
        plt.title(str(i[0][1]))
        plt.xlabel('Country')
        plt.show()
 
#working
def CountryDeathsContinent():
    # read the CSV file into a pandas dataframe
    df = pd.read_csv('data.csv') # replace 'file.csv' with the name of your file


    # group  the data by country and get the maximum number of deaths for each country
    max_deaths = df.groupby(['Entity', 'Continent'])['Deaths'].max()


    # create a 2D numpy array with the country, continent, and maximum number of deaths for each country
    data = np.empty((len(max_deaths), 3), dtype=object)
    for i, ((country, continent), deaths) in enumerate(max_deaths.iteritems()):
        data[i, 0] = country
        data[i, 1] = continent
        data[i, 2] = deaths


    # print the 2D numpy array
    #print(data)
    data2 = data[np.argsort(data[:, 1])]
    return data2
   

#working
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
        
        
#NOTworking
#sorted by docs ratio
#RATIOS
#version 2
#practicaly the same as before. Do we need it?? SOSSS
def MedianCountryContinentDocsDeathsCasesRatioChart(data):
    # divide the array based on the value of the second column
    Africa = data[data[:, 1] == 'Africa']
    Asia = data[data[:, 1] == 'Asia']
    Europe = data[data[:, 1] == 'Europe']
    NAmerica = data[data[:, 1] == 'North America']
    Oceania = data[data[:, 1] == 'Oceania']
    SAmerica = data[data[:, 1] == 'South America']
   


    continents = [ Africa, Asia, Europe, NAmerica, Oceania,  SAmerica]
    mediansDeaths =[]
    mediansComp =[]



    for i in continents:
        # extract the labels and values from the array
    
        values = i[:, 5].astype(float)
        medianDeaths = round(np.median(values),2)
        mediansDeaths.append(medianDeaths)
        print(mediansDeaths)
        values2 = i[:, 2].astype(float)
        medianComp = round(np.median(values2),2)
        mediansComp.append(medianComp)
        print(mediansComp)
    
    continents2 = [ "Africa", "Asia", "Europe", "North America", "Oceania",  "South America"]

    values1 = mediansComp
    values2 = mediansDeaths


    # create a bar chart using matplotlib
    conts = ("Africa", "Asia", "Europe", "North America", "Oceania",  "South America")
    means = {
        'Avg Comparison': mediansComp,
        'Avg Deaths': mediansDeaths,        
    }

    x = np.arange(len(conts))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in means.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=2)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('%')
    ax.set_title('Continents Comparison')
    ax.set_xticks(x + width, conts)
    #ax.legend(loc='upper left', ncols=2)
    ax.set_ylim(0, 250)

    plt.show()
  
def CasesTimeCountryContintent():
    # read the CSV file into a pandas dataframe
    df = pd.read_csv('data.csv') # replace 'file.csv' with the name of your file

    max_deaths = df.groupby(['Entity', 'Continent', "Medical doctors per 1000 people"])
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


def try1():
    df = pd.read_csv('data.csv')
    user_input = input("Enter a Continent: ")
    df_filtered = df[df.iloc[:, 1] == user_input]
    selected_columns = ['Entity', 'Continent', 'Date', 'Cases', 'Deaths']
    df_selected = df_filtered[selected_columns]
    df_selected['daily Cases'] = df_selected.groupby('Entity')['Cases'].diff()
    df_selected['daily Deaths'] = df_selected.groupby('Entity')['Deaths'].diff()

    # Replace negative values with zero for daily Cases and daily Deaths
    df_selected['daily Cases'] = np.where(df_selected['daily Cases'] < 0, 0, df_selected['daily Cases'])
    df_selected['daily Deaths'] = np.where(df_selected['daily Deaths'] < 0, 0, df_selected['daily Deaths'])

    # Convert the "Date" column to datetime format
    df_selected['Date'] = pd.to_datetime(df_selected['Date'])

    # Plotting
    

    # Group by entity and plot each entity's daily cases

    user_input2 = input("Dearhs as D or Cases as C?")
    if user_input2 =="D":
        fig, ax = plt.subplots()
        for entity, data in df_selected.groupby('Entity'):
            ax.plot(data['Date'], data['daily Deaths'], label=entity)        
        

        ax.set_xlabel('Date')
        ax.set_ylabel('Daily Deaths')
        ax.set_title('Daily Deaths for Entities in ' + user_input)
        ax.legend()
        ax.tick_params(axis='x', rotation=45)

        plt.show()
    elif user_input2 =="C":
        fig, ax = plt.subplots()
        for entity, data in df_selected.groupby('Entity'):
            ax.plot(data['Date'], data['daily Cases'], label=entity)        
        

        ax.set_xlabel('Date')
        ax.set_ylabel('Daily Cases')
        ax.set_title('Daily Cases for Entities in ' + user_input)
        ax.legend()
        ax.tick_params(axis='x', rotation=45)

        plt.show()
    else:
        print("wrong input")
    
if __name__ == '__main__':
    try1()

    
    

