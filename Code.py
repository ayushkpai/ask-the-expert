from tkinter import Tk, simpledialog, messagebox
from dotenv import load_dotenv
import os

load_dotenv()
CAPITAL_FILE = os.getenv("CAPITAL_FILE")

root = Tk()
root.withdraw()

the_world = {}

def read_from_file():
    with open(CAPITAL_FILE) as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            country, city = line.split("/")
            country = country.lower()
            city = city.lower()
            the_world[country] = city

def ask_question():
    query_country = simpledialog.askstring(
        "Ask the expert",
        "Type the name of a country"
    )
    if query_country:
        query_country = query_country.lower()

    if query_country is None:
        root.quit()
        return

    query_country = query_country.strip()

    if query_country in the_world:
        result = the_world[query_country]
        messagebox.showinfo(
            "Ask the expert",
            f"The capital of {query_country.title()} is {result.title()}"
        )
    else:
        city = messagebox.showinfo(
            "Ask the expert",
            f"There is no country called {query_country.title()}"
        )

        if city is None:
            root.quit()
            return

        city = city.strip()

    root.after(100, ask_question)

read_from_file()
root.after(100, ask_question)

root.mainloop()
