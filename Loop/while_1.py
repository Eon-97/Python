# while 문의 기본 생김새

'''
while_stmt ::= "while" expression ":" suite
["else" ":" suite]

while문은 조건문이 참인 동안에 while문 아래의 문장이 반복해서 수행됩니다.
'''

treeHit = 0
while treeHit <10:
    treeHit = treeHit +1
    print('나무를 %d번 찍었습니다' %treeHit)
    if treeHit ==10:
        print("나무가 넘어갑니다")