from datetime import date, datetime


weekdays = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Monday',
    6: 'Monday',
}


def get_birthdays_per_week(users):

    days = {}
    current_date = date.today()
    if len(users) == 0:
        return {}
    for birthdays in users:
        birth_date = (birthdays.get('birthday'))
        birth_date = datetime(year=current_date.year + 1, month=birth_date.month,
                              day=birth_date.day).date()  # for next year
        difference = birth_date - current_date
        if 0 <= int(difference.days) <= 6:
            if days.get(weekdays.get(birth_date.weekday())):
                days.get(weekdays.get(birth_date.weekday())).append(
                    birthdays.get('name'))  # if exist
            else:
                days.update({str(weekdays.get(birth_date.weekday())): [
                            birthdays.get('name')]})  # if new

        birth_date = datetime(year=current_date.year, month=birth_date.month,
                              day=birth_date.day).date()  # for this year
        difference = birth_date - current_date
        if 0 <= int(difference.days) <= 6:
            if days.get(weekdays.get(birth_date.weekday())):
                days.get(weekdays.get(birth_date.weekday())
                         ).append(birthdays.get('name'))
            else:
                days.update(
                    {str(weekdays.get(birth_date.weekday())): [birthdays.get('name')]})

    return days


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 9, 17).date()},
        {"name": "Jana Koza", "birthday": datetime(1028, 9, 12).date()},
        {"name": "NIK", "birthday": datetime(1020, 9, 19).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
