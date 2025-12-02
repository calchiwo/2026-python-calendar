import calendar
import datetime

year = 2026
calendar.setfirstweekday(calendar.MONDAY)

for month in range(1, 13):
    print(f"{calendar.month_name[month]} {year}".center(28))
    print("CW  Mon Tue Wed Thu Fri Sat Sun")

    for week in calendar.monthcalendar(year, month):
        first_day = next((d for d in week if d != 0), None)
        if first_day is None:
            continue
        try:
            cw = datetime.date(year, month, first_day).isocalendar()[1]
        except ValueError:
            continue

        days = " ".join(f"{d:3}" if d != 0 else "   " for d in week)
        print(f"{cw:>2} {days}")

    print()
