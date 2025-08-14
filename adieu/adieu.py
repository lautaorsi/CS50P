import inflect
p = inflect.engine()
list = []
rlist=[]
try:
    while True:
            s = input("Input: ")
            list.append(s)



except EOFError:
    rlist = p.join((list))
    print(f"\nAdieu, adieu, to {rlist}")
