class CurrencyConverter:
    def __init__(self, exchange_rate):
        self.exchange_rate = exchange_rate

    def convert_to_chilean_pesos(self, dollars):
        pesos = dollars * self.exchange_rate
        return round(pesos) 

    def convert_to_dollars(self, pesos):
        dollars = pesos / self.exchange_rate
        return round(dollars)
    
def formato_dolares(dolar):
    return f"{dolar} dolares"

def formato_pesos(pesos):
    return f"{pesos} pesos"
    

#peso chileno  con fecha 26/12/2022 correspondiente a $879.50
converter = CurrencyConverter(879.50)

amount_in_pesos = converter.convert_to_chilean_pesos(100)
print(amount_in_pesos)  # 87950
print(formato_pesos(amount_in_pesos)) # 87950 pesos

amount_in_dollars = converter.convert_to_dollars(100000)
print(amount_in_dollars) # 114 dolares
print(formato_dolares(amount_in_dollars)) # 114 dolares