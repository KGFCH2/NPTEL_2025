import math

weights_input = input()
weights = weights_input.split()
rounded_weights = [str(math.floor(float(weight))) for weight in weights]
output = ",".join(rounded_weights)
print(output)
