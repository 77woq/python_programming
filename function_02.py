# definitions and uses
# def 함수 저장. use 호출!

x = 5
print('hello')
def lyrics():
    print("배고팡")
    print("다이어트중")

lyrics()

# Arguments 
# 인자를 이용해 살짝 조정
# 인자는 우리가 함수로 집어 넣는 것 parameters

def greet(lang): # lang == parameters
    if lang=='es':
        print('hola')
    elif lang=='fr':
        print('bonjour')
    else:
        print('hello')
# : 쫌 중요;;
greet('es')
greet('fr')
greet('jb')

# return values
