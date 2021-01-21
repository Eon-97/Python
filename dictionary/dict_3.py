my_dict3 =  dict(
    key1 = 123, #int
    key2 = 1.23, #float
    key3 = 'str', #str
    key4 = ('tuple',1,2,3), #tuple
    key5 ={'dict':1,'dict2':2}, #dict
    key6 = ['list',1,2,3,] #list
)

# clear() 매소드를 사용하여 딕셔너리의 모든 아이템을 삭제

my_dict3.clear()
print(my_dict3) # 결과 : {}

# get() 매소드를 사용하여 존재하지 않는 키로 none 리턴하기
# get() 매소드를 사용했을 때 key의 값이 딕셔너리 안에 존재하면 key의 맞는 value를 리턴합니다 
my_dict4 = {
    '하나' : 1,
    '둘' :2,
    3 : '셋'
}
'''
존재하지 않는 key를 입력했을 때 일어나는 에러를 방지하기 위해 많이 사용됩니다.
'''
print(my_dict4.get('넷'))
# 결과 : None 
print(my_dict4.get('하나'))
# 결과 : 1 