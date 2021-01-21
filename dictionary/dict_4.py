my_dict3 =  dict(
    key1 = 123, #int
    key2 = 1.23, #float
    key3 = 'str', #str
    key4 = ('tuple',1,2,3), #tuple
    key5 ={'dict':1,'dict2':2}, #dict
    key6 = ['list',1,2,3,] #list
)
'''
# items()
items 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 객체로 돌려줍니다
'''
print(my_dict3.items())
# 결과 -> dict_items([('key1', 123), ('key2', 1.23), ('key3', 'str'), ('key4', ('tuple', 1, 2, 3)), ('key5', {'dict': 1, 'dict2': 2}), ('key6', ['list', 1, 2, 3])]
'''
# values()
values 함수를 이용하여 딕셔너리의 value값만  (리스트로)  dict_values 객체로 돌려줍니다.
'''
print(my_dict3.values())
# 결과 -> dict_values([123, 1.23, 'str', ('tuple', 1, 2, 3), {'dict': 1, 'dict2': 2}, ['list', 1, 2, 3]])

'''
# keys()
딕셔너리의 Key만을 모아서 dict_keys 객체로 돌려줍니다. (리스트로)
'''
print(my_dict3.keys())
# 결과 -> dict_keys(['key1', 'key2', 'key3', 'key4', 'key5', 'key6'])

'''
# in
딕셔너리 안에 해당 key가 존재하는지 조사하는 방법입니다
존재하는 key의 경우 True
존재하지 않는 key의 경우 False 
를 리턴합니다 
'''
print('name' in my_dict3)
# 결과 -> False
print('key1' in my_dict3)
# 결과 -> True