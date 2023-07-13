import matplotlib.pyplot as plt

# x1 = [2,4,5,6]
# y1 = [2,3,6,7]

# x2 = [1,2,3,4]
# y2 = [1,2,4,4]

left = [1,2,3,4]
height = [10,11,23,36,4]
tick_label = ['one','two','three','four','five']

plt.bar(left,height, tick_label=tick_label, width=0.8, color = ['Blue', 'Orange'])

# plt.plot(x1,y1, label = 'Line 1', color = 'Blue', linestyle = 'dashed', linewidth = 3, marker = '*', markerfacecolor = 'Green')
# plt.plot(x2,y2, label = 'Line 2', color = 'Green', linewidth = 3, marker = 'o', markerfacecolor = 'Blue', markersize = 12)
plt.title('Sample graph')
plt.xlabel('X axis')
plt.ylabel('Y axis')
# plt.legend()
plt.show()