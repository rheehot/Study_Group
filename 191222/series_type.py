# pandas 모듈에서 series 클래스 가져오기
from pandas import Series

# 기본 시리즈 만들기
# 리스트를 통해 만들 수 있다.
# 즉, 리스트 자료형을 가공하여 생성된 데이터 구조
items = [10, 30, 50, 70, 90]
column = Series(items)

# 타입을 확인
print(type(column))
print(type(column.values))
