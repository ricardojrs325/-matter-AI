
import matplotlib.pyplot as plt
s = np.random.random(32000)
plt.hist(s, 30, density=True)
plt.show()
