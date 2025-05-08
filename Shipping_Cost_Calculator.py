# Shipping Cost Calculator
# Aquí hay una nueva actualización por luisgonzalezcabezas
# Here is another update by luisgonzalezcabezas

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

