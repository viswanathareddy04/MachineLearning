import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


data =  np.asarray([1,2,2,2,4,5,6,6,6,9,10,10,11,14,14,15,18,19,20, 50])
print(data)

sns.displot(data, kde=True, bins=5)
plt.xlabel('Intervals')
plt.ylabel('Frequency')
plt.show()

sns.displot(data, kde=False, bins=10)
plt.xlabel('Intervals')
plt.ylabel('Frequency')
plt.show()