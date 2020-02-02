x=0
if x<2:
    print('small')
elif x<10:
    print("medium")
else:
    print('large')
print('all done!')

# traceback error 복구하고 싶은 부분에 띄우는 파이썬 자체 오류

x = 21

if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
elif x < 20 :
    print('Big')
elif x < 40 :
    print('Large')
elif x < 100 :
    print('Huge')
else :
    print('Ginormous')
# large가 출력된다

# try / except
astr = 'hello bob'
try:
    istr= int(astr)
except:
    istr=-1
# except문은 try 문이 작동되지 않을 때 쓰임
print('FIRST',istr)
# try문에 print 그냥 출력 넣는 것은 무의미!
# try 문에는 중단될 것 같은 구문 넣는게 좋음

# 더 현실적인 예ㅅㅣ 
rawstr=input('enter a number: ')
try:
    ival=int(rawstr)
except:
    ival=-1
if ival>0:
    print('nice work!')
else:
    print('not a number')

# 즉 파이썬 try/except
# 에러가 발생할 것 같은 코드를 try안에 넣고 except 뒤에는 발생할 수 있는 에러의 이름?을 적어두면
# 에러 발생시 프로그램이 멈추지 않고 별도 처리가 가능.