A = float(input())
B = float(input())
C = float(input())

weight_A = float(2)
weight_B = float(3)
weight_C = float(5)

MEDIA = (A * weight_A + B * weight_B + weight_C * C) / \
    (weight_A+weight_B+weight_C)

print(f"MEDIA = {MEDIA:.1f}")
