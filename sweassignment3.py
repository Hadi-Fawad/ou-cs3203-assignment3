def sum_list(num):
    return sum(num)

def product_list(num):
    product = 1
    for number in num:
        product *= number
    return product


array = [1, 2, 3, 5, 10]
sumres = sum_list(array)
prodres = product_list(array)
print(sumres)
print(prodres)