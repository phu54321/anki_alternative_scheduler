#%%

from matplotlib import pyplot as plt
import pandas as pd

#%%

data = pd.read_csv('revlog.csv')
#%%
data[data.time == 60000]
