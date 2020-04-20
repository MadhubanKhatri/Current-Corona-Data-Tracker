from tkinter import *
import requests
from bs4 import BeautifulSoup

root = Tk()
root.geometry("400x180")
root.title("Corona Tracker App")

url = "https://worldometers.info/coronavirus"
r = requests.get(url)
data = r.content
soup = BeautifulSoup(data, 'html.parser')
cases = soup.find_all('div',class_="maincounter-number")

def get_data():
    cases_lbl['text'] = f"Total Cases: {cases[0].get_text().strip()}"
    death_lbl['text'] = f"Total Deaths: {cases[1].get_text().strip()}"
    recover_lbl['text'] = f"Total Recovered: {cases[2].get_text().strip()}"

    lbl['text'] = ":Stay Home:"

frame = Frame(root,borderwidth=5,bg="orange")
frame.pack(fill=X)

btn = Button(frame,text="Get Data", font="lucida 15 bold", command=get_data)
btn.pack()

cases_lbl = Label(frame, text="Total Cases: ", bg="orange", fg="grey", font="arial 15 bold")
cases_lbl.pack()

death_lbl = Label(frame, text="Total Deaths: ", bg="orange", fg="red",font="arial 15 bold")
death_lbl.pack()

recover_lbl = Label(frame, text="Total Recovered: ", bg="orange", fg="green",font="arial 15 bold")
recover_lbl.pack()

lbl = Label(root, text="", bg="steelblue",fg="white", font="arial 15 bold")
lbl.pack(fill=X)

root.mainloop()