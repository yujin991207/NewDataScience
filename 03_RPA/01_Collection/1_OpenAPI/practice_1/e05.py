# {'id':일련번호, 'sido_name':시도명, 'sigungu_name':시군구명, 'remarks':대피지구명,
# 'shel_nm':대피장소명, 'address':주소, 'lon':경도, 'lat':위도, 'shel_av':수용가능인원수,
# 'lenth':해변으로부터거리, 'shel_div_type':대피소 분류명, 'seismic':내진적용여부, 'height':해발높이}

# 열순서변경
# ['일련번호','시도명','시군구명','대피지구명','대피장소명','주소','수용가능인원수','대피소 분류명',''해변으로부터거리,'내진적용여부','해발높이','경도','위도']

import pandas as pd

file_name = '지진해일_긴급대피장소.csv'

df = pd.read_csv(file_name)

rename_dict = {'id':'일련번호', 'sido_name':'시도명', 'sigungu_name':'시군구명', 'remarks':'대피지구명',
               'shel_nm':'대피장소명', 'address':'주소', 'lon':'경도', 'lat':'위도', 'shel_av':'수용가능인원수',
               'lenth':'해변으로부터거리', 'shel_div_type':'대피소 분류명', 'seismic':'내진적용여부', 'height':'해발높이'}
df.rename(columns = rename_dict, inplace = True)

df = df[['일련번호','시도명','시군구명','대피지구명','대피장소명','주소','수용가능인원수',
         '대피소 분류명','해변으로부터거리','내진적용여부','해발높이','경도','위도']]

print(df)