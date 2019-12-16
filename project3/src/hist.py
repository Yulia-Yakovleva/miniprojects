import matplotlib.pyplot as plt
import seaborn as sns

with open('../data/31mer_hist_corrected.txt') as f:
    lines = f.read().splitlines()
    vs = [int(line.split(' ')[1]) for line in lines]

sns.set(style="whitegrid")
plt.plot(vs)

plt.yscale('log')
plt.xlabel('bin id')
plt.ylabel('frequency')
plt.savefig('../figs/hist_31_corrected.png', dpi=150)
plt.show()
