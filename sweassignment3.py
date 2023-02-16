def sum_list(num):
    return sum(num)

def product_list(num):
    product = 1
    for number in num:
        product *= number
    return product

def reverse_list(num):
    return num[::-1]

def main():

    inputstring = input("Enter values in the array with a space in between.")
    inputnums = inputstring.split()

    num = []
    for item in inputnums:
        num.append(int(item))

    sum_result = sum_list(num)
    product_result = product_list(num)
    reverse_result = reverse_list(num)

    print("Sum: ", sum_result)
    print("Product: ", product_result)
    print("Reverse: ", reverse_result)

if __name__ == "__main__":
    main()