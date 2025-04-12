def main():
    

    divident :float = float(input("enter the divident :"))
    divider :float = float(input("enter the divider :"))

    quotient = divident //divider
    remainder = divident % divider

    print(f"The quotient is {quotient} and the remainder is {remainder}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()