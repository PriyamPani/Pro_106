import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Days ", y="Marks ")
        fig.show()

def getDataSource(data_path):
    marks = []
    days_present = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    return {"x" : marks, "y": days_present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation  :->",correlation[0,1])

def setup():
    data_path  = "Student Marks vs Days Present.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()