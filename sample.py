import pandas as pd
input_file='D:\Wuhan Unniversity of Techonology\大四\毕业设计\吹灰优化\阳逻电厂数据\吹灰DCS数据\低再蒸汽进口\OPSRV^TNT^5HAJ10CT002.txt'
output_file='D:\Wuhan Unniversity of Techonology\大四\毕业设计\吹灰优化\阳逻电厂数据\吹灰DCS数据\低再蒸汽进口\OPSRV^TNT^5HAJ10CT002.csv'
try:
    df=pd.read_csv(input_file,sep='\t',encoding='utf-8')
    sampled_df=df.iloc[::300]
    sampled_df.to_csv(output_file,index=False,encoding='utf-8-sig')
except Exception as e:
    print(f"出错了: {e}")