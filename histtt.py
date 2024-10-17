import numpy as np
import matplotlib.pyplot as plt
import statistics
from datetime import datetime
maxi = int(1e5)
dynode = [0,50,100,150,200,250,300]
xbins = np.linspace(0,10000, 101)
configurations = [
    {"N": 2363, "QE": 0.12, "color": "r", "label": "N=2363, QE=0.12"},
    {"N": 1543, "QE": 0.12, "color": "g", "label": "N=1543, QE=0.12"},
    {"N": 2363, "QE": 0.55, "color": "b", "label": "N=2363, QE=0.55"},
    {"N": 1543, "QE": 0.55, "color": "k", "label": "N=1543, QE=0.55"}
]
plt.figure(figsize=(10, 6)) 
for config in configurations:
    N = config["N"]
    QE = config["QE"]
    color = config["color"]
    label = config["label"]
    pe = 0
    for i in range(N):
        if np.random.uniform() < QE:
            pe += 1
    dist = []
    print(f"Running simulation for {label}")
    print(datetime.now())
    for i in range(maxi):
        if np.random.uniform() < QE:
            electrons = 1
            for j in range(len(dynode) - 1):
                mu = electrons * (dynode[j + 1] - dynode[j]) /20
                electrons = electrons + np.random.poisson(mu)
            dist.append(electrons)
    print(datetime.now())
    print(f"The fraction of trials that produced a photoelectron is {len(dist) / maxi}")
    print(f"The mean of the distribution was {statistics.mean(dist)}")
    plt.hist(dist, bins=xbins, color=color, histtype='step', label=label, linewidth=2)
plt.xlim((0, 10000))
plt.ylim((0, 7500))
plt.xlabel('Number of Anode Electrons')
plt.ylabel('Count')
plt.title('Comparison of Distributions for Different N and QE Values (V=20)')
plt.legend()
plt.show()

