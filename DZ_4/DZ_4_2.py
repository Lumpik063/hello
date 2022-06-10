
from requests import get
from xml.etree import ElementTree


def currency_rates(cur):

    currency_dict = {'USD': 'R01235', 'EUR': 'R01239', 'GBP': 'R01035'}

    if cur not in currency_dict:
        return None

    currency = currency_dict[cur]

    response = get(f'http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=02/03/2001&date_req2=14/03/2001&VAL_NM_RQ={currency}')


    tree = ElementTree.fromstring(response.text)
    currency_list=[]
    for i in tree:
        for j in i:
            if j.tag == 'Value':
                currency_list.append(j.text)
    return currency_list


print(currency_rates('USD'))