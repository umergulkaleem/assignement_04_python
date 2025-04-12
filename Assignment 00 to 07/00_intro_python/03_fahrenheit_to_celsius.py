def main():
    print("This progem will change temprature in fahrenheit to celsius")
    temp_fahrenheit : str = input("Enter the temprature in farenheit :")
    temp_fahrenheit : int =  int(temp_fahrenheit)
    temp_celsius : int = (temp_fahrenheit - 32) * 5/9
    print(f"{temp_fahrenheit} degree farenheit is equal to {temp_celsius} degree celsius")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()