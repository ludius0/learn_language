import time
from datetime import datetime
import calendar


class menu():

    def displey_current_time():
        now = datetime.now()
        print("\n" + f"{now}" + "\n")

    def displey_year():
        print(time.strftime("\n" + "%Y" + "\n"))

    def displey_month():
        print(time.strftime("\n" + "%m" + "\n"))

    def displey_minute():
        print(time.strftime("\n" + "%M" + "\n"))

    def displey_second():
        print(time.strftime("\n" + "%S" + "\n"))

    def displey_user_day():
        import datetime
        try:
            user_date = input("Write date (for example: 04 January 2020): ")
            resulted_day = datetime.datetime.strptime(user_date, "%d %B %Y").weekday()
            print(f"\n{calendar.day_name[resulted_day]}" + "\n")
        except:
            print("Error...\n")


while True:
    
    time = datetime.now()
        
    print("Choose action:\n1. Write a current time\n2. Write a current year\n3. Write a current month\n4. Write a current minute\n5. Write a current seconds\n6. Find a day\n7. End program")
    user_input = input("Write a number: ")
    if user_input == "1" or user_input == " 1":
        menu.displey_current_time()
        
    elif user_input == "2" or user_input == " 2":
        menu.displey_year()
        
    elif user_input == "3" or user_input == " 3":
        menu.displey_month()
        
    elif user_input == "4" or user_input == " 4":
        menu.displey_minute()
        
    elif user_input == "5" or user_input == " 5":
        menu.displey_second()
        
    elif user_input == "6" or user_input == " 6":
        menu.displey_user_day()
        
    elif user_input == "7" or user_input == " 7":
        break
    else:
        print("Invalid number")

print("Goodbye...")
