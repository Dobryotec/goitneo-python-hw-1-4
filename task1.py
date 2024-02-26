from datetime import date, timedelta
from collections import defaultdict

users = [{
    "name": "Bill", "birthday": date(1995, 10, 30)
},
{
    "name": "John", "birthday": date(1996, 5, 26)
},
{
    "name": "Jane", "birthday": date(1997, 3, 3)
},
{"name": "Dmytro", "birthday": date(1996, 2, 29)}]

def get_birthdays_per_week(users):
    birthdays_per_week = defaultdict(list)
    today = date.today()
    
    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year.replace(year=today.year + 1)
        
        delta_days = (birthday_this_year - today).days
        next_birthday_weekday = (today + timedelta(days=delta_days)).strftime('%A')
        
        if next_birthday_weekday == "Saturday":
            delta_days += 2
        elif next_birthday_weekday == "Sunday":
            delta_days += 1
        
        next_birthday_date = today + timedelta(days=delta_days)
        
        next_birthday_weekday = next_birthday_date.strftime('%A')

        if delta_days > 0 and delta_days < 7:
           birthdays_per_week[next_birthday_weekday].append(user["name"])

    for day, names in birthdays_per_week.items():
        print(f"{day}: {', '.join(names)}")


get_birthdays_per_week(users)    





