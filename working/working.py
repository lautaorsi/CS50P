import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if re.search(r"^(\d{1,2})(:\d{2})? (AM|PM) to (\d{1,2})(:\d{1,2})? (AM|PM)$",s):
        matches = re.search(r"^(\d{1,2})(:\d{2})? (AM|PM) to (\d{1,2})(:\d{1,2})? (AM|PM)$",s)
        hour1 = int(matches.group(1))
        try:
            minutes1 = int(matches.group(2).strip(':'))
        except AttributeError:
            minutes1 = 00

        meridiem1 = matches.group(3)
        hour2 = int(matches.group(4))
        try:
            minutes2 = int(matches.group(5).strip(':'))
        except AttributeError:
            minutes2 = 00
        meridiem2 = matches.group(6)
        if int(minutes1) >= 60 or int(minutes2) >= 60:
            raise (ValueError)
        if meridiem1 == "PM":
            hour1 += 12
            if hour1 == 24:
                hour1 = 12

        if meridiem2 == "PM":
            hour2 += 12
            if hour2 == 24:
                hour2 = 12

        if meridiem1 == "AM":
            if hour1 == 12:
                hour1 = 0
        if meridiem2 == "AM":
              if hour2 == 12:
                hour2 = 0

        if hour1 < 10:
            hour1 = f'0{hour1}'
        if minutes1 < 10:
            minutes1 = f'0{minutes1}'
        if hour2 < 10:
            hour2 = f'0{hour2}'
        if minutes2 < 10:
            minutes2 = f'0{minutes2}'
        return(str(hour1) + ':' + str(minutes1) + ' to ' + str(hour2) + ':' + str(minutes2) )







    else:
        raise (ValueError)





if __name__ == "__main__":
    main()