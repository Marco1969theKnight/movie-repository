from mysql import connector

class Model:

    """
    ******************************************
    * A data model with MySQL for a movie DB *
    ******************************************
    """

    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d
    
    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()

    """
    *******************
    * Country methods *
    *******************
    """

    def create_pais(self, nombre):
        try:
            sql = 'INSERT INTO  pais (`nombre`) VALUES(%s)'
            vals = (nombre,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_pais(self, pais):
        try:
            sql = 'SELECT * FROM pais WHERE nombre = %s'
            vals = (pais,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_pais(self):
        try:
            sql = 'SELECT * FROM pais'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    """
    def update_pais(self, nombre):
        try:
            vals = []
            vals.append(nombre)
            vals = tuple(vals)
            try:
                sql = 'UPDATE pais SET '+','.join()
        except connector.Error as err:
            return err
    """

    """
    *****************
    * Genre methods *
    *****************
    """

    def create_genero(self, nombre, sub_gen):
        try:
            sql = 'INSERT INTO  genero (`nombre`, `sub_gen`) VALUES(%s, %s)'
            vals = (nombre, sub_gen)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_genero(self, genero):
        try:
            sql = 'SELECT * FROM genero WHERE nombre = %s'
            vals = (genero,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_generos(self):
        try:
            sql = 'SELECT * FROM genero'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def update_generos(self, nombre, sub_gen):
        fields = []
        vals = []
        if sub_gen != '':
            vals.append(sub_gen)
            fields.append('sub_gen = %s')
        vals.append(nombre)
        vals = tuple(vals) 
        try:
            sql = 'UPDATE generos SET '+','.join(fields)+' WHERE nombre = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    **********************
    * University methods *
    **********************
    """

    def create_alma_mater(self, nombre, id_pais):
        try:
            sql = 'INSERT INTO  genero (`nombre`, `id_pais`) VALUES(%s, %s)'
            vals = (nombre, id_pais)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_an_alma_mater(self, alma_mater):
        try:
            sql = 'SELECT * FROM alma_mater WHERE nombre = %s'
            vals = (alma_mater,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_alma_mater(self):
        try:
            sql = 'SELECT * FROM alma_mater'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_alma_mater_pais(self, pais):
        try:
            sql = 'SELECT * FROM alma_mater WHERE id_pais = %s'
            vals = (pais,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def update_alma_mater(self, nombre, id_pais):
        fields = []
        vals = []
        if id_pais != '':
            vals.append(id_pais)
            fields.append('id_pais = %s')
        vals.append(nombre)
        vals = tuple(vals)
        try:
            sql = 'UPDATE alma_mater SET ' + \
                ','.join(fields)+' WHERE nombre = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ********************
    * Director methods *
    ********************
    """

    def create_directores(self, nombre, apellido, id_alma_mater, anio_act_in, anio_act_fin):
        try:
            sql = 'INSERT INTO  directores (`nombre`, `apellido`, `id_alma_mater`, `anio_act_in`, `anio_act_fin`) VALUES(%s, %s, %s, %s, %s)'
            vals = (nombre, apellido, id_alma_mater, anio_act_in, anio_act_fin)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_directores(self, directores_nombre, directores_apellido):
        try:
            sql = 'SELECT * FROM directores WHERE nombre = %s AND apellido = %s'
            vals = (directores_nombre, directores_apellido)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_directores(self):
        try:
            sql = 'SELECT * FROM directores'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_directores_alma_mater(self, alma_mater):
        try:
            sql = 'SELECT * FROM directores WHERE id_alma_mater = %s'
            vals = (alma_mater,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_directores_anio_act_in(self, anio_act_in):
        try:
            sql = 'SELECT * FROM directores WHERE anio_act_in = %s'
            vals = (anio_act_in,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_directores_anio_act_fin(self, anio_act_fin):
        try:
            sql = 'SELECT * FROM directores WHERE anio_act_fin = %s'
            vals = (anio_act_fin,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def update_directores(self, nombre, apellido, id_alma_mater, anio_act_in, anio_act_fin):
        fields = []
        vals = []
        if id_alma_mater != '':
            vals.append(id_alma_mater)
            fields.append('id_alma_mater = %s')
        if anio_act_in != '':
            vals.append(anio_act_in)
            fields.append('anio_act_in = %s')
        if anio_act_fin != '':
            vals.append(anio_act_fin)
            fields.append('anio_act_fin = %s')
        vals.append(nombre)
        vals.append(apellido)
        vals = tuple(vals)
        try:
            sql = 'UPDATE directores SET ' + \
                ','.join(fields)+' WHERE nombre = %s AND apellido = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ********************
    * Writers methods *
    ********************
    """

    def create_escritores(self, nombre, apellido, id_alma_mater, anio_act_in, anio_act_fin):
        try:
            sql = 'INSERT INTO  escritores (`nombre`, `apellido`, `id_alma_mater`, `anio_act_in`, `anio_act_fin`) VALUES(%s, %s, %s, %s, %s)'
            vals = (nombre, apellido, id_alma_mater, anio_act_in, anio_act_fin)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_escritores(self, escritores_nombre, escritores_apellido):
        try:
            sql = 'SELECT * FROM escritores WHERE nombre = %s AND apellido = %s'
            vals = (escritores_nombre, escritores_apellido)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_escritores(self):
        try:
            sql = 'SELECT * FROM escritores'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_escritores_alma_mater(self, alma_mater):
        try:
            sql = 'SELECT * FROM escritores WHERE id_alma_mater = %s'
            vals = (alma_mater,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_escritores_anio_act_in(self, anio_act_in):
        try:
            sql = 'SELECT * FROM escritores WHERE anio_act_in = %s'
            vals = (anio_act_in,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_escritores_anio_act_fin(self, anio_act_fin):
        try:
            sql = 'SELECT * FROM escritores WHERE anio_act_fin = %s'
            vals = (anio_act_fin,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_escritores(self, nombre, apellido, id_alma_mater, anio_act_in, anio_act_fin):
        fields = []
        vals = []
        if id_alma_mater != '':
            vals.append(id_alma_mater)
            fields.append('id_alma_mater = %s')
        if anio_act_in != '':
            vals.append(anio_act_in)
            fields.append('anio_act_in = %s')
        if anio_act_fin != '':
            vals.append(anio_act_fin)
            fields.append('anio_act_fin = %s')
        vals.append(nombre)
        vals.append(apellido)
        vals = tuple(vals)
        try:
            sql = 'UPDATE escritores SET ' + \
                ','.join(fields)+' WHERE nombre = %s AND apellido = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ******************
    * Actors methods *
    ******************
    """

    def create_actores(self, nombre, apellido, id_alma_mater, anio_act_in, anio_act_fin):
        try:
            sql = 'INSERT INTO  actores (`nombre`, `apellido`, `id_alma_mater`, `anio_act_in`, `anio_act_fin`) VALUES(%s, %s, %s, %s, %s)'
            vals = (nombre, apellido, id_alma_mater, anio_act_in, anio_act_fin)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_actores(self, actores_nombre, actores_apellido):
        try:
            sql = 'SELECT * FROM actores WHERE nombre = %s AND apellido = %s'
            vals = (actores_nombre, actores_apellido)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_actores(self):
        try:
            sql = 'SELECT * FROM actores'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_actores_alma_mater(self, alma_mater):
        try:
            sql = 'SELECT * FROM actores WHERE id_alma_mater = %s'
            vals = (alma_mater,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_actores_anio_act_in(self, anio_act_in):
        try:
            sql = 'SELECT * FROM actores WHERE anio_act_in = %s'
            vals = (anio_act_in,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_actores_anio_act_fin(self, anio_act_fin):
        try:
            sql = 'SELECT * FROM actores WHERE anio_act_fin = %s'
            vals = (anio_act_fin,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_actores(self, nombre, apellido, id_alma_mater, anio_act_in, anio_act_fin):
        fields = []
        vals = []
        if id_alma_mater != '':
            vals.append(id_alma_mater)
            fields.append('id_alma_mater = %s')
        if anio_act_in != '':
            vals.append(anio_act_in)
            fields.append('anio_act_in = %s')
        if anio_act_fin != '':
            vals.append(anio_act_fin)
            fields.append('anio_act_fin = %s')
        vals.append(nombre)
        vals.append(apellido)
        vals = tuple(vals)
        try:
            sql = 'UPDATE actores SET ' + \
                ','.join(fields)+' WHERE nombre = %s AND apellido = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ******************
    * Movies methods *
    ******************
    """

    def create_peliculas(self, titulo, id_genero, id_director, anio, id_pais, calif):
        try:
            sql = 'INSERT INTO  peliculas (`titulo`, `id_genero`, `id_director`, `anio`, `id_pais`, `calif`) VALUES(%s, %s, %s, %s, %s, %s)'
            vals = (titulo, id_genero, id_director, anio, id_pais, calif)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_peliculas(self, titulo):
        try:
            sql = 'SELECT * FROM peliculas WHERE titulo = %s'
            vals = (titulo)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_peliculas_id_genero(self, genero):
        try:
            sql = 'SELECT * FROM peliculas WHERE id_genero = %s'
            vals = (genero,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_peliculas_id_director(self, director):
        try:
            sql = 'SELECT * FROM peliculas WHERE id_director = %s'
            vals = (director,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_peliculas_anio(self, anio):
        try:
            sql = 'SELECT * FROM peliculas WHERE anio = %s'
            vals = (anio,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_peliculas_id_pais(self, pais):
        try:
            sql = 'SELECT * FROM peliculas WHERE id_pais = %s'
            vals = (pais,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_peliculas_calif(self, calif):
        try:
            sql = 'SELECT * FROM peliculas WHERE calif = %s'
            vals = (calif,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_all_peliculas(self):
        try:
            sql = 'SELECT * FROM peliculas'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_peliculas(self, titulo, id_genero, id_director, anio, id_pais, calif):
        fields = []
        vals = []
        if id_genero != '':
            vals.append(id_genero)
            fields.append('id_genero = %s')
        if id_director != '':
            vals.append(id_director)
            fields.append('id_director = %s')
        if anio != '':
            vals.append(anio)
            fields.append('anio = %s')
        if id_pais != '':
            vals.append(id_pais)
            fields.append('id_pais = %s')
        if calif != '':
            vals.append(calif)
            fields.append('calif = %s')
        vals.append(titulo)
        vals = tuple(vals)
        try:
            sql = 'UPDATE peliculas SET ' + \
                ','.join(fields)+' WHERE titulo = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    **************************
    * Writers career methods *
    **************************
    """

    def create_carrera_escritores(self, id_escritor, id_pelicula, remuneracion):
        try:
            sql = 'INSERT INTO  carrera_escritores (`id_escritor`, `id_pelicula`, `remuneracion`) VALUES(%s, %s, %s)'
            vals = (id_escritor, id_pelicula, remuneracion)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_carrera_escritores(self, escritor):
        try:
            sql = 'SELECT * FROM carrera_escritores WHERE id_escritor = %s'
            vals = (escritor,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_carrera_escritores(self):
        try:
            sql = 'SELECT * FROM carrera_escritores'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_carrera_escritores_pelicula(self, pelicula):
        try:
            sql = 'SELECT * FROM carrera_escritores WHERE id_pelicula = %s'
            vals = (pelicula,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_carrera_escritores_remuneracion(self, remuneracion):
        try:
            sql = 'SELECT * FROM carrera_escritores WHERE remuneracion = %s'
            vals = (remuneracion,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_carrera_escritores(self, id_escritor, id_pelicula, remuneracion):
        fields = []
        vals = []
        if remuneracion != '':
            vals.append(remuneracion)
            fields.append('remuneracion = %s')
        vals.append(id_escritor)
        vals.append(id_pelicula)
        vals = tuple(vals)
        try:
            sql = 'UPDATE carrera_escritores SET ' + \
                ','.join(fields)+' WHERE id_escritor = %s AND id_pelicula = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    *************************
    * Actors career methods *
    *************************
    """

    def create_carrera_actores(self, id_actor, id_pelicula, remuneracion):
        try:
            sql = 'INSERT INTO  carrera_escritores (`id_actor`, `id_pelicula`, `remuneracion`) VALUES(%s, %s, %s)'
            vals = (id_actor, id_pelicula, remuneracion)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_carrera_actores(self, actor):
        try:
            sql = 'SELECT * FROM carrera_actores WHERE id_actor = %s'
            vals = (actor,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_carrera_actores(self):
        try:
            sql = 'SELECT * FROM carrera_actores'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err


    def read_carrera_actores_pelicula(self, pelicula):
        try:
            sql = 'SELECT * FROM carrera_actores WHERE id_pelicula = %s'
            vals = (pelicula,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_carrera_actores_remuneracion(self, remuneracion):
        try:
            sql = 'SELECT * FROM carrera_actores WHERE remuneracion = %s'
            vals = (remuneracion,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_carrera_actores(self, id_actor, id_pelicula, remuneracion):
        fields = []
        vals = []
        if remuneracion != '':
            vals.append(remuneracion)
            fields.append('remuneracion = %s')
        vals.append(id_actor)
        vals.append(id_pelicula)
        vals = tuple(vals)
        try:
            sql = 'UPDATE carrera_actores SET ' + \
                ','.join(fields)+' WHERE id_escritor = %s AND id_pelicula = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
