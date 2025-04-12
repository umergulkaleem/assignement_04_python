import math

def main():
    print("Delete this line and write your code here! :)")

    ab:int=int(input("Enter the lenght if AB side"))
    ac:int=int(input("Enter the lenght if AC side"))

    bc = math.sqrt(ab**2 +ac**2)

    print(f"The length of the hypotenuse is {bc}")
    






# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()