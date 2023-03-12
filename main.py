import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

price = [1.45,0.9,2.1,4.6,4.5,5.6,0.8,5.36889929,0.85,3,12,0.5,5,4.5,2.55,7,17,4,3.5,6.297712,1.5,4.9419,8,10,0.6,0.42,0.7,2,2,0.49080461,0.44777,1.42,0.52514935,0.85,1.2,8,63.5,7,5.208,3.129,4.92865082,3.4,1.5,0.75,4.92446839,6,0,5.2]
"""
绘制水平条形图方法barh
参数一：y轴
参数二：x轴
"""
plt.barh(range(48), price, height=0.7, color='steelblue', alpha=0.8)      # 从下往上画
plt.yticks(range(48), ['台泥','亞泥','統一','台塑','南亞','台化','遠東新','亞德客-KY','中鋼','正新','和泰車','聯電','台達電','鴻海','國巨','台積電','華碩','瑞昱','廣達','研華','南亞科','中華電','聯發科','可成','台灣高鐵','彰銀','華南金','富邦金','國泰金','玉山金','元大金','兆豐金','台新金','中信金','第一金','統一超','大立光','聯詠','台灣大','遠傳','和碩','中租-KY','上海商銀','合庫金','矽力-KY','台塑化','南電','豐泰'])
plt.xlim(0,66)
plt.xlabel("盈餘分配之股東現金股利(元/股)")
plt.title("2017年各公司股東現金股利分配情况")
for x, y in enumerate(price):
    plt.text(y + 0.2, x - 0.1, '%s' % y)
plt.show()