# -*- coding: utf-8 -*-
"""Coursera_Foundation_Module2_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1u_ib4pbL_cxJx-rkHFX0egRT9EV5l-kZ

# Launch Pandas
"""

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')

"""# Load house sales data"""

file_path = '/content/drive/MyDrive/CourseraFoundation/Module2/coursera/home_data.csv'
sales = pd.read_csv(file_path)

sales.head()

"""# Explore"""

sales.head()

#sales.summary()

plt.plot(sales[1:201]['sqft_living'],sales[1:201]['price'])

plt.scatter(sales[1:2001]['sqft_living'],sales[1:2001]['price'])

"""# Simple regression model that predicts price from square feet"""

from sklearn.linear_model import LinearRegression

lr_model = LinearRegression()

from sklearn.model_selection import train_test_split

training_set, test_set = train_test_split(sales, train_size=0.8, random_state=24)

"""## train simple regression model"""

x = sales['sqft_living'].to_numpy()
y = sales['price']

lr_model.fit(x.reshape(-1, 1), y)

print(f"w0 = {lr_model.intercept_: .3f}")
print(f"w1 = {lr_model.coef_[0]: .3f}")

yHat = lr_model.predict(x.reshape(-1,1))

"""# Evaluate the quality of our model"""

RSS = np.sum((yHat - y)**2)
print(RSS.shape)

print(f"rss = {RSS:.3f}")

RSS/len(yHat)

from sklearn.metrics import mean_squared_error
rss_sk = mean_squared_error(y, yHat)
print(f"rss_sk = {rss_sk:.3f}")