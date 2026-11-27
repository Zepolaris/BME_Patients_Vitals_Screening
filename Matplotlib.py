#基于yourself.py小Demo的深入图像画法
#运用matplotlib,pandas


import matplotlib.pyplot as plt
#必须加，防止中文变方块
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

#准备画布（散点图）
plt.figure(figsize=(12,8))
#1.准备数据
ages=[20,22,24,26,28,30,32,34,36,38,]
gene_levels=[15,22,25,33,38,45,47,50,53,57]
#2.画图(把点变成粉色，形状为三角形，大小为80):散点图
plt.scatter(ages,gene_levels,color="pink",edgecolors="black",marker='^',s=60)
#3.加标题和坐标轴名字
plt.title("年龄与基因表达量关系图",fontsize=14)
plt.xlabel("年龄(岁)",fontsize=12)
plt.ylabel("基因表达量",fontsize=12)
#4.加网格线
plt.grid(True,linestyle="--",alpha=0.5)
#5.设置x轴刻度和y轴刻度
plt.xticks(range(15,50,5),fontsize=12)
plt.yticks(range(10,70,5),fontsize=12)
plt.savefig("Ma_scatter.png",dpi=300)

#柱状图
plt.figure(figsize=(12,8))
#1.准备数据
groups=["男性患者","女性患者","儿童患者"]
avg_temps=[180.2,162.3,145.6]
#2.画图
plt.bar(groups,avg_temps,color="red",width=0.5)
#3
plt.title("不同人群身高对比",fontsize=14)
plt.xlabel("患者分类",fontsize=12)
plt.ylabel("平均身高(cm)",fontsize=12)
plt.grid(True,linestyle="--",alpha=0.5)
plt.savefig("Ma_bar.png",dpi=300)

#折线图
plt.figure(figsize=(12,8))
#1.准备数据
days=["周一","周二","周三","周四","周五","周六","周天"]
temp=[36,37.5,38.2,38.8,36.8,36.5,36.2]
#2.画图
plt.plot(days,temp,color="blue",marker='o',linewidth=2)
#3.坐标
plt.title("患者一周体温变化趋势",fontsize=14)
plt.xlabel("日期",fontsize=12)
plt.ylabel("体温(℃)",fontsize=12)
plt.grid(True,linestyle="--",alpha=0.5)

plt.savefig("Ma_plot.png",dpi=300)
plt.show()

