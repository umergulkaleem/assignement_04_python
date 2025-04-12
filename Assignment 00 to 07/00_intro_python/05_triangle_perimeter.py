def main():
    side1:int = int(input("Enter the length of side 1 :"))
    side2:int = int(input("Enter the length of side 2 :"))
    side3:int = int(input("Enter the length of side 3 :"))

    perimeter :int = side1+side2+side3
    print(f"the perimeter of the triangle is {perimeter}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()