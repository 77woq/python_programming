def computepay(hours,rate):
    print("in computepay",hours,rate)
    if hours>40:
        reg = rate * hours
        otp = (hours-40.0) * (rate*0.5)
        pay = reg + otp
    else:
        pay=hours*rate
    print("Returning",pay)
    return pay

sh=input("Enter hours: ")
sr=input("Enter rate: ")
fh=float(sh)
fr= float(sr)
# print(fh,fr)
# 급여계산 추가 수당 계산까지
xp=computepay(fh,fr)

print("Pay:",xp)

def greeting(input):
    try:
        name=str(input)
    except:
        name=-1
        print("please input your name")
    return "hello"+name

print(greeting("connect"))