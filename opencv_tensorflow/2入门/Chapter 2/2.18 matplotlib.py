import numpy as np
import matplotlib.pyplot as plt

x = np.array(range(1, 9))
y = np.array([3, 5, 7, 10, 2, 6, 9, 12])

# 折线 plt.plot(x, y, color, lw=可选 ,)
plt.plot(x, y, "r", lw=10)
plt.show()

# 折线 柱状 饼状
# plt.plot(x, y, "r")
# plt.bar(x, y, %lw, alpha=透明度[0, 1], color=颜色)
plt.bar(x, y, 0.5, alpha=0.5, color="g")
plt.show()


