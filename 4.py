a=int(input("請輸入一個三位數:"))
b=a//100
c=a%100//10
d=a%10
e=b+c+d
print(f"每位數字的總和:{e}")