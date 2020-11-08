def price_string_to_price_euro(string):
  """ Función que convierte un string a entero, si el dato no es correcto el precio será 0
      arg:
        string a convertir
      return:
        price en int
  """
  try:
    new_string = string[1:]
    price = float(new_string)
  except:
    price = 0
  return price