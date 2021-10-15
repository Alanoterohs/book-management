
arrayData = [{
"isbn": "1234-5678-1234-5678",
"title": "los alquimistas",
"gender": "economia",
"idiom":"spanish",
"price": 100,
},
{
"isbn": "1234-5678-1234-0000",
"title": "el hombre en busca del sentido",
"gender": "arte",
"idiom":"spanish",
"price": 150,
},
{
"isbn": "0000-5678-1234-0000",
"title": "AAA",
"gender": "autoayuda",
"idiom":"spanish",
"price": 350,
}]

def high_price(listBook):
    price_sorted = sorted(arrayData, key=lambda book : book['price'], reverse=True)
    dictionary_with_max_price = price_sorted[0]
    return dictionary_with_max_price
