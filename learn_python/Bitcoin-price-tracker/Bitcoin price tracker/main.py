# modules
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
from matplotlib.ticker import FuncFormatter
from matplotlib import ticker
import matplotlib.dates as dates

import tkinter as tk
from tkinter import messagebox
import webbrowser

# script
import data as d


plt.style.use("seaborn")


LARGE_FONT= ("Verdana", 30, "bold")
NORMAL_FONT = ("Verdana", 16)
NOTE_FONT = ("Verdana", 10)

def callback(url):
    webbrowser.open_new(url)


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default="icon.ico")
        tk.Tk.wm_title(self, "Bitcoin charts")

        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, GraphOne, GraphTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=1, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame): # NOTE: ADD NOTES

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Tk.configure(self, background="#ecf0f1")
        main_text = "Welcome to Bitcoin chart program!\nChoose one of the option:"
        label = tk.Label(self, text=main_text, font=LARGE_FONT, relief="groove", bg="#ecf0f1")
        label.pack(pady=20,padx=20)
        
        button = tk.Button(self, text="History of BTC price", command=lambda: controller.show_frame(GraphOne), height=5, width=15)
        button.pack(ipadx=200)

        button2 = tk.Button(self, text="Current BTC price", command=lambda: controller.show_frame(GraphTwo), height=5, width=15)
        button2.pack(ipadx=200)

        
        # Hyperlinks
        autor = tk.Label(self, text="\nProgrammed by ludius0", fg="#7f8c8d", cursor="hand2", bg="#ecf0f1")
        autor.pack()
        autor.bind("<Button-1>", lambda e: callback("https://github.com/ludius0"))

        link = tk.Label(self, text="Powered by CoinDesk", fg="#7f8c8d", cursor="hand2", bg="#ecf0f1")
        link.pack()
        link.bind("<Button-1>", lambda e: callback("https://www.coindesk.com/price/bitcoin"))





