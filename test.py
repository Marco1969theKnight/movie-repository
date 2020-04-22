from Model.model import Model

m = Model()
"""
m.create_pais('Estados Unidos de America')
m.create_pais('Mexico')


m.create_alma_mater('Howard University', 1)
m.create_alma_mater('Newark Arts High School', 1)
m.create_alma_mater('Hampshire College', 1)
m.create_alma_mater('California State University', 1)
m.create_alma_mater('Universidad Autonoma de Mexico', 2)
m.create_alma_mater('Centro Form Teatral San Cayetano', 2)

m.create_directores('Ryan', 'Coogler', 4, 2009, 2020)
m.create_directores('Charles', 'Chaplin', None, 1901, 1976)
m.create_directores('Alfonso', 'Cuaron', 5, 1981, 2020)

m.create_genero('Accion', 'Super Heroes')
m.create_genero('Aventura', 'Exploracion')
m.create_genero('Experimental', 'Indie')
m.create_genero('Familiar', 'Animales')

data = m.read_all_genero()
print(data)

m.update_genero('Experimental', 'Independiente')
data = m.read_all_genero()
print(data)

m.update_genero('Aventura', 'Civilizaciones antiguas')
data = m.read_all_genero()
print(data)
"""
"""
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

university = m.read_an_alma_mater(4)
print(university)
director = m.read_a_directores(5)
print(director)

m.close_db()
