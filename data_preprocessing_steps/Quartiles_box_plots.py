#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 14:40:25 2022

@author: viswanathareddy
"""

import numpy as np
import pandas as pd
import seaborn as sns

data =  np.asarray([1,2,2,2,4,5,6,6,6,9,10,10,11,14,14,15,18,19,20, 50])

quartile_25 = np.percentile(data, 25)

quartile_50 = np.percentile(data, 50)

quartile_75 = np.percentile(data, 75)

IQR = quartile_75 - quartile_25

median = np.median(data)

if (quartile_50 == median):
    print('True')
    
    
### Box Plot


df = pd.DataFrame(data, columns=["Sample Data"])
sns.boxplot(df)
