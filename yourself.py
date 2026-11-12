import pandas as pd

def analyze_vitals(file_path):
    count=0
    #用pandas读取真实的CSV文件
    df=pd.read_csv(file_path)
    print("---开始分析患者数据---")
    #遍历Pandas表格
    for index,patient in df.iterrows():
        temp=patient["temp"]
        name=patient["name"]
        heart_rate=patient["heart_rate"]
        if(temp>=37.5):
            print(f"警告！{name}发热！(┳Д┳)")
            count+=1
        if(heart_rate>=100):
            print(f"警告！{name}心率过快！o(╥﹏╥)o")
            count+=1

#筛选异常数据
    abnormal_df=df[(df["temp"]>=37.5)|(df["heart_rate"]>=100)]
    abnormal_df.to_csv("abnormal_report.csv",index=False,encoding='utf-8-sig')
    print("异常数据已成功导出至abnormal_report.csv文件！ヽ(*≧ω≦)ﾉ")
    return count
total=analyze_vitals("patients.csv")
print(f"总计发现{total}人体征异常")