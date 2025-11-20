import matplotlib.pyplot as plt
import time
import numpy as np
from sklearn.model_selection import TimeSeriesSplit

def scalabilty_analysis(estimator, X, y, model_name: str):
    """if your data needs scaled for your model, make sure you apply that in a pipeline then use
    pipeline as your estimator. 
    Model name changes title of graph"""
    tt = np.empty((5,5))
    ss = np.array([0.2,0.4,0.6,0.8,1.0])
    for j in range(0,5):
        train_time = []
        tss = TimeSeriesSplit(n_splits = 5)       
        for i, (split_idx, _) in enumerate(tss.split(X, y)):        # creates 5 subsamples at "0.2", "0.4", "0.6", "0.8", "1.0"
            Xs = X.iloc[split_idx,:] 
            ys = y.iloc[split_idx]
            t0 = time.time()
            estimator.fit(Xs, ys[ys.columns[0]])
            train_time.append((time.time() - t0)*1000)
        tt[j,:] = train_time
    avg_tt = tt.mean(axis=0)    
    plt.figure(figsize=(8,6))
    plt.plot(ss, avg_tt, '-o')
    plt.xlabel("Relative Training Sample Size", fontsize=12)
    plt.ylabel("Train Time (ms)", fontsize=12)
    plt.grid()
    plt.title(f"Scalability Analysis of Train Time - {model_name}", fontsize=15)
    plt.show()
