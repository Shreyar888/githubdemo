x = "8"
c = x 
for i in range(0,10):
    print(c, end="")
    c += x                   #value will be changed in each iteration (mutable)
    if i == 9:
        break
    else:
        print(",", end=" ")
   

