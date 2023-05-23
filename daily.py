import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def fetchdataCountry():
    
    df = pd.read_csv('data.csv')
    user_input = input("Enter a Country: ")
    df_filtered = df[df.iloc[:, 0] == user_input]
    selected_columns = ['Entity', 'Date', 'Cases', 'Deaths']  # Replace with the actual column names you want to select
    df_selected = df_filtered[selected_columns]
    df_selected['daily Cases'] = df_selected['Cases'].diff()
    df_selected['daily Deaths'] = df_selected['Deaths'].diff()
    print(df_selected)
    # Convert the "Date" column to datetime format
    df_selected['Date'] = pd.to_datetime(df_selected['Date'])

    # Plotting
    fig, ax1 = plt.subplots()

    ax1.plot(df_selected['Date'], df_selected['daily Cases'], 'b-')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Daily Cases', color='b')
    ax1.tick_params('y', colors='b')

    ax2 = ax1.twinx()
    ax2.plot(df_selected['Date'], df_selected['daily Deaths'], 'r-')
    ax2.set_ylabel('Daily Deaths', color='r')
    ax2.tick_params('y', colors='r')

    plt.title('Daily Cases and Daily Deaths over Time')
    plt.xticks(rotation=45)

    plt.show()

def fetchdataContinent():
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
    user_input = input("Country (A) or Continent (B)?")
    if user_input=="A":
        fetchdataCountry()
    elif user_input =="B":
        fetchdataContinent()
    else:
        print("wrong input")