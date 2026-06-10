def is_leap_year(x:int)->bool:
    
    """This program checks whether the year provided is leap year or not."""

    if (x%4 == 0 and x%100 != 0) or x%400 == 0:
        return True
    else:
        return False
    

months_with_31_days = ['january','march','may','july','august','october','december']

months_with_30_days = ['april', 'june', 'september', 'november']

from time import sleep

print("\n","This program finds the number of days the given month has.".center(130,'='),"\n")

sleep(1)

while True:
    
    try:
        
        month_name = input('Enter a month name (or hit enter with no input to exit): ')
        # We should validate the input

        if month_name.strip() == "":
            print("Exiting program. Goodbye.\n")
            break

        month_name = month_name.lower()

        match month_name:
            case "february":

                year = input("Enter the year too (or hit enter with no input to exit): ")
        
                if year.strip() == "":
                    print("Exiting program. Goodbye.\n")
                    break
                    # Now it's safe to convert.

                year = int(year)

                if year < 0:
                    print("BCE or CE, year is always positive. Let's try that again.\n")
                    continue   # ensuring the year is > 0 and continuing the year loop
                
                if is_leap_year(year):
                    print(f"The month February of {year} has 29 days as {year} is a Leap year\n")

                else:
                    print(f"The month: {month_name.title()} of {year} has 28 days.\n")

            case month if month in months_with_31_days:
                print(f"The month: {month_name.title()} has 31 days.\n")
            
            case month if month in months_with_30_days:
                print(f"The month: {month_name.title()} has 30 days.\n")

            case _:
                print(f"The month entered: {month_name} is not a recognized month.\n")
                continue    

    except ValueError as Err:
        print(f"{Err}\n")
        








