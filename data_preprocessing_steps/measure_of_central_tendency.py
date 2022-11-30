#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 10:20:19 2022

@author: viswanathareddy
"""

import numpy as np
from scipy.stats import mode

data =  np.asarray([1,2,2,2,4,5,6,6,6,9,10,10,11,14,14,15,18,19,20])

### Mean

#### Arithematic Average of all data point
#### Mean = sum of all points / total number of points

data_mean = np.mean(data)

### Median

#### Described as middle value in a sequence of data points ordered by rank
###  1. Sort the data in increasing order
###  2. if length of the list is odd, then median is the middle value
###  3. if length of the list is even, then take avergae of the two middle values

data_median = np.median(data)

### Mode

#### The datapoints with the highest frequency
#### there can e multiple modes in a dataset
#### In Case of continuos values, it might not be possible to find the mode (Since all the values will be unique)
#### It can be used over non-numerical data as well
data_mode = mode(data)

non_numeric_list = ['q', 'q' ,'a', 'b', 'c','c','c']
mode_non_numerical = mode(non_numeric_list)

##### Mean effected is by extreme data points

data_manipulated = np.append(data, 250)

data_mean_extreme = np.mean(data_manipulated)

data_median_extreme = np.median(data_manipulated)


### Vairance

#### Variance is a measure of how the data points are spread throughout the dataset and how far the data points are from each other
#### Low variance indicates that the data points are close to each other and to the mean
#### High Variance indicates that the data points are far from each other and to the mean
#### Calculated as the average of the square of the distance between each point from the mean

variance = np.var(data)

## Standard Deviation
#### Square root of the variance
#### Is the measure of how much variation from the mean exists

standard_dev = np.std(data)

