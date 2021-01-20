user_id = input(' id : ')
user_pw = input(' pw: ')

# and ->  A와 B 모두가 True이면  ture
if user_id == "eon" and  user_pw =='1111':
    print('hello')
else:
    print('Wjo are you?')

# or -> A와 B중에 한가지만 true여도 true 
if user_id == "eon" or  user_pw =='1111':
    print('hello')
else:
    print('Wjo are you?')

# not : true -> false , false ->true 가 된다
if not user_id == "eon" :
    print('Wjo are you?') 
else:
    print('hello')





