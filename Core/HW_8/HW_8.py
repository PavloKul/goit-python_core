from datetime import datetime, date, timedelta
from unicodedata import name

birth_list = [
    {'name': 'Ivan', 'birthday': datetime(1985, 2, 24)},
    {'name': 'Petro', 'birthday': datetime(1999, 8, 1)},
    {'name': 'Ihor', 'birthday': datetime(2001, 8, 5)},
    {'name': 'Masha', 'birthday': datetime(2015, 7, 31)},
    {'name': 'Boris', 'birthday': datetime(2015, 7, 30)},
    {'name': 'Volodymyr', 'birthday': datetime(2015, 8, 2)}]


def get_birthdays_per_week(birth_list):
    
    today = datetime.now()
    start = today - timedelta(days=today.weekday()-5)
    end = start + timedelta(days=6)
    current_year = today.year
    grouped_birth = {}
    weekDays = ("Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday")
    
    for birth in birth_list:
        
        if end.date() >= birth['birthday'].replace(year=current_year).date() >= start.date():
            current_birth = birth['birthday'].replace(year=current_year).date()
            day = current_birth.strftime('%A')
        
            if day == 'Sunday' or day == 'Saturday':
                day = 'Monday'

            if day not in grouped_birth:
                grouped_birth[day] = []
            grouped_birth[day].append(birth['name'])
            
    for day in weekDays:
        if day in grouped_birth:
            t = ', '.join(grouped_birth[day])

            print(f'{day}: {t}')
    

    
    
    




get_birthdays_per_week(birth_list)
