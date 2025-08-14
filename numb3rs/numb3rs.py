import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    nums = ip.split('.')
    if len(nums) != 4:
        return(False)
    else:
        for i in nums:
            try:
                int(i)
            except ValueError:
                return(False)
            else:
                if int(i) <= 255 and int(i) >= 0:
                    continue
                else:
                    return(False)
        else:
            return(True)






...


if __name__ == "__main__":
    main()