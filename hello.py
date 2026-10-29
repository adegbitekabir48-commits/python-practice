# Engineer Adegite Kabir - Backend in training
print("hello world")
print("I am Kabir, learning Python Backend - Alhamdulillah")

def calculate(a, b, op):
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/": return a / b if b != 0 else "Cannot divide by zero"
    return "Unknown operation"

print("10 + 5 =", calculate(10, 5, "+"))
print("10 / 0 =", calculate(10, 0, "/"))