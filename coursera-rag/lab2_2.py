import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
import matplotlib.pyplot as plt
import joblib
import os

from sklearn.datasets import fetch_20newsgroups

# Load the 20 Newsgroups dataset
newsgroups_train = fetch_20newsgroups(subset='train', shuffle=True, random_state=42, data_home='./dataset')

# Convert the dataset to a DataFrame for easier handling
df = pd.DataFrame({
    'text': newsgroups_train.data,
    'category': newsgroups_train.target
})

# Display some basic information about the dataset
print(df.head())
print("\nDataset Size:", df.shape)
print("\nNumber of Categories:", len(newsgroups_train.target_names))
print("\nCategories:", newsgroups_train.target_names)