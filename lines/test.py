import sys


def main():
     counter = 0

     file = open(fname, "r")
     for line in file:
          newline = line.strip()
          if len(newline) == 0:
               continue
          else:
               if newline[0] != '#':
                    counter += 1
     print(counter)





if __name__ == "__main__":
    main()