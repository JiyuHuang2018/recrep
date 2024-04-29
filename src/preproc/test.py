from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys

# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import numpy.random as npr
from sklearn.cluster import KMeans
from scipy.stats import invgamma

from scipy import sparse, stats

# plt.style.use('ggplot')


# In[2]:


# import seaborn as sns
# sns.set_style("white")
# sns.set_context("paper")

# color_names = ["red",
#                "windows blue",
#                "medium green",
#                "dusty purple",
#                "orange",
#                "amber",
#                "clay",
#                "pink",
#                "greyish",
#                "light cyan",
#                "steel blue",
#                "forest green",
#                "pastel purple",
#                "mint",
#                "salmon",
#                "dark brown"]
# colors = sns.xkcd_palette(color_names)


# In[3]:


DATA_DIR = 'dat/raw/movielens/'


# In[4]:


OUT_DATA_DIR = 'dat/proc/ml_sg/'


# # R3

# In[5]:
raw_file_path = os.path.join(DATA_DIR, 'train_data.csv')
test_file_path = os.path.join(DATA_DIR, 'test_data.csv')
raw_data = pd.read_csv(raw_file_path,usecols=['userId', 'movieId', 'rating'])
test_data = pd.read_csv(test_file_path,usecols=['userId', 'movieId', 'rating'])
print(raw_data.head())