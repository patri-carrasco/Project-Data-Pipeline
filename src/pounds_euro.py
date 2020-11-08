def pounds_euro(l):
    """
        Función que convierte las libras a euros
        arg:
            l, valor en libras que se quiere calcular
        return
            valor en euros con dos decimales
        
        puntos a mejor: 
          usar api https://cambio.today/api
    """
    return round(l*1.11,2)