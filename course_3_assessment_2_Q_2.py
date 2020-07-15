# Below, we have provided a list of strings called countries. Use filter to produce a list called b_countries that
# only contains the strings from countries that begin with B.

countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia',
             'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt',
             'Morocco', 'Switzerland', 'Belgium']


def country_b(country):
    if country[0] == 'B':
        return country


b_countries = filter(country_b, countries)

print(list(b_countries))
