
INCHES_IN_FOOT:int = 12

def main():
   feet:float =float(input("Enter the no of feet :"))
   inches :float = feet*INCHES_IN_FOOT

   print(f"{feet} feet is equal to {inches} inches")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()