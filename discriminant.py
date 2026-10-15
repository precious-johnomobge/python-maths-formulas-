# My First Python Formula - By Precious John Omobga
# Journey: WAEC 2028 -> Oxford Computer Science
# Formula: D = b² - 4ac (Quadratic Discriminant)

def calculate_discriminant(a, b, c):
    """Calculate D = b squared - 4ac"""
    D = b**2 - 4*a*c
    return D

# Example values
a = 1
b = 5
c = 6

D = calculate_discriminant(a, b, c)

print("=== Quadratic Discriminant ===")
print(f"For equation: {a}x² + {b}x + {c} = 0")
print(f"D = b² - 4ac = {b}² - 4*{a}*{c}")
print(f"D = {D}")

if D > 0:
    print("Result: Two distinct real roots")
elif D == 0:
    print("Result: One repeated real root")
else:
    print("Result: Two complex roots")

print("\nCoded by Precious - Future Oxford CS Student!")