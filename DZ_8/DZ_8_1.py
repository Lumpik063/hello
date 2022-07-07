import re


email_test = ['alibaba@mail.ru', 'sdfghdhdhd', 'traratata@mailru']



check = re.compile(r"(?P<username>[a-zA-Z0-9\.\-\_]+)@(?P<domain>[a-zA-Z0-9\.\-\_]+)")


def email_parse(address):
    match = re.search(check, address)
    try:
        if check.match(address):
            return match.groupdict()
        else:
            raise ValueError from ValueError
    except ValueError:
        print(f'ValueError: wrong email:{address}')

res = map(email_parse, email_test)

for j in res:
    print(j)
