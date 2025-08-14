def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if start_2L(s) and range_char(s) and contain_char(s) and start_0(s) and num_loc(s):
        return(True)

def start_2L(s):
    if s[0:2].isalpha():
        return(True)


def range_char(s):
    if 2<=len(s)<=6:
        return(True)

def contain_char(s):
    if s.isalnum():
        return(True)

def start_0(s):
    n = ""
    L = 0
    for i in s:
         if i.isnumeric():
           n += i
    if len(n) == 0 or n[0] != "0":
        return(True)



def num_loc(s):
    n= ""
    for i in s:
        if i.isdigit():
            n += i
    m =  len(s) - len(n)
    slic = slice(0, m)
    ss = s[slic
           ]
    if ss.isalpha() == True:
        return(True)




main()