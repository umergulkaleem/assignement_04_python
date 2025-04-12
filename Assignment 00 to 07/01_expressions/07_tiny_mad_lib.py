SENTENCE_START :str = "Panaversity is amazing i learned python to make my"

def main():

    adjective:str=input("enter and adjective :")
    noun:str=input("enter and noun :")
    verb:str=input("enter and verb :")

    print(SENTENCE_START+ " "+ adjective+ " "+noun+ " "+verb+".")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()