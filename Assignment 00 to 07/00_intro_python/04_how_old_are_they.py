def main():
    print("This progrem will print the age of the people ")
    names :list[str] = ["Anton", "Beth", "Chen", "Drew" ,"Ethan"]
    age :list[int] = [21,21+6,21+6+20,21+6+20+21,21+6+20]

    for i in range(len(names)):
        print(f"{names[i]} age is {age[i]}")


if __name__ == '__main__':
    main()