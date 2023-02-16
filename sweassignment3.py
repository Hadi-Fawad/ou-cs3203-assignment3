def sum_list(num):
    return sum(num)

def product_list(num):
    product = 1
    
    for number in num:
        product *= number
    return product

def main():

    inputstring = input("Enter values in the array with a space in between.")
    inputnums = inputstring.split()

    numbers = []
    for item in inputnums:
        numbers.append(int(item))

    sum_result = sum_list(numbers)

    print("Sum: ", sum_result)
    print("Product: ", product_result)

if __name__ == "__main__":
    main()