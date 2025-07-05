cp= int(input("Enter your cost price"))
sp= int(input("Enter your selling price"))
if cp>sp:
    print("Loss")
elif cp==sp:
     print("neither profit nor loss")
else:
    print("profit")
    p=sp-cp

    print(p)
