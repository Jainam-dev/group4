import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

array =  np.random.randint(0,100,20).reshape(2,10)
print(array)

plt.boxplot(array)
plt.show()