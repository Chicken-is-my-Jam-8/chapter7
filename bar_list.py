import matplotlib.pyplot as plt


colors = ['r','g','b','w','k']

yp = [100, 200, 300, 400, 500]
xp = [0, 10, 20, 30, 40]
bar_width = 10


plt.bar(xp, yp, bar_width, color = colors)


plt.xticks([5, 15, 25, 35, 45],
           ['2016', '2017', '2018', '2019', '2020'])
plt.yticks([0, 100, 200, 300, 400, 500],
           ['$0m','$1m','$2m','$3m','$4m','$5m',])

plt.xlabel("Year")
plt.ylabel("Sales")

plt.title("Sales by Year")
plt.show()
