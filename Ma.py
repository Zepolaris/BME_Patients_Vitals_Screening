#基于yourself.py小Demo的深入图像画法
#运用matplotlib,pandas

import matplotlib.pyplot as plt
#1.准备数据
ages=[20,25,30,34,35,32,18,66,55,53]
gene_levels=[15,16,34,43,45,23,43,23,46,76]
#2.画图(把点变成粉色，形状为三角形，大小为80)
plt.scatter(ages,gene_levels,color="pink",edgecolors="black",marker='^',s=60)

#3.加标题和坐标轴名字
plt.title("年龄与基因表达量关系图",fontsize=14)
plt.xlabel("年龄(岁)",fontsize=12)
plt.ylabel("基因表达量",fontsize=12)
#4.加网格线
plt.grid(True,linestyle="--",alpha=0.5)
#5.设置x轴刻度和y轴刻度
plt.xticks(range(15,70,5),fontsize=12)
plt.yticks(range(10,80,5),fontsize=12)

#6.显示
plt.savefig("My_first_beautiful_Plot.png",dpi=300)
plt.show()
