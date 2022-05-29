# cars-engage-2022

# Data Analysis

>Developed an application to demonstrate how the Automotive Industry could harness data to take informed decisions.

> Live demo [here](https://youtu.be/0lu2atR5Qcg)

## Table of Contents
* [Objective](#objective)
* [Why this Project?](#why-this-project)
* [General Information about the Project](#general-information-about-the-project)
* [How to use the web application?](#how-to-use-the-web-application)
* [Technologies Used](https://github.com/Shweta2024/cars-engage-2022/blob/main/requirements.txt)
* [Features](#features)
* [Room for Improvement](#room-for-improvement)
* [Installing/Contributing Guidelines](https://github.com/Shweta2024/cars-engage-2022/blob/main/Contributing.md)
* [Contact](#contact)




# Objective

- The ultimate goal of this project is to develop an application that the Automotive Industry could use to harness data to make informed decisions. 
- It helps to find out which is the most popular car **on the basis** of its engine type, fuel type, mileage, model, etc. 
- It will help them to figure out the trending designs of cars and can use those reports to accordingly **manipulate the design of the cars**,by making them more      **optimized, customer-centric, and innovative**. 
- It also allows them to **find out the relation between** different parameters like how exactly the prices vary with the independent variables. With the help of **customer segmentation**, they can find which group of people prefers which features.

# Why this Project?

Quick and accurate analysis of data is something that cannot be neglected in the automotive industry. The scale of data that is available to us is huge and it is tedious to find out reports from it manually, also there are chances of making errors while calculating. All these complexities make the traditional quantitative approaches to analysis inappropriate.  This led to the need for the development of this application, with the help of Machine Learning concepts, we can easily **find out the variations of one feature with respect to others accurately in a very less time.**

# General Information about the Project

This project uses the concept of Data Analysis to demonstrate how the Automotive Industry could harness data to make informed decisions.

I have used this Dataset->[cars](https://github.com/Shweta2024/cars-engage-2022/blob/main/cars.csv)

- Since the given dataset had missing values, I deleted the columns having more than 60% missing values.

- Followed by filling the missing values with the mode of the column.

- Then, **I used plots such as** : bar plots, box plots, and scatter plots to display the relationship between different attributes(features of the cars).

- Followed by using an Elbow plot to find the optimal value of K to apply **K-Means Clustering** ,so as  to group the people on the basis of the Displacement and the Ex-Showroom Price

- Prior to using K-means Clustering, I scaled the values of Displacement and Ex-showroom Price, for making data points generalized so that the distance between them will be lower.
 

--------------

- The below table shows the statistical summary of the dataframe given dataframe. 
- It includes count, mean, median (or 50th percentile) standard variation, minimum value,maximum value, and percentile values of columns. 

![statistical-result](https://user-images.githubusercontent.com/75883328/170816874-23d68a19-f346-46a0-8a7f-3f135c2e587e.png)

--------------
 
- The below Bar Plot represents the top 10 popular Make of Cars.
- Maruti Suzuki is the most popular Make ,followed by Hyundai ,Mahindra,Tata and so on.
- Skoda and Ford are having equal count,
- Bmw and Renault are having nearly equal count,
![image](https://user-images.githubusercontent.com/75883328/170739247-83b990a5-0903-4479-8fd2-dce66650b826.png)

--------------

- The below Bar Plot represents the top 10 popular Models of Cars.
- Nexon is a the top model and a tough competitor of Kuv100 Nxt. 
- Compass and Xuv500 are having equal count.
- Seltos and Innova crysta are having equal count. 
- Ciaz and Swift are having equal count.
![image](https://user-images.githubusercontent.com/75883328/170739378-a9086d13-0555-4059-848f-c0156497344d.png)

--------------

- The below Bar Plot represents popular Types of Cars.
- Manual Cars are prefered over Automatic ,AMT,DCT and CVT.
![image](https://user-images.githubusercontent.com/75883328/170739410-aa8ec711-93df-4a52-be4b-aa0ac1ad80bf.png)

--------------

- The below Bar Plot represents popular Fuel Types of Cars.
- Cars running on Petrol and Diesel are more as compared to those running on CNG,Hybrid,Electric and CNG+Petrol.
-  CNG,Hybrid and Electric are having equal count.
![image](https://user-images.githubusercontent.com/75883328/170739441-c5197a85-f822-4a1f-9112-ef20ac943aed.png)

--------------

- The below Bar Plot represents the top 10 popular Body Type of Cars.
- SUV is the most popular body type.
- Coupe,MUV and MPV are having equal count.
![image](https://user-images.githubusercontent.com/75883328/170739554-d3f3ba43-c24f-40c7-a8ca-8e4e9c307a7a.png)

--------------

- The below Box plot represents that Renault is having the heighest Ex-showroom Price and median.
- Tata is having the lowest Ex-showroom Price and median.
- Renault is the most prefered Make by the middle 50% sample of the dataset.
![image](https://user-images.githubusercontent.com/75883328/170742559-9d65e19a-769b-4386-bd85-b098cf7361ed.png)

--------------

- The below Box plot represents that the Ex-showroom Price of Automatic cars are higher than Manual cars.
- The middle 50% sample of the given dataset prefers Manual over Automatic cars. 
![image](https://user-images.githubusercontent.com/75883328/170742134-c3c627fe-444f-46c8-95b8-17802b9585c1.png)

--------------

- The below Box plot represents that the Ex-showroom Price of Kwid Model is highest.
- The middle 50% sample of the given dataset does not prefers Alto K10.
- Nano Genx is having the least Ex-showroom Price.
![image](https://user-images.githubusercontent.com/75883328/170742643-8df51f2b-97cf-45d4-acbd-7e2304bb87d1.png)

--------------

- The below Box plot represents that cars running on Petrol are most prefered. 
![image](https://user-images.githubusercontent.com/75883328/170742200-92b87cd6-9c75-4273-aff3-e1747a0912c5.png)

--------------


![image](https://user-images.githubusercontent.com/75883328/170742734-a28e5f42-da26-4cd7-9f4e-c2115a6062cb.png)


--------------

- The below Box plot represents that Hatchback Body type is prefered over the MPV Body Type by the middle 50% sample of the given dataset.. 

![image](https://user-images.githubusercontent.com/75883328/170742233-734ffcf3-6565-498a-af08-56a4a465d3f8.png)

--------------

- The below Bar plot shows that Renault is having the heighest Ex-Showroom Price.
- Maruti Suzuki is a tough competitor of Renault.
![image](https://user-images.githubusercontent.com/75883328/170739837-dfc961ed-5a7c-4777-9f84-931ce64b2a9a.png)

--------------

- City Mileage of Manual is heigher as compared to Automatic cars. 
![image](https://user-images.githubusercontent.com/75883328/170740037-5f2e5f54-4658-4226-86a8-30e0f7470f97.png)

--------------

- Eeco has the heighest Displacement.
- Redi-Go ,Kwid Model and Alto K10 are having nearly equal Displacement. 

![image](https://user-images.githubusercontent.com/75883328/170740121-5e1ab48b-2279-4985-ba42-e37ac3e62e5c.png)

--------------

![image](https://user-images.githubusercontent.com/75883328/170741497-8d01bf96-4950-4b20-babd-5dd7ba318d21.png)

--------------

![image](https://user-images.githubusercontent.com/75883328/170741403-bf221233-9721-4060-a109-f96e8688d62d.png)

--------------

- This is an Elbow Plot and is used to find the optimal value of k ,for k-Means Clustering.
- Since the elbow is formed at k=3,therefore the optimal value of k is 3 .i.e. we'll have 3 clusters.

![image](https://user-images.githubusercontent.com/75883328/170740608-a97d601b-05da-483f-b2a3-ba001acb3b9b.png)

--------------

- The below scatter plot represents the 3 clusters formed by considering Displacement and Ex-Showroom Price for K-Means Clustering.

![image](https://user-images.githubusercontent.com/75883328/170741261-33c584b7-117d-482f-bb96-7a8201b8d7ec.png)


## How to use the web application?

>Click on this link :- [Information & Visualization](https://cars-engage-2022.herokuapp.com/information)

The above link directs to the an interface where you can check the following information about the dataset :- 
- The number of rows and columns.
- The datatype of each columns.
- The number and percentage of missing values in each columns.
- Head and tail of the dataframe.
- Statistical description.
- Box plots,bar plots and scatter plots between different columns ,so as to understand their relation.

>Click on this link :- [Customer Segmentation](https://cars-engage-2022.herokuapp.com/optimalK)

The above link directs to the an interface where you can check the following information :-
- The head of the dataframe after scaling Displacement and Ex-Showroom Price.
- Elbow Plot(used to find the optimal value of k).
- Scatter plot between Displacement and Ex-Showroom Price (after using K-means clustering).


## Features

Below are the informations that can be found from my application :- 

- The most popular Car as per their Make , Model,Fuel Type ,Body Type, etc.
- How exactly the prices vary with the independent variables.
- Customer segments.





## Room for Improvement

- Since the aim of the project was to use data analysis,I have not used any algorithm to predict the price of a car.Although, algorithms like **Linear Regression** and  **Random Forest Algorithm** can be used for predicting the price of the car. 



## Contact

😄 Created by - [Shweta Bhagat](https://www.linkedin.com/in/shweta-bhagat-5a3969200/)

📧 Email : bhagatshweta0216@gmail.com

Feel free to contact me!

<p align="center">
<img src ="https://user-images.githubusercontent.com/75883328/170819712-4aca091e-43e1-4aa4-a038-f7771cd93737.gif"/>
</p>


