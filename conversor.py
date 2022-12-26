class CurrencyConverter:
  def __init__(self, exchange_rate):
    self.exchange_rate = exchange_rate

  def convert_to_chilean_pesos(self, dollars):
    pesos = dollars * self.exchange_rate
    return pesos

converter = CurrencyConverter(697.50)

amount_in_pesos = converter.convert_to_chilean_pesos(100)
print(amount_in_pesos)  # 69750.0