def main():
    print("This progream will add two numbers")
    num1:str = input("Enter the first number:")
    num1:int = int(num1)
    num2:str = input("Enter the second number:")
    num2:int = int(num2)

    total:int = num1+num2
    print(f"Ther total of {num1} + {num2} is {total}  ")



if __name__ == '__main__':
    main()