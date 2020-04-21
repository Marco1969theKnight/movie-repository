from Model.model import Model

m = Model()
value = None
"""
m.create_pais('Estados Unidos de America')
m.create_pais('Mexico')


m.create_alma_mater('Howard University', 1)
m.create_alma_mater('Newark Arts High School', 1)
m.create_alma_mater('Hampshire College', 1)
m.create_alma_mater('California State University', 1)
m.create_alma_mater('Universidad Autonoma de Mexico', 2)
m.create_alma_mater('Centro de Formacion Teatral San Cayetano', 2)
"""
#m.create_directores('Ryan', 'Coogler', 4, 2009, 2020)
m.create_directores('Charles', 'Chaplin', value, 1899, 1976)
#m.create_directores('Alfonso', 'Cuaron', 5, 1981, 2020)
"""
m.create_genero('Accion', 'Super Heroes')
m.create_genero('Aventura', 'Exploracion')
m.create_genero('Experimental', 'Indie')

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

m.close_db()
