from datetime import date
from datetime import datetime

today = date.today()
curr_time = datetime.now()


class menu():

    def current_time():
        now = datetime.now()
        print(f"{now}" + "\n")
    
    def year():
        formatted_time = curr_time.strftime("%Y")
        print(f"{formatted_time}" + "\n")

    def month():
        formatted_time = curr_time.strftime("%m")
        print(f"{formatted_time}" + "\n")

    def minute():
        formatted_time = curr_time.strftime("%M")
        print(f"{formatted_time}" + "\n")

    def second():
        formatted_time = curr_time.strftime("%S")
        print(f"{formatted_time}" + "\n")

    def find_user_day():
        import datetime
        try:
            user_date = input("Write date (for example: 04 January 2020): ")
            resulted_day = datetime.datetime.strptime(user_date, "%d %B %Y").weekday()
            print(f"{calendar.day_name[resulted_day]}" + "\n")
        except:
            print("Error...\n")

main_menu = True

while main_menu:
    print("Choose action:\n1. Write a current time\n2. Write a current year\n3. Write a current month\n4. Write a current minute\n5. Write a current seconds\n6. Find a day\n7. End program")
    user_input = input("Write a number: ")
    if user_input == "1" or user_input == " 1":
        menu.current_time()
    elif user_input == "2" or user_input == " 2":
        menu.year()
    elif user_input == "3" or user_input == " 3":
        menu.month()
    elif user_input == "4" or user_input == " 4":
        menu.minute()
    elif user_input == "5" or user_input == " 5":
        menu.second()
    elif user_input == "6" or user_input == " 6":
        menu.find_user_day()
    elif user_input == "7" or user_input == " 7":
        main_menu = False
    else:
        print("Invalid number")

print("Goodbye...")


