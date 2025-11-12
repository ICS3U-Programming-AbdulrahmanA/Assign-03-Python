def main():
    # get month and year from user as a string
    month_input = input("Please enter a month number (1-12): ")
    year_input = input("Please enter a year: ")

    # to convert month into int and to catch an exception
    try:
        month = int(month_input)

        # to convert year into int and catch an exception
        try:
            year = int(year_input)

            # check for valid month input
            if month < 1 or month > 12:
                print("Month must be between 1 and 12.")
            else:
                # leap year check
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    leap_year = True
                else:
                    leap_year = False

                # determine number of days
                if (
                    month == 1
                    or month == 3
                    or month == 5
                    or month == 7
                    or month == 8
                    or month == 10
                    or month == 12
                ):
                    days = 31
                elif month == 4 or month == 6 or month == 9 or month == 11:
                    days = 30
                elif month == 2:
                    if leap_year:
                        days = 29
                    else:
                        days = 28
                else:
                    print("Invalid month.")

                # determine month name
                if month == 1:
                    monthname = "January"
                elif month == 2:
                    monthname = "February"
                elif month == 3:
                    monthname = "March"
                elif month == 4:
                    monthname = "April"
                elif month == 5:
                    monthname = "May"
                elif month == 6:
                    monthname = "June"
                elif month == 7:
                    monthname = "July"
                elif month == 8:
                    monthname = "August"
                elif month == 9:
                    monthname = "September"
                elif month == 10:
                    monthname = "October"
                elif month == 11:
                    monthname = "November"
                elif month == 12:
                    monthname = "December"

                # display results
                print()
                print("Month:", monthname)
                print("Year:", year)
                print("Days in this month:", days)

                if leap_year == True:
                    print("This is a leap year.")
                else:
                    print("This is not a leap year.")
        # if there is an invalid input
        except:
            print("Invalid input. Please enter a valid number.")

    # if there is an invalid input
    except:
        print("Invalid input. Please enter a valid number.")


main()
