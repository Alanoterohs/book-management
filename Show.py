# 2.) Mostrar: Mostrar el vector generado en el punto anterior de tal manera que se muestre el género y el idioma del libro en lugar de los números que los representan y se listen ordenados por título en forma ascendente. Cada libro debe mostrarse a razón de una línea por registro.

# Código de identificación o ISBN (cadena de caracteres).
# Título.
# Género (0: Autoayuda, 1:Arte, 2: Ficción, 3: Computación, 4: Economía, 5: Escolar, 6: Sociedad, 7: Gastronomía, 8: Infantil , 9: Otros).
# Idioma (1: español, 2: inglés, 3: francés, 4:italiano, 5:otros).
# Precio.

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
