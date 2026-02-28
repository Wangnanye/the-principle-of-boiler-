import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['mathtext.fontset']='cm'
plt.rcParams['font.family']='serif'
plt.rcParams['font.serif']='Times New Roman'
df = pd.read_csv("D:\Wuhan Unniversity of Techonology\大四\毕业设计\吹灰优化\阳逻电厂数据\吹灰DCS数据\蒸汽吹灰开始\OPSRV^TNT^5HSFSTEP3.CSV")
time=df['t']
value=df['value']
plt.figure(figsize=(12, 6))
plt.xlim(0,168)
plt.ylim(0,1)
for i in time:
    plt.axvline(x=i, linestyle='--',color='black',linewidth=0.5)
plt.title('Soot-blower signal')
plt.xlabel('t')
plt.ylabel('signal')
plt.legend()
plt.show()