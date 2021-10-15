arrayData = [{
"isbn": "1234-5678-1234-5678",
"title": "los alquimistas",
"gender": "economy",
"idiom":"spanish",
"price": 100,
},
{
"isbn": "1234-5678-1234-0000",
"title": "el hombre en busca del sentido",
"gender": "Autoayuda",
"idiom":"spanish",
"price": 150,
},
{
"isbn": "0000-5678-1234-0000",
"title": "AAA",
"gender": "Autoayuda",
"idiom":"spanish",
"price": 350,
}]

def show(ArrayBook):
    books_sorted = sorted(arrayData, key=lambda book : book['title'])
    for book in books_sorted:
        print('Title: ' + book['title'])
        print('Gender: ' + book['gender'])
        print('Idiom: ' + book['idiom'])
        print('-------------------------------')

show(arrayData)
