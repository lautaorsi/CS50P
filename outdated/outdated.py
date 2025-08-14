months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

mc = 1

while True:
    s = input("Date:").strip(" ")
    if s.find("/") != -1:
        s = s.split("/")
        try:
           s[0]=int(s[0])
           s[1]=int(s[1])
        except ValueError:
            continue
        if s[0] <= 12 and s[1] <= 31:
            day = s[0]
            month = s[1]
            year = s[2]
            print(f"{year}-{day:02d}-{month:02d}")
            break
    elif s.find(",") != -1:
        s = s.split(" ")
        try:
            s[2]=int(s[2])
            s[1]=int(s[1].strip(","))
            for i in months:
                if s[0] == i:
                    break
                else:
                    mc += 1
                    continue
            if s[1] <= 31:
                day = s[1]
                month = mc
                year = s[2]
                print(f"{year}-{mc:02d}-{day:02d}")
            else:
                continue
            break
        except ValueError:
            continue


