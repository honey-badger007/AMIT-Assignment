import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Load the dataset from the tips dataset
df=sns.load_dataset("tips")

#Create a scatter plot using Seaborn to visualize the relationship between total_bill and tip.
#Add different colors for different days of the week.

plt.figure(figsize=(6.4,4.8))
sns.scatterplot(x=df["total_bill"],y=df["tip"],hue=df["day"])
plt.title("Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()

# Create a histogram of the total_bill column using Matplotlib.
plt.figure(figsize=(6.4,4.8))
plt.hist(df["total_bill"], bins=10,color="blue",edgecolor="black")
plt.title("Total Bill Distribution")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()

# - Create a heatmap of the correlation matrix of the numerical columns
#  in the Tips dataset using Seaborn.
df.info()
# show numeric only columns first
numeric_df = df.select_dtypes(include=[np.number])
corr_matrix = numeric_df.corr()

plt.figure(figsize=(6.4,4.8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
# Create a bar plot to show the average tip amount for each day using Seaborn.

plt.figure(figsize=(6.4,4.8))
sns.barplot(x=df["day"],y=df["tip"])
plt.title("Average Tip Amount by Day")
plt.xlabel("Day")
plt.ylabel("Tip")
plt.show()


plt.figure(figsize=(6.4,4.8))
sns.barplot(x=df["day"],y=df["tip"],hue=df["sex"])
plt.title("Average Tip Amount by Day and Sex")
plt.xlabel("Day")
plt.ylabel("Tip")
plt.show()

#Create a line plot to show the trend of tip amount over total_bill using Matplotlib.

plt.figure(figsize=(6.4,4.8))
df_sorted = df.sort_values(by="tip")
plt.plot(df_sorted["tip"],df_sorted["total_bill"])
plt.title("Tip Vs Total Bill")
plt.xlabel("Tip")
plt.ylabel("Total Bill")
plt.show()

# Create a figure with two subplots (1 row, 2 columns).
# In the first subplot, create a scatter plot of total_bill vs tip.
# In the second subplot, create a scatter plot of total_bill vs size.

plt.figure(figsize=(12.8,4.8))
plt.subplot(1,2,1)
plt.scatter(df_sorted["tip"], df_sorted["total_bill"])
plt.title("Tip Vs Total Bill")
plt.xlabel("Tip")
plt.ylabel("Total Bill")
plt.subplot(1,2,2)
plt.scatter(df_sorted["size"], df_sorted["total_bill"])
plt.title("Size Vs Total Bill")
plt.xlabel("Size")
plt.ylabel("Total Bill")
plt.show()

#  Exercise 8: 2x2 Grid of Subplot
# - Plot the following in each subplot:
# - (1, 1): Scatter plot of total_bill vs tip
# - (1, 2): Histogram of total_bill
# - (2, 1): Box plot of total_bill by day
# - (2, 2): lineplot plot of total_bill vs tip

plt.figure(figsize=(12.8,9.6))

plt.subplot(2,2,1)

plt.scatter(df_sorted["tip"], df_sorted["total_bill"])
plt.title("Tip Vs Total Bill")
plt.xlabel("Tip")
plt.ylabel("Total Bill")

plt.subplot(2,2,2)

plt.hist(df_sorted["total_bill"], bins=10,edgecolor="black")
plt.title("Histogram of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")

plt.subplot(2,2,3)

sns.boxplot(y=df["total_bill"],hue=df["day"],palette="flare")
plt.title("Boxplot of Total Bill by Day")
plt.xlabel("Total Bill")
plt.ylabel("Day")

plt.subplot(2,2,4)

df_sorted["tip_per_person"] = df_sorted["tip"] / df_sorted["size"]
plt.plot(df_sorted["tip_per_person"], df_sorted["total_bill"])
plt.title("Tip per Person Vs Total Bill")
plt.xlabel("Tip per Person")
plt.ylabel("Total Bill")
plt.show()
         
# Exercise 9: Customizing Subplot:
# - Plot the following in each subplot:
# - (1, 1): Line plot of total_bill vs tip
# - (2, 1): Bar plot of the average tip amount for each day
# - (3, 1): Heatmap of the correlation matrix

plt.figure(figsize=(12.8,9.6))
plt.subplot(3,1,1)
plt.plot(df_sorted["tip"], df_sorted["total_bill"])
plt.title("Tip Vs Total Bill")
plt.xlabel("Tip")

plt.subplot(3,1,2)
sns.barplot(x=df["day"],y=df["tip"],hue=df["day"],palette="flare")
plt.title("Average Tip Amount for Each Day")
plt.xlabel("Day")
plt.ylabel("Tip")

plt.subplot(3,1,3)

numeric_df = df.select_dtypes(include=[np.number])
corr_matrix = numeric_df.corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()


