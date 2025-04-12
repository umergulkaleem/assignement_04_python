
def main():
    C:int= 299792458
    mass :int =int(input("enter the mass is kg :"))
    energy= mass*C*C

    print("e = m * C^2...")
    print("m = " + str(mass) + " kg")
    print("C = " + str(C) + " m/s")
    print(f"the energy according to E=mC^2 is :{energy} j")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()