
# 리스트의 기본 생김새
number = [1,2,3,4,5]
name = ['구름','소정','미연','따옴']

# name 리스트에 미연과 number 리스트에 5의 값을 출력해보자

print(name[2]) # 리스트의 요소는 0부터 순차적으로  
# 결과 : 미연
print(number[-1]) # 리스트는 , 뒤에서 부터 순서를 -1 로 시작한다 
# 결과 : 5  



# 리스트안에 요소갯수를 출력해보자 
print(len(name)) # name의 요소갯수는 4개
print(len(number)) #number의 요소갯수는 5개



# 리스트의 요소 수정하기 
miyeon = ['미연',3]
miyeon[1] = 25
print(miyeon) # 결과 : ['미연', 25]

# append 사용해보기
miyeon.append('cat')
print(miyeon) # 결과 : ['미연', 25, 'cat']

# remove 사용해보기 
miyeon.remove('미연')
print(miyeon) # 결과 : [25, 'cat']

# del 사용해보기
del miyeon[0]
print(miyeon) # 결과 : ['cat']