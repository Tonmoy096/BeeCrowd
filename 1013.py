inputs = input().split()  
a = int(inputs[0])  
b = int(inputs[1])
c = int(inputs[2])


MaiorAB = (a + b + abs(a - b)) // 2
MaiorFinal = (MaiorAB + c + abs(MaiorAB - c)) // 2

print(f"{MaiorFinal} eh o maior")