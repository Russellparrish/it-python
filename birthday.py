import datetime
from banner import banner

banner("BIRTHDAY", "Russell")

# process
# 1. Find out birthday from user
# 2. Calculat how many days apart that is from now
# 3. Pint the birthday info, days to go,Days ago< or Happy BDay!

def main():
    birthday = get_birthday_from_user()
    now = datetime.date.today()
    num_days = calculate_Days_Between_dates(birthday, now)
    print_birthday_info(num_days)

def get_birthday_from_user():
    print("what is your Birtday?")
    year = int(input("year [YYYY]"))
    month = int(input("month [MM]"))
    day = int(input("day [DD]"))

    birthday = datetime.date(year, month, day)
    return birthday

def calculate_Days_Between_dates(date1, date2):
    this_year = datetime.date(date2.year, date1.month, date1.day)

    dt = this_year - date2
    return dt.days


def print_birthday_info(number_of_days):
    print(number_of_days)







main()