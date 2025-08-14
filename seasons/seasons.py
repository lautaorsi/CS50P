from datetime import date
import datetime
import re
import inflect
import sys



def word(time):
     p = inflect.engine()
     words = p.number_to_words(time, andword=" ")
     return(words)

def forma(time):
    if not re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$",time):
        sys.exit(ValueError)
    else:
        date_format = "%Y-%m-%d %H:%M:%S"
        time = time + " 00:00:00"
        bday = datetime.datetime.strptime(time, date_format).date()
        return(bday)

def main():
    bday = forma(input('Date of Birth:'))
    date_format2 = "%Y-%m-%d %H:%M:%S"
    pre = (datetime.date.today())
    today = datetime.datetime.strptime(str(pre) + " 00:00:00", date_format2).date()
    ddate = today - bday
    t_minutes = int((ddate.total_seconds())/60)
    print((word(t_minutes) + " minutes").capitalize())









if __name__ == "__main__":
    main()