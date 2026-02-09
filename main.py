# Quiz #4

# Input
# ========================================

num1 = int(input("Please enter number 1: "))
num2 = int(input("\nPlease enter number 2: "))
mathType = input("\nPlease select a math type (A, S, M, D): ")
# ========================================

# Add
# ========================================

if mathType.lower() == "a":
    print (f"{num1} plus {num2} equals {num1+num2}") 

# ========================================

# Sub
# ========================================

if mathType.lower() == "s":
    print (f"{num1} minus {num2} equals {num1-num2}")

# ========================================

# Mul
# ========================================
def mul(n1, n2):
    return n1*n2

if mathType.lower() == "m":
    print (f"{num1} plus {num2} equals {mul(num1, num2)}")

# ========================================

# Div
# ========================================

if mathType.lower() == "d":
    print (f"{num1} plus {num2} equals {num1/num2}")

# ========================================

# Output
# ========================================

print("this should create a conflict")

# ========================================
