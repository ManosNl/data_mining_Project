import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('data.csv')

# Group the data by continent and entity
grouped_data = df.groupby(['Continent', 'Entity', 'Date']).sum()

# Create a 2D numpy array with the columns 'Entity', 'Continent', 'Cases', and 'Date'
np_array = grouped_data.reset_index()[['Entity', 'Continent','Date', 'Cases' ]].to_numpy()

# Print the numpy array
#print(np_array)

# divide the array based on the value of the second column
Africa = np_array[np_array[:, 1] == 'Africa']
Asia = np_array[np_array[:, 1] == 'Asia']
Europe = np_array[np_array[:, 1] == 'Europe']
NAmerica = np_array[np_array[:, 1] == 'North America']
Oceania = np_array[np_array[:, 1] == 'Oceania']
SAmerica = np_array[np_array[:, 1] == 'South America']



continents = [ Africa, Asia, Europe, NAmerica, Oceania,  SAmerica]

for i in continents:
    print (i[0][1])
    print (i)

    # Create a dictionary to store the data for each entity
    entity_data = {}

    # Loop through the rows of the numpy array and add the data to the dictionary
    for row in i:
        entity = row[0]
        date = row[2]
        cases = row[3]
        
        if entity not in entity_data:
            entity_data[entity] = {'dates': [], 'cases': []}
        
        entity_data[entity]['dates'].append(date)
        entity_data[entity]['cases'].append(cases)

    # Plot the data for each entity and calculate the average number of cases
    for entity, data in entity_data.items():
        dates = data['dates']
        cases = data['cases']
        
        plt.plot(dates, cases, label=entity)
        
        #avg_cases = sum(cases) / len(cases)
        #print(f"Average cases for {entity}: {avg_cases:.2f}")

    # Set the x-axis label and rotate the x-tick labels
    plt.xlabel('Date')
    plt.xticks([])

    # Set the y-axis label
    plt.ylabel('Cases')

    # Set the plot title and legend
    plt.title('Cases by Entity')
    plt.legend()

    # Show the plot
    plt.show()