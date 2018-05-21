from math import ceil
from zeep import Client


def temp_convert():
    print('Enter path to temp_list file')
    file_temp = input()

    with open(file_temp) as f:
        temp_in_celcius = []
        for temp in f:
            client1 = Client('https://www.w3schools.com/xml/tempconvert.asmx?WSDL')
            convertion_result = round(float(client1.service.FahrenheitToCelsius(temp.split()[0])), 2)
            temp_in_celcius.append(convertion_result)

        print('Средняя температура {}°C'.format(round(sum(temp_in_celcius) / len(temp_in_celcius), 2)))


def calc_flight_cost():
    print('Enter path to cost_list file')
    file_curr = input()
    with open(file_curr) as f:
        cost_for_each_flight = []
        for cost in f:
            cost_for_each_flight.append(cost.split(':')[1].strip())

        tocurrency = 'RUB'
        total_cost = 0
        for cost in cost_for_each_flight:
            amount = cost.split()[0]
            fromcurrency = cost.split()[1]
            client1 = Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
            # cost = client1.service.ConvertToNum(None, 'USD', toCurrency='EUR', 100, 2, None, None)
            cost_resp = ceil(
                client1.service.ConvertToNum(fromCurrency=fromcurrency, toCurrency=tocurrency, amount=amount,
                                             rounding="true")
            )
            total_cost += cost_resp

        print('Общая стоимость перелетов', total_cost, tocurrency)


temp_convert()

calc_flight_cost()
