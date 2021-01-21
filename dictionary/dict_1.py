'''
1. 딕셔너리는 리스트와 함께 가장 많이 쓰이는 데이터 스트럭쳐 중 하나입니다.
2. 딕셔너리는 key , value 매핑을 사용하여 데이터를 저장합니다.
3. 딕셔너리는 순서가 없는 데이터 타입입니다 
'''
# 딕셔너리의 기본 생김새

# 컬리 브레이스를 사용하여 정의

my_dict = {}
print(type(my_dict)) #결과 : <class 'dict'>
# 딕셔너리의 아이템은 key : value 형식을 갖고 :으로 구분됩니다 그리고 아이템과 아이템의 사이는 ,로 구분됩니다.
person = {
    'first_name' : 'miyeon' ,
    'last_name' : 'choi',
    'age' : 25
}
print(person)
# -> 결과 : {'first_name': 'miyeon', 'last_name': 'choi', 'age': 25}

# dict() 컨스트럭쳐를 사용하여 정의
'''
dict() 컨스트럭쳐를 사용할 때 변수에 데이터를 할당하듯 = 을 사용합니다 
'''
person_2 = dict(
    first_name = 'sojung' ,
    last_name = 'you',
    age = 29
)
print(person_2)
# -> 결과 : {'first_name': 'miyeon', 'last_name': 'choi', 'age': 25}


# value 값 변경
print(person['age']) # 변경 전 결과 : 25

person['age'] = 100
print(person['age']) # 변경 후 결과 : 100



# 아이템 추가 
person['job'] = 'programmer'
print(person)
# 결과 : {'first_name': 'miyeon', 'last_name': 'choi', 'age': 100, 'job': 'programmer'}

# del 을 사용하여 아이템 삭제
del person['job']
print(person)
# 결과 : {'first_name': 'miyeon', 'last_name': 'choi', 'age': 100}