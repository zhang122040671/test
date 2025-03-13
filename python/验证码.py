import random

def createCode():
    codeStr=""
    for num in range(4):
        codeStr+=str(random.randint(0,9))
    return codeStr

def checkingCode(inputCode,realCode):
    res=False
    if (inputCode==realCode):
        res=True
    return res

realCode=createCode()
print(realCode)
inputCode=input("请输入短信验证码:")

if (checkingCode(inputCode,realCode)):
    print("验证码正确")
else:
    print("验证码错误")
