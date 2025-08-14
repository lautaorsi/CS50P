import validators

inp = input('Whats your email address?')
res = validators.email(inp)
if res == True:
    print('Valid')
else:
    print('Invalid')