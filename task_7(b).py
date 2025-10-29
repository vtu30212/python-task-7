def cube_product_of_natural_numbers(n):
    product = 1
    for i in range(1, n + 1):
        product *= i ** 3
    return product

n = int(input("Enter the value of N: "))
result = cube_product_of_natural_numbers(n)
print("Cube product of the first", n, "natural numbers is:", result)
