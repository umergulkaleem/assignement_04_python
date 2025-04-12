DAYS_IN_YEAR = 365
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
SECONDS_PER_MINUTES =60


def main():
    totalseconds = DAYS_IN_YEAR*HOURS_PER_DAY*MINUTES_PER_HOUR*SECONDS_PER_MINUTES

    print(f"The seconds in a year is {totalseconds}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()