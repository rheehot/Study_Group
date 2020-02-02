from pandas import DataFrame
from Data import grade_dic
from print_df import print_df

df = DataFrame(grade_dic, index=['노진구', '이슬이', '비실이', '퉁퉁이', '도라에몽'])

# print_df(df)

# 행의 모든 값이 결측치 일시 행을 삭제
null_data_del = df.dropna(how='all')

print_df(null_data_del)
