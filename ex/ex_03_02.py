sh=input("Enter hours: ")
sr=input("Enter rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except: 
    print("Error, please enter numeric number!")
    quit() 
    # quit() donotcontinue!
    
fh=float(sh)
fr= float(sr)
# print(fh,fr)
# 급여계산 추가 수당 계산까지
if fh>40:
    print("overtime")
    reg = fr * fh
    otp = (fh-40.0) * (fr*0.5)
    xp = reg + otp
else:
    xp=fh * fr
print("Pay:",xp)