def obtener_precio_bitcoin(fecha):
    url = f"https://api.coingecko.com/api/v3/coins/bitcoin/history?date={fecha}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        try:
            precio_usd = datos['market_data']['current_price']['usd']
            precio_eur = datos['market_data']['current_price']['eur']
            market_cap = datos['market_data']['market_cap']['usd']
            return {
                'fecha': fecha,
                'precio_usd': precio_usd,
                'precio_eur': precio_eur,
                'market_cap': market_cap
            }
        except KeyError:
            print(f"No se encontraron datos de precios o capitalización para la fecha {fecha}")
            return None
    else:
        print(f"Error al obtener los datos para la fecha {fecha}: {respuesta.status_code}")
        return None

fechas = ['01-01-2024', '01-07-2024']

datos_bitcoin = []

for fecha in fechas:
    datos = obtener_precio_bitcoin(fecha)
    if datos:
        datos_bitcoin.append(datos)

with open('bitcoin_historical_data.json', 'w') as archivo_json:
    json.dump(datos_bitcoin, archivo_json, indent=4)

print("Datos guardados en bitcoin_historical_data.json")
