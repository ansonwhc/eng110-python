person = {
    "name": "John",
    "job": "Consultant",
    "age": 23,
}


def print_person():
    person['job'] = 'zoo keeper'
    person['hobby'] = ['video games', 'board games', 'gym']
    person.update([("name", "John Dough")])
    print(person.get("height"))
    print(person)


def print_movie():
    film = {}
    film['Title'] = 'Rocky'
    film['Actor'] = {
        'main': 'Sylvester Stallone',
        'supporting': ['Talia Shire', 'Burt Young']
    }
    film['Director'] = 'John G. Avildsen'
    film['Runtime (hours)'] = round(1 + 59/60, 2)
    print(film)
    print(film.items())


if __name__ == "__main__":
    print_movie()
