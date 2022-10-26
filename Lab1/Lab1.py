import matplotlib.pyplot as plt
import numpy as np

#создание окна, в котором будет выводится график
fig, ax = plt.subplots()
#задание промежутка
x = np.linspace(-5, 5, 21)
#задание функции
y = x ** 2
#построение графика
ax.plot(x,y)
plt.show()
