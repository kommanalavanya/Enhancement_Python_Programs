def add(n1,n2):
  return n1+n2
def sub(n1,n2):
  return n1-n2
def prod(n1,n2):
  return n1*n2
def div(n1,n2):
  return n1/n2


operations = {
  "+": add,
  "-": sub,
  "*": prod,
  "/": div
}
num1=int(input("what is the first number"))
num2=int(input("what's the second number"))
for key in operations:
  print(key)
op=input("Enter the operator any from the above")
result=operations[op](num1,num2)
print(f"{num1} {op} {num2} = {result}")
  