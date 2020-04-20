from Model.model import Model

m = Model()

m.create_genero('Accion', 'Super Heroes')
m.create_genero('Aventura', 'Exploracion')
m.create_genero('Experimental', 'Indie')

data = m.read_all_generos()
print(data)

m.close_db()