class GraphOne(tk.Frame):

    def __init__(self, parent, controller): #NOTE: Add option to choose date; Add design (show markers, and with ttk)
        tk.Frame.__init__(self, parent)

        year, month, day, hour, minute, second = d.call_time()

        self.start_date = "2013-09-01"
        self.end_date = f"{year}-{month}-{day}"
        
        # Set x and y plots
        self.last_price = 0

        # Prepare graph
        self.draw_graph()

        
        ### SET UP WIDGETS

        text1 = tk.Text(self, font=NORMAL_FONT, height=1, width=22, state="normal")
        text1.insert(tk.END, "Last Price:")
        text1.tag_configure("center", justify='center')
        text1.tag_add("center", "1.0", "end")
        text1.config(state="disabled")
        text1.grid(row=0, column=5, sticky="s")
        
        self.n = tk.StringVar() # Last price
        self.entry1 = tk.Entry(self, font=NORMAL_FONT, textvariable=self.n, state='normal', justify="center")
        self.entry1.insert(0, self.last_price)
        self.entry1.grid(row=1, column=5, sticky="new")

        text2 = tk.Text(self, font=NORMAL_FONT, height=1, width=22, state="normal")
        text2.insert(tk.END, "First date:")
        text2.tag_configure("center", justify='center')
        text2.tag_add("center", "1.0", "end")
        text2.config(state="disabled")
        text2.grid(row=2, column=5, sticky="s")

        self.n2 = tk.StringVar() # Start date
        self.entry2 = tk.Entry(self, font=NORMAL_FONT, textvariable=self.n2, state='normal', justify="center")
        self.entry2.insert(0, self.start_date)
        self.entry2.grid(row=3, column=5, sticky="new")

        text3 = tk.Text(self, font=NORMAL_FONT, height=1, width=22, state="normal")
        text3.insert(tk.END, "Last date:")
        text3.tag_configure("center", justify='center')
        text3.tag_add("center", "1.0", "end")
        text3.config(state="disabled")
        text3.grid(row=4, column=5, sticky="s")

        self.n3 = tk.StringVar() # End date
        self.entry3 = tk.Entry(self, font=NORMAL_FONT, textvariable=self.n3, state='normal', justify="center")
        self.entry3.insert(0, self.end_date)
        self.entry3.grid(row=5, column=5, sticky="new")

        
        button1 = tk.Button(self, text="Find", command=lambda: self.find_date(), height=4, width=10)
        button1.grid(row=6, column=5, sticky="ew")

        button2 = tk.Button(self, text="Go back", command=lambda: controller.show_frame(StartPage), height=4, width=20)
        button2.grid(row=7, column=5)

        self.label1 = tk.Label(self, text="\nNOTES:\nYou can input dates\nto draw specific part of graph.\nIt must be writed in format\nYEAR-MONTH-DAY\nExample: 2019-08-28\nThe oldest day is 2013-09-01\nand you can't write future date.\nAfter you write date, than hit ""find"" button", fg="#7f8c8d", font=NOTE_FONT)
        self.label1.grid(row=8, column=5, columnspan=6, sticky="nsew")

        self.link = tk.Label(self, text="\nPowered by CoinDesk", fg="#7f8c8d", cursor="hand2")
        self.link.grid(row=10, column=0, columnspan=6, sticky="nsew")
        self.link.bind("<Button-1>", lambda e: callback("https://www.coindesk.com/price/bitcoin"))

        # Prepare graph
        self.draw_graph()

    def find_date(self):
        self.start_date = f"{self.entry2.get()}"
        self.end_date = f"{self.entry3.get()}"
        self.refresh()

    def refresh_price(self):
        #self.entry1.delete(0, "end")
        self.n = tk.StringVar() # Last price
        self.entry1 = tk.Entry(self, font=NORMAL_FONT, textvariable=self.n, state='normal', justify="center")
        self.entry1.insert(0, self.last_price)
        self.entry1.grid(row=1, column=5, sticky="new")
        
        #self.entry1.insert(0, self.last_price)
        

    def draw_graph(self): # Set up graph
        self.fig, self.ax = plt.subplots()

        self.chart_type = FigureCanvasTkAgg(self.fig, self)
        self.chart_type.get_tk_widget().grid(row=0, column=0, rowspan=10, columnspan=4)

        self.y_plot, self.x_plot = d.date_loop(self.start_date, self.end_date)
        self.last_price = self.y_plot[-1]

        # Make add dollars to y axis
        formatter = ticker.FormatStrFormatter('$%0.0f')
        self.ax.yaxis.set_major_formatter(formatter)

        # Accept dates
        plt.gca().xaxis.set_major_formatter(dates.DateFormatter("%Y-%m-%d"))
        plt.gca().xaxis.set_major_locator(dates.DayLocator(interval=50))


        # Set up ax
        self.ax.plot(self.x_plot, self.y_plot, label="Bitcoin", color="#FFD54F", linestyle="-")
        self.ax.set_title("Price of Bitcoin in history")

        self.refresh_price()

    def refresh(self): # Delete and create graph
        self.fig.clf()
        self.ax.cla()
        plt.close()
        self.x_plot.clear()
        self.y_plot.clear()
        self.draw_graph()




