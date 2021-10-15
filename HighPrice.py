
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
"idiom":"english",
"price": 350,
}]

def high_price(listBook):
    search_idiom = input('Escriba el idioma del cual quiere saber el libro con el precio mas alto: ').lower()

    price_sorted = sorted(arrayData, key=lambda book : book['price'], reverse=True)

    book_max_price = []
    idiom_not_found = True
    length = len(price_sorted)
    index = 0
    while idiom_not_found and index < length:

        if price_sorted[index]['idiom'] == search_idiom:
            book_max_price = price_sorted[index]
            idiom_not_found = False
        index += 1


    return book_max_price

print(high_price(arrayData))
