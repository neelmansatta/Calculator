#Calculator
from art import logo
# Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  
  #Here we select "+"
  check_to_continue = "y"
  while check_to_continue == "y":
    operation_symbol = input("pick an operation: ") 
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    check_to_continue = input ("Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation. or another other key to stop :").lower()
    if check_to_continue == "y":
      num1 = answer
    elif check_to_continue =="n":
      calculator()
    else:
      return 

calculator()