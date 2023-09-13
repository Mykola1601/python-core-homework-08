from datetime import date, datetime


weekdays ={ 
    0: 'Monday',
    1: 'Tuesday', 
    2: 'Wednesday', 
    3: 'Thursday', 
    4: 'Friday', 
    5: 'Saturday', 
    6: 'Sunday',
    }



def get_birthdays_per_week(users):
    
    days={}
    # print(users)
    current_date = date.today()
    # print('now=', current_date)
    if len(users) == 0:
        users=[]
    for birthdays in users:
        # print (birthdays)
        # birth_date = datetime(birthdays.get('birthday'))
        birth_date = birthdays.get('birthday')
        birth_date = date(year=current_date.year, month = birth_date.month, day = birth_date.day )
        # print(birth_date.weekday())
        difference = birth_date - current_date
        
        # print (birth_date.weekday())
        # print ("diff", difference.days)

        if difference.days < 0 :
           print('birth passed')
        # else:
        days.update( { weekdays.get(birth_date.weekday()) : birthdays.get('name')}) 
           

    print(days)
    return days










if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 12, 12).date()},
        # {"name": "Jana Koza", "birthday": datetime(2028, 10, 10).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
