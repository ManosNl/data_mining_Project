import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import csv
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objs as go
from plotly import tools
from plotly.subplots import make_subplots
import plotly.offline as py

def pre1():
    df = pd.read_csv('data.csv')
    print(df.info())
    #df2 = df.dropna()
    #print(df2.info())
    dummies = []
    cols = ['Entity', 'Continent', 'Date']
    for col in cols:
        dummies.append(pd.get_dummies(df[col]))
    covid_dummies = pd.concat(dummies, axis=1)
    df = pd.concat((df,covid_dummies), axis=1)
    df = df.drop(['Entity', 'Continent', 'Date'], axis=1)
    print(df.info())

def ForEachCountryDatasetInfo():
    df = pd.read_csv('data.csv')
    for entity in df['Entity'].unique():
        print(entity)
        entity_df = df[df['Entity'] == entity]
        entity_df.to_csv(f'{entity}_data.csv', index=False)
        print(entity_df.info())
        entity_df['Daily tests'] = entity_df['Daily tests'].interpolate()


def addPerc(Country):
    #print("adding")
    df = pd.read_csv('data.csv')
    df_filtered = df[df.iloc[:, 0] == Country]
    selected_columns = ['Entity', 'Date', 'Cases', 'Deaths', 'Population', "Daily tests"]  # Replace with the actual column names you want to select
    df_selected = df_filtered[selected_columns]
    df_selected['daily Cases'] = df_selected['Cases'].diff()
    df_selected['daily Deaths'] = df_selected['Deaths'].diff()
    #print(df_selected)
    # Add two new columns
    df_selected['Positivity Rate'] = df_selected['daily Cases'] / df_selected['Daily tests']
    df_selected['Death Rate'] = df_selected['daily Deaths'] / df_selected['daily Cases']
    df_selected['Cases per Population'] = df_selected['Deaths'] / df_selected['Population']
    # Convert the "Date" column to datetime format
    df_selected['Date'] = pd.to_datetime(df_selected['Date'])
    #print(df_selected)
        # Calculate medians of the new columns
    median_column1 = round(df_selected['Positivity Rate'].median(),6)
    median_column2 = round(df_selected['Death Rate'].median(),6)
    median_column3 = round(df_selected['Cases per Population'].median(),6)
    medians = np.array([])
    medians = np.append(medians, [Country, median_column1,median_column2, median_column3])
    return medians

def PercForAllCountries():
    print("all")
    df = pd.read_csv('data.csv')
    statistics_df = pd.DataFrame(columns=['Entity', 'Positivity Rate','Death Rate', 'Cases per Population' ])
    
    for entity in df['Entity'].unique():
        print(entity)
        stats = addPerc(entity)
        statistics_df = statistics_df.append({'Entity': entity, 'Positivity Rate': stats[1],'Death Rate': stats[2],'Cases per Population': stats[3]}, ignore_index=True)
    # Specify the file path for the new CSV file
    output_file = "statistics_with_entity1.csv"

    # Write the DataFrame to the CSV file
    statistics_df.to_csv(output_file, index=False)


def cl():
    print("cl")
    df = pd.read_csv('statistics_with_entity2.csv')
    print(df)
    X = df[['Positivity Rate','Death Rate' ]]
    kmeans = KMeans(n_clusters=3) 
    kmeans.fit(X)
    labels = kmeans.labels_
    colors = ['red', 'green', 'blue']
    df['Graph_Color'] = [colors[label] for label in labels]
    plt.scatter(df['Positivity Rate'], df['Death Rate'] ,c=df['Graph_Color'])
    centroids = kmeans.cluster_centers_
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=200, linewidths=1, color='black')

    # Add labels to the plot
    plt.xlabel('(g)')
    plt.ylabel('Level')
    plt.title('Clustering with K-Means')

    # Show the plot
    plt.show()

def cl():
    print("cl")
    df = pd.read_csv('statistics_with_entity2.csv')
    print(df)
    X = df[['Positivity Rate','Death Rate' ]]
    kmeans = KMeans(n_clusters=3) 
    kmeans.fit(X)
    labels = kmeans.labels_
    colors = ['red', 'green', 'blue']
    df['Graph_Color'] = [colors[label] for label in labels]
    plt.scatter(df['Positivity Rate'], df['Death Rate'] ,c=df['Graph_Color'])
    centroids = kmeans.cluster_centers_
    plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=200, linewidths=1, color='black')

    # Add labels to the plot
    plt.xlabel('(g)')
    plt.ylabel('Level')
    plt.title('Clustering with K-Means')

    # Show the plot
    plt.show()

def cl2():
    print("cl2")
    df = pd.read_csv('statistics_with_entity2.csv')
    df.head()
    df.info()
    x = df[['Positivity Rate','Death Rate', 'Cases per Population' ]].values
    WCSS = []
    for i in range(1,11):
        model = KMeans(n_clusters = i,init = 'k-means++')
        model.fit(x)
        WCSS.append(model.inertia_)
    fig = plt.figure(figsize = (7,7))
    plt.plot(range(1,11),WCSS, linewidth=4, markersize=12,marker='o',color = 'green')
    plt.xticks(np.arange(11))
    plt.xlabel("Number of clusters")
    plt.ylabel("WCSS")
    plt.show()

    #elbow at 3 add this to the report
    model = KMeans(n_clusters = 3, init = "k-means++", max_iter = 300, n_init = 10, random_state = 0)
    y_clusters = model.fit_predict(x)
    sns.countplot(y_clusters)
    print(x[y_clusters == 0,0][1])
    print(x[y_clusters == 0,1][1])
    print(x[y_clusters == 0,2][1])
    fig = plt.figure(figsize = (15,15))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x[y_clusters == 0,0],x[y_clusters == 0,1],x[y_clusters == 0,2], s = 40 , color = 'blue', label = "cluster 0")
    ax.scatter(x[y_clusters == 1,0],x[y_clusters == 1,1],x[y_clusters == 1,2], s = 40 , color = 'orange', label = "cluster 1")
    ax.scatter(x[y_clusters == 2,0],x[y_clusters == 2,1],x[y_clusters == 2,2], s = 40 , color = 'green', label = "cluster 2")
    ax.set_xlabel('Positivity Rate-->')
    ax.set_ylabel('Death Rate-->')
    ax.set_zlabel('Cases per Population-->')
    ax.legend()
    plt.show()
    

    # 3d scatterplot using plotly
    Scene = dict(xaxis = dict(title  = 'Positivity Rate -->'),yaxis = dict(title  = 'Death Rate--->'),zaxis = dict(title  = 'Cases per Population-->'))

    # model.labels_ is nothing but the predicted clusters i.e y_clusters
    labels = model.labels_
    trace = go.Scatter3d(x=x[:, 0], y=x[:, 1], z=x[:, 2], mode='markers',marker=dict(color = labels, size= 10, line=dict(color= 'black',width = 10)))
    layout = go.Layout(margin=dict(l=0,r=0),scene = Scene,height = 800,width = 800)
    data = [trace]
    fig = go.Figure(data = data, layout = layout)
    fig.show()


if __name__ == '__main__':
    cl2()