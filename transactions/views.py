from django.views import View

import json
import requests


class Addition(View):
    pass




class getApi(View):
    @staticmethod
    def get(self):
        r = requests.get('http://call.tgju.org/ajax.json')
        print(r.text)
        result = json.loads(r.text)
        dollar_price = result['current']['price_dollar_rl']['p']
        dollar_price = dollar_price.split(',')
        final_dollar_price = ''
        for i in dollar_price:
            final_dollar_price = final_dollar_price + i

        final_dollar_price = int(final_dollar_price)/10

        print(final_dollar_price)

