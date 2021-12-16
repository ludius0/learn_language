from tkinter import *
import requests
import json

# Set up screen
root = Tk()
root.title("Weather app")
root.geometry("450x150")

# Api key to make it all work --> Rewrite it with your API key
api_key = "YOUR API"



### Weather Function
def weather():
    global report, comment
    color = None
    
    try:
# Call data from openweather
        i = city.get()
        api_call = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + i + "&appid=" + api_key)
        api = json.loads(api_call.content)
        
# "Decode" needed data (and match kelvin to celsius and fahrenheit)
        clouds = api["weather"][0]["description"]
        temp_k = api["main"]["temp"]
        temp_f = round(9/5 * (temp_k - 273) + 32)
        temp_c = round(temp_k - 273.15)

# Colors and comments
        if temp_c <= -20:
            color = "white"
            report_comment = "You're going to be ice cube!"
        elif temp_c < -5 and temp_c > -20:
            color = "#6666FF"
            report_comment = "Oh man! It's freaking cold!"
        elif temp_c >= -5 and temp_c <= 10:
            color = "#00CCCC"
            report_comment = "Acceptable."
        elif temp_c > 10 and temp_c <= 20:
            color = "#00FF00"
            report_comment = "Nice."
        elif temp_c > 20 and temp_c <= 30:
            color = "#FFFF33"
            report_comment = "Pretty hot."
        elif temp_c > 30:
            color = "#FF3333"
            report_comment = "Oh man! You're going to be roasted chicken!"
        root.configure(background=color)


# Put data on screen (rewrite labels)
        report.config(text=f"{i}-->Temperature: {temp_f}°F/{temp_c}°C, Weather: {clouds}", background = color)
        comment.config(text=report_comment, background = color)


# Handle Error    
    except Exception as i:
        error = "Error...\nTry restart your connection, change API or type another city."
        report.config(text=error)



### LABELS AND BUTTONS
# Create Entry for user input of city and activation Button
city = Entry(root)
city.grid(row=0, column=0, ipadx=70)
city.insert(0, "London")

find_data_button = Button(root, text="Search", command=weather)
find_data_button.grid(row=0, column=1, ipadx=20, sticky=N+E+S+W)

# Create reporting labels
report = Label(root, text="")
report.grid(row=1, column=0)
comment = Label(root, text="")
comment.grid(row=2, column=0)


###Loop
root.mainloop()

