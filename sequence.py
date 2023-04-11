#Each "line" counts the previous line starting with n
def nthterm(n):
  if n==1: #one
    return "1"
  if n==2: #one 1
    return "11"
  prterm="11" 
  for i in range(3, n+1):
    prterm=prterm+"&"
    lgh=len(prterm)
    count=1
    gh=""
    for z in range(1,lgh):
      if prterm[z]!=prterm[z-1]:
        gh=gh+str(count+0)
        gh=gh+prterm[z-1]
        count=1
      else:
        count=count+1
    prterm=gh
  return prterm
n=int(input("Enter n integer to know nth term of the sequence: "))
print("-----------------------------")
ans=(nthterm(n))
print("The nth term of the sequence is: ", ans)
