import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df_titles = pd.read_csv('titles.csv', low_memory=False)

# Предварительная обработка данных

# Удаление фильмов, набравшие мало голосов в IMDB.

print(df_titles['imdb_id'])