from Model.model import Model

m = Model()

"""
m.create_pais('Estados Unidos de America')
m.create_pais('Mexico')

m.create_genero('Accion', 'Super Heroes')
m.create_genero('Aventura', 'Exploracion')
m.create_genero('Experimental', 'Indie')
m.create_genero('Familiar', 'Animales')
m.create_genero('Comedia', 'Critica social')
m.create_genero('Drama', 'Tragedia')

m.create_alma_mater('Howard University', 1)
m.create_alma_mater('Newark Arts High School', 1)
m.create_alma_mater('Hampshire College', 1)
m.create_alma_mater('California State University', 1)
m.create_alma_mater('Universidad Autonoma de Mexico', 2)
m.create_alma_mater('Centro Formacion Teatral San Cayetano', 2)

m.create_directores('Ryan', 'Coogler', 4, 2009, 2020)
m.create_directores('Charles', 'Chaplin', None, 1901, 1976)
m.create_directores('Alfonso', 'Cuaron', 5, 1981, 2020)

m.create_escritores('Ryan', 'Coogler', 4, 2009, 2020)
m.create_escritores('Charles', 'Chaplin', None, 1901, 1976)
m.create_escritores('Alfonso', 'Cuaron', 5, 1981, 2020)

m.create_actores('Chadwick', 'Boseman', 1, 2000, 2020)
m.create_actores('Michael', 'Jordan', 2, 1999, 2000)
m.create_actores('Lupita', 'Nyong\'o', 3, 2005, 2020)
m.create_actores('Charles', 'Chaplin', None, 1901, 1976)
m.create_actores('Paulette', 'Goddard', None, 1926, 1972)
m.create_actores('Henry', 'Bergman', None, 1913, 1936)
m.create_actores('Yalitza', 'Aparicio', None, 2018, 2020)
m.create_actores('Marina', 'de Tavara', 6, 1998, 2020)

m.create_peliculas('Black panther', 1, 1, 2018, 1, 97)
m.create_peliculas('Modern times', 5, 2, 1936, 1, 100)
m.create_peliculas('Roma', 6, 3, 2018, 2, 95)

m.create_carrera_escritores(1, 1, 2500000)
m.create_carrera_escritores(2, 2, 100000)
m.create_carrera_escritores(3, 3, 1000000)

m.create_carrera_actores(1, 1, 1500000)
m.create_carrera_actores(2, 1, 2000000)
m.create_carrera_actores(3, 1, 1000000)
m.create_carrera_actores(4, 2, 100000)
m.create_carrera_actores(5, 2, 50000)
m.create_carrera_actores(6, 2, 50000)
m.create_carrera_actores(7, 3, 100000)
m.create_carrera_actores(8, 3, 200000)

data = m.read_all_genero()
print(data)

m.update_genero('Experimental', 'Independiente')
data = m.read_all_genero()
print(data)

m.update_genero('Aventura', 'Civilizaciones antiguas')
data = m.read_all_genero()
print(data)

data = m.read_genero_sub_gen('Super Heroes')
print(data)

m.delete_genero('Accion')
data = m.read_all_genero()
print(data)
"""

#data = m.read_all_genero()
#print(data)

#m.delete_genero(43)

data = m.read_all_pais()
print(data)

data = m.read_all_genero()
print(data)

data = m.read_all_alma_mater()
print(data)

data = m.read_all_directores()
print(data)

data = m.read_all_escritores()
print(data)

data = m.read_all_actores()
print(data)

data = m.read_all_peliculas()
print(data)

data = m.read_all_carrera_escritores()
print(data)

data = m.read_all_carrera_actores()
print(data)

university = m.read_an_alma_mater(4)
print('\n')
print(university)
director = m.read_a_directores(1)
print('\n')
print(director)

university_usa = m.read_alma_mater_pais(1)
university_mex = m.read_alma_mater_pais(2)
print('\n')
print(university_usa)
print('\n')
print(university_mex)

m.close_db()