class GraphTwo(tk.Frame): # Live plotting Bitcoin chart

    def __init__(self, parent, controller): # Set up widgets and graph
        tk.Frame.__init__(self, parent)
        
        self.x_plot_USD, self.y_plot_USD = [], []
        self.x_plot_EURO, self.y_plot_EURO = [], []

        self.x_plot, self.y_plot = [], []
        
        self.current_price = 0
        self.curr = "EUR"
        self.n_1 = -2
        self.n_2 = 0

        self.add_data_to_plots()
        self.prepare_graph()

        ### Set up widgets
        text1 = tk.Text(self, font=NORMAL_FONT, height=1, width=22)
        text1.insert(tk.END, "Choose currency:")
        text1.tag_configure("center", justify='center')
        text1.tag_add("center", "1.0", "end")
        text1.config(state="disabled")
        text1.grid(row=0, column=5, sticky="s")

        
        self.clicked = tk.StringVar()
        self.clicked.set("USD")
        self.choose_c = tk.OptionMenu(self, self.clicked, "USD", "EURO")
        self.choose_c.grid(row=1, column=5, sticky="nsew")
        
        self.button1 = tk.Button(self, text="Change currency", command=self.check_currency)
        self.button1.grid(row=2, column=5, sticky="new")

        text2 = tk.Text(self, font=NORMAL_FONT, height=1, width=22)
        text2.insert(tk.END, "Current price:")
        text2.tag_configure("center", justify='center')
        text2.tag_add("center", "1.0", "end")
        text2.config(state="disabled")
        text2.grid(row=3, column=5, sticky="s")

        self.n = tk.DoubleVar()
        self.entry1 = tk.Entry(self, font=NORMAL_FONT, textvariable=self.n, state='normal', justify="center")
        self.entry1.insert(0, self.current_price)
        self.entry1.grid(row=4, column=5, sticky="new")

        text3 = tk.Text(self, font=NORMAL_FONT, height=1, width=22)
        text3.insert(tk.END, "Set alarm for price:")
        text3.tag_configure("center", justify='center')
        text3.tag_add("center", "1.0", "end")
        text3.config(state="disabled")
        text3.grid(row=5, column=5, sticky="s")

        self.n = tk.DoubleVar()
        self.entry2 = tk.Entry(self, font=NORMAL_FONT, textvariable=self.n, state='normal', justify="center")
        self.entry2.grid(row=6, column=5, sticky="new")
        
        button2 = tk.Button(self, text="Go back", command=lambda: controller.show_frame(StartPage), height=4, width=20)
        button2.grid(row=7, column=5)

        self.label1 = tk.Label(self, text="\nNOTES:\nThe chart is updated every 25 seconds.\nAlarm for price isn't changing\nwith different currency.\nAfter you choose currency,\nthan hit ""Change currency"" button.", fg="#7f8c8d", font=NOTE_FONT)
        self.label1.grid(row=8, column=5, columnspan=6, sticky="nsew")
        
        self.link = tk.Label(self, text="\nPowered by CoinDesk", fg="#7f8c8d", cursor="hand2")
        self.link.grid(row=15, column=0, columnspan=6, sticky="nsew")
        self.link.bind("<Button-1>", lambda e: callback("https://www.coindesk.com/price/bitcoin"))

    def prepare_graph(self): # Set up graph
        self.fig, self.ax = plt.subplots()

        self.chart_type = FigureCanvasTkAgg(self.fig, self)
        self.chart_type.get_tk_widget().grid(row=0, column=0, rowspan=10, columnspan=4)

        self.ani = FuncAnimation(plt.gcf(), self.plot_current_price, interval=25000, blit=False)

    def refresh(self): # Delete and create graph
        self.fig.clf()
        self.ax.cla()
        plt.close()
        self.prepare_graph()

    def clear_plots(self):
        self.x_plot.clear()
        self.y_plot.clear()
        
        
    def check_currency(self):
        clicked = self.clicked.get()
        if clicked == "USD":
            self.n_1 = -2
            self.n_2 = 0
        elif clicked == "EURO":
            self.n_1 = -1
            self.n_2 = 1
        self.refresh()

        
    def add_data_to_plots(self):
        year, month, day, hour, minute, second = d.call_time()
        time_stamp = f"{str(hour)}:{str(minute)}:{str(second)}"
        self.api = d.actual_api(self.curr)
        self.x_plot_USD.append(time_stamp)
        self.x_plot_EURO.append(time_stamp)
        self.y_plot_USD.append(self.api["bpi"]["USD"]["rate_float"])
        self.y_plot_EURO.append(self.api["bpi"]["EUR"]["rate_float"])

    def check_price(self):
        check = float(self.entry2.get())
        if check == 0.0:
            pass
        elif check >= self.current_price:
            tk.messagebox.showinfo(self, message="CHECK PRICE!")
        

    def plot_current_price(self, i): # animated; get update every so often
        
        self.entry1.delete(0, "end")
        
        # Set x and y plots
        self.add_data_to_plots()

        #self.check_currency()

        clicked = self.clicked.get()
        if clicked == "USD":
            self.currency = "USD"
            self.x_plot = self.x_plot_USD
            self.y_plot = self.y_plot_USD
        elif clicked == "EURO":
            self.currency = "EUR"
            self.x_plot = self.x_plot_EURO
            self.y_plot = self.y_plot_EURO

        self.current_price = self.y_plot[self.n_1]
        
        
        formatter = ticker.FormatStrFormatter("%0.0f")
        self.ax.yaxis.set_major_formatter(formatter)


        # Make sure it won't run off wild
        self.ax.cla()
        
        
        self.ax.plot(self.x_plot[self.n_2::2], self.y_plot[self.n_2::2], label="Bitcoin", color="#FFD54F", linestyle="-", marker="o")
        self.ax.set_title("Current price of Bitcoin")

        self.entry1.insert(0, self.current_price)
        self.check_price()


app = App()
app.mainloop()
