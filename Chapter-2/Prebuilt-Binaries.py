import numpy as np
import matplotlib.pylab as plt

# แสดงกราฟกำลัง 2
t = np.linspace(0, 1, 100)
plt.plot(t, t**2)
plt.show()

# แสดงกราฟ square root
plt.plot(t, t**0.5)
plt.show()