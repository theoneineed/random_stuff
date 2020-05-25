import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

data = {'A': [45,37,42,35,39],
        'B': [38,31,26,28,33],
        'C': [10,15,17,21,12]
        }

df = pd.DataFrame(data,columns=['A','B','C'])

covMatrix = pd.DataFrame.cov(df)
sn.heatmap(covMatrix, annot=True, fmt='g')
plt.show()
