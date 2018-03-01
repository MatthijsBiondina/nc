from sklearn.metrics import roc_auc_score as auc

#import sklearn.metrics.roc_auc_score as auc

e_file = open('english.scores','r').read()
t_file = open('tagalog.scores','r').read()

eScores = e_file.split()
tScores = t_file.split()

allScores = [-float(i) for i in eScores + tScores]
allLabels = [True for i in range(len(eScores))] + [False for i in range(len(tScores))]

print(eScores)

a = auc(allLabels, allScores)
print(a)


