import matplotlib.pyplot as plt

x_list = list(range(1))
y1_list = [22, 35, 35, 23, 45, 23]
y2_list = [24, 25, 35, 46, 34, 23]
plt.title('Рисунок')
plt.xlabel('')
plt.ylabel('')
plt.plot(x_list, y1_list, label="1", marker='^')
plt.plot(x_list, y2_list, label="2", marker='o')
#plt.bar
plt.legend()
plt.show()