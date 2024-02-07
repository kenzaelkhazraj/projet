from datetime import datetime
import prettytable

events =[]

def add_event(title, date, time):
    event ={"title":title, "date": date, "time": time}
    events.append(event)

def display_events():
    sorted_events = sorted(events, key=lambda x: 
datetime.strptime (x["date"] + " " + x["time"],
"%Y-%m-%d %H:%M"))
    
    table = prettytable.prettytable(["title","date","time"])
    for event in sorted_events:
        table.add_row([event['title'],event['date'],event['time']])
        print(table)

while True :
    print("1. Add an event\n2. display events\n3.quit")
    choice = input("choice: ")

    if choice == "1":
        title = input("Event title: ")
        date = input("Event date (Year-Month-Day): ")
        time = input("Event time (Hour:Minute): ")
        add_event(title, date, time)

    elif choice == "2":
        display_events()

    elif choice== "3":
       break

