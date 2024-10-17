import numpy as np
import matplotlib.pyplot as plt
import statistics
from datetime import datetime
maxi = int(1e5)  
QE = 0.23 
dynode_sets = [
    {"dynodes": [0, 150, 300, 450, 600, 750], "label": "Set 1:[0, 150, 300, 450, 600, 750]", "color": "r"},
    {"dynodes": [0, 150, 300, 450, 600, 750, 900], "label": "Set 2: [0, 150, 300, 450, 600, 750, 900]", "color": "g"},
    {"dynodes": [0, 150, 300, 450, 600, 750, 900, 1050], "label": "Set 3: [0, 150, 300, 450, 600, 750, 900,1050]", "color": "b"}
]
xbins = np.linspace(0, 3e6, 101)  
plt.figure(figsize=(10, 6))
for dynode_set in dynode_sets:
    dynodes = dynode_set["dynodes"]
    color = dynode_set["color"]
    label = dynode_set["label"]
    
    dist = []
    print(f"Running simulation for {label}")
    print(datetime.now())

    for i in range(maxi):
        if np.random.uniform() < QE:
            electrons = 1
            for j in range(len(dynodes) - 1):
                mu = electrons * (dynodes[j + 1] - dynodes[j]) / 20
                electrons = electrons + np.random.poisson(mu)
            dist.append(electrons)

    print(datetime.now())
    print(f"The mean of the distribution for {label} was", statistics.mean(dist))
    counts, edges = np.histogram(dist, bins=xbins)
    spacing = (edges[1] - edges[0]) / 2
    centres = edges[1:] - spacing
    plt.semilogy(centres, counts, color=color, marker='o', linestyle='-', label=label)
plt.xlim((0, 3e6))
plt.ylim((0.8, 10000))
plt.xlabel('Number of Anode Electrons')
plt.ylabel('Counts (log scale)')
plt.title('Semilogy Plot for Different Dynode Potentials')
plt.legend(title='Dynode Potential Sets')
plt.show()

