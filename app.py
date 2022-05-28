import os
import numpy as np
import pandas as pd

#Importing Visualization libraries
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt

#Importing Classes from the python files
from information import Information
from preprocessing import Pre_Processing
from plots import Plots
from visualization import Visualization
from kMeansClustering import KMeans_clustering

#Importing from flask 
from flask import Flask, render_template, request, send_file
import jsonify
import requests
from flask import Response

PEOPLE_FOLDER = os.path.join('static', 'sub')

df= pd.read_csv('cars.csv')
df["Ex-Showroom_Price"] = df["Ex-Showroom_Price"].str.replace(r'.* ([\d,]+)+$', r'\1',regex=True).str.replace(',', '',regex=True).astype('int32')


app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

@app.route("/information")
def information():
    data=Information(df)
    dataset_shape,dataTypes,data_head,data_tail,data_describe=data.info()
    total_missing,missing_value,percentage_missing_value = data.total_missing_values()
    data2=Pre_Processing(df,percentage_missing_value)
    drop_head=data2.drop_column()
    fill_head=data2.fill_missing_values()
    dummy=data2.dummies()
    return render_template('index.html',shape=dataset_shape,dtypes=dataTypes,head=[data_head.to_html(classes='HEAD')],
    tail=[data_tail.to_html(classes='TAIL')],desc=[data_describe.to_html(classes='HEAD')],
    totalMis=total_missing,MisVal=missing_value,cent=percentage_missing_value,
    dhead=[drop_head.to_html(classes='DHEAD')],fhead=[fill_head.to_html(classes='FHEAD')],dum=[dummy.to_html(classes='DHEAD')])

data=Information(df)
total_missing,missing_value,percentage_missing_value = data.total_missing_values()
data2=Pre_Processing(df,percentage_missing_value)
drop_head=data2.drop_column()
fill_head=data2.fill_missing_values()

@app.route("/plots",methods=['POST'])
def plots():
    if request.method=="POST":
        col=request.form['Column']
        data=Plots(df,col)
        fig=data.bar_plot()
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'bar.png')
        return render_template("index.html", a = full_filename)

@app.route("/boxPlot",methods=['POST'])
def boxPlot():
    if request.method=="POST":
        cl=request.form['Col']
        data=Plots(df,cl)
        fig=data.box_plot()
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'box.png')
        return render_template("index.html", b = full_filename)


@app.route("/barPlot",methods=['POST'])
def barPlot():
    if request.method=="POST":
        x=request.form['x']
        y=request.form['y']
        data = Visualization(df,x,y)
        fig=data.bar_chart()
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'bar2.png')
        return render_template("index.html", c = full_filename)

@app.route("/scatterPlot",methods=['POST'])
def scatterPlot():
    if request.method=="POST":
        x=request.form['xAxis']
        y=request.form['yAxis']
        data = Visualization(df,x,y)
        fig=data.scatter_chart()
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'scatter2.png')
        return render_template("index.html", d= full_filename)

@app.route("/optimalK")
def optimalK():
    data=KMeans_clustering(df)
    scaled_feature=data.scaling_features()
    fig=data.sum_square_error()
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'elbowPlot.png')
    g=data.kmean()
    file = os.path.join(app.config['UPLOAD_FOLDER'], 'clustering.png')
    return render_template("index.html", scaled=[scaled_feature.to_html(classes='SHEAD')], e= full_filename,f= file)

if __name__ == '__main__':
    app.run(debug = True)
