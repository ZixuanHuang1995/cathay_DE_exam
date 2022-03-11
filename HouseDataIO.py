import pandas as pd
import re

#Extract data
df_a = pd.read_csv('~/Desktop/cathay_DE_exam/dataset/a_lvr_land_a.csv', encoding='utf-8').drop([0])
df_b = pd.read_csv('~/Desktop/cathay_DE_exam/dataset/b_lvr_land_a.csv', encoding='utf-8').drop([0])
df_e = pd.read_csv('~/Desktop/cathay_DE_exam/dataset/e_lvr_land_a.csv', encoding='utf-8').drop([0])
df_f = pd.read_csv('~/Desktop/cathay_DE_exam/dataset/f_lvr_land_a.csv', encoding='utf-8').drop([0])
df_h = pd.read_csv('~/Desktop/cathay_DE_exam/dataset/h_lvr_land_a.csv', encoding='utf-8').drop([0])

#Transform data
df_all = pd.concat([df_a, df_b, df_e, df_f, df_h],axis=0) #合併dataframe
Less13FArray = ['一層', '二層', '三層', '四層', '五層', '六層', '七層', '八層', '九層', '十層', '十一層', '十二層']
filter_a_df = df_all.query("主要用途 == '住家用' & 建物型態.str.contains('住宅大樓') & 總樓層數 not in @Less13FArray & 總樓層數.notnull()")
filter_b_df = pd.DataFrame(columns=['item','result'])
filter_b_df.loc[0] = ['總件數', len(df_all.index)]
ParkingCount = 0
for row in df_all['交易筆棟數']:
    numbers = [float(s) for s in re.findall(r'-?\d+\.?\d*', row)]
    ParkingCount += numbers[2]
filter_b_df.loc[1] = ['總車位數', ParkingCount]
filter_b_df.loc[2] = ['平均總價元', pd.to_numeric(df_all['總價元']).mean()]
filter_b_df.loc[3] = ['平均車位總價元', pd.to_numeric(df_all['車位總價元']).mean()]

#Load data
filter_a_df.to_csv("~/Desktop/cathay_DE_exam/output/filter_a.csv", index = False) #輸出filter_a.csv
filter_b_df.to_csv("~/Desktop/cathay_DE_exam/output/filter_b.csv", index = False) #輸出filter_b.csv