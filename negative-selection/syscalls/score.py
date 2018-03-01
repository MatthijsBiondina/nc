import pandas as pd

labels = pd.read_csv('snd.labels')
idx = pd.read_csv('snd.test.index')
# pred = pd.read_csv('snd.scores')
idx.columns = ['index']
pred.columns = ['pred']
df = pd.concat([pred, idx])
means = df.groupby('index').mean()

from sklearn.metrics import roc_auc_score as auc

a = auc(labels, means)
print(a)

