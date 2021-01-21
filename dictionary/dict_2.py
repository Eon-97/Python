'''
딕셔너리의 key로 가능한 데이터 탑입은 int,float,str,tuple 입니다.
# 리스트와 딕셔너리는 key로 사용할 수 없습니다.
'''
my_dict = {
    1 : 'int',
    1.23 : 'float',
    '하나 둘' : 'str',
    (1,2,3) : 'tuple'
}
print(my_dict)
# 결과 : {1: 'int', 1.23: 'float', '하나 둘': 'str', (1, 2, 3): 'tuple'}

'''
딕셔너리의 value에는 모든 데이터 타입을 저장할 수 있습니다.
'''
my_dict2 =  dict(
    key1 = 123, #int
    key2 = 1.23, #float
    key3 = 'str', #str
    key4 = ('tuple',1,2,3), #tuple
    key5 ={'dict':1,'dict2':2}, #dict
    key6 = ['list',1,2,3,] #list
)
print(my_dict2)
# 결과 : {'key1': 123, 'key2': 1.23, 'key3': 'str', 'key4': ('tuple', 1, 2, 3), 'key5': {'dict': 1, 'dict2': 2}, 'key6': ['list', 1, 2, 3]}

'''
딕셔너리 안의 리스트 아이템을 참조할 경우
my_dict2 
'''
print(my_dict2['key6'][0]) #결과-> list
'''
딕셔너리 안의 딕셔너리 아이템을 참조할 경우
my_dict2
'''
print(my_dict2['key5']['dict']) #결과-> 1

# 파이썬 버전 3.6이하의 버전에는 딕셔너리의 순서가 없고, 3.7 이상의 버전에서는 순서가 있습니다.