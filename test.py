from Model.model import Model

m = Model()

m.create_genero('Accion', 'Super Heroes')
m.create_genero('Aventura', 'Exploracion')
m.create_genero('Experimental', 'Indie')

"""
data = m.read_all_genero()
print(data)

m.update_genero('Experimental', 'Independiente')
data = m.read_all_genero()
print(data)

m.update_genero('Aventura', 'Civilizaciones antiguas')
data = m.read_all_genero()
print(data)
"""

data = m.read_genero_sub_gen('Super Heroes')
print(data)

m.delete_genero('Accion')
data = m.read_all_genero()
print(data)

m.close_db()
