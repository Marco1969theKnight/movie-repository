from Model.model import Model
from View.view import View
from datetime import date

class Controller:
    """
    *******************************
    * A controller for a movie DB *
    *******************************
    """

    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        self.view.start()
        self.main_menu()

    """
    ***********************
    * General controllers *
    ***********************
    """

    def main_menu(self):
        o = '100'
        while o != '0':
            self.view.main_menu()
            self.view.option('9')
            o = input()
            if o == '1':
                self.view.pais_menu()
            elif o == '2':
                self.view.genero_menu()
            elif o == '3':
                self.view.alma_mater_menu()
            elif o == '4':
                self.view.directores_menu()
            elif o == '5':
                self.view.escritores_menu()
            elif o == '6':
                self.view.actores_menu()
            elif o == '7':
                self.view.peliculas_menu()
            elif o == '8':
                self.view.carrera_escritores_menu()
            elif o == '9':
                self.view.carrera_actores_menu()
            elif o == '0':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    def update_list(self, fs, vs):    
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields, vals

    """
    *****************************
    * Controllers for countries *
    *****************************
    """

    def pais_menu(self):
        o = '100'
        while o != '0':
            self.view.pais_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_pais()
            elif o == '2':
                self.read_a_pais()
            elif o == '3':
                self.read_all_pais()
            elif o == '4':
                self.read_pais_nombre()
            elif o == '5':
                self.update_pais()
            elif o == '6':
                self.delete_pais()
            elif o == '0':
                return
            else:
                self.view.not_valid_option()
        return
    
    def create_pais(self):
        self.view.ask('Nombre: ')
        nombre = input()
        out = self.model.create_pais(nombre)
        if type(out) == int:
            self.view.ok(nombre, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('EL PAIS ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR EL PAIS. REVISA')
        return

    def read_a_pais(self):
        self.view.ask('ID del pais: ')
        id_pais = input()
        pais = self.model.read_a_pais(id_pais)
        if type(pais) == tuple:
            self.view.show_pais_header(' Datos del Pais '+id_pais+' ')
            self.view.show_a_pais(pais)
            self.view.show_pais_midder()
            self.view.show_pais_footer()
        else:
            if pais == None:
                self.view.error('PAIS NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL PAIS. REVISA')
        return

    def read_all_pais(self):
        paises = self.model.read_all_pais()
        if type(paises) == list:
            self.view.show_pais_header(' Todos los Paises ')
            for pais in paises:
                self.view.show_a_pais(pais)
            self.view.show_pais_midder()
            self.view.show_pais_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS PAISES. REVISA')
        return

    def read_pais_nombre(self):
        self.view.ask('Nombre: ')
        nombre = input()
        paises = self.model.read_pais_nombre(nombre)
        if type(paises) == list:
            self.view.show_pais_header(' Paises con el nombre de '+nombre+' ')
            for pais in paises:
                self.view.show_a_pais(pais)
            self.view.show_pais_midder()
            self.view.show_pais_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS PAISES. REVISA')
        return

    def update_pais(self):
        self.view.ask('ID del pais: ')
        id_pais = input()
        pais = self.model.read_a_pais(id_pais)
        if type(pais) == tuple:
            self.view.show_pais_header(' Nombre del pais '+id_pais+' ')
            self.view.show_a_pais(pais)
            self.view.show_pais_midder()
            self.view.show_pais_footer()
        else:
            if pais == None:
                self.view.error('EL PAIS NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL PAIS. REVISA')
            return
        self.view.msg(
            'Ingresa los valores a modificar (vacio para dejarlo igual):')
        self.view.ask('Nombre: ')
        nombre = input()
        fields, vals = self.update_list(['nombre'], nombre)
        vals.append(id_pais)
        vals = tuple(vals)
        out = self.model.update_pais(fields, vals)
        if type(out) == int:
            self.view.ok(id_pais, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL PAIS. REVISA')
        return

    def delete_pais(self):
        self.view.ask('ID del pais: ')
        id_pais = input()
        count = self.model.delete_pais(id_pais)
        if count != 0:
            self.view.ok(id_pais, 'borro')
        else:
            if count == 0:
                self.view.error('EL PAIS NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL PAIS. REVISA')
        return

    """
    **************************
    * Controllers for genres *
    **************************
    """

    def genero_menu(self):
        o = '100'
        while o != '0':
            self.view.genero_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_genero()
            elif o == '2':
                self.read_a_genero()
            elif o == '3':
                self.read_all_genero()
            elif o == '4':
                self.read_genero_nombre()
            elif o == '5':
                self.read_genero_sub_gen()
            elif o == '6':
                self.update_genero()
            elif o == '7':
                self.delete_genero()
            elif o == '0':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_genero(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Subgenero: ')
        subgenero = input()
        return[nombre, subgenero]
    
    def create_genero(self):
        nombre, subgenero = self.ask_genero()
        out = self.model.create_genero(nombre, subgenero)
        if type(out) == int:
            self.view.ok(nombre, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('EL GENERO ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR EL GENERO. REVISA')
        return

    def read_a_genero(self):
        self.view.ask('ID del genero: ')
        id_genero = input()
        genero = self.model.read_a_genero(id_genero)
        if type(genero) == tuple:
            self.view.show_genero_header(' Datos del Pais '+id_genero+' ')
            self.view.show_a_genero(genero)
            self.view.show_genero_midder()
            self.view.show_genero_footer()
        else:
            if genero == None:
                self.view.error('GENERO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL GENERO. REVISA')
        return

    def read_all_genero(self):
        generos = self.model.read_all_genero()
        if type(generos) == list:
            self.view.show_genero_header(' Todos los Generos ')
            for genero in generos:
                self.view.show_a_genero(genero)
            self.view.show_genero_midder()
            self.view.show_genero_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS GENEROS. REVISA')
        return

    def read_genero_nombre(self):
        self.view.ask('Nombre: ')
        nombre = input()
        generos = self.model.read_genero_nombre(nombre)
        if type(generos) == list:
            self.view.show_genero_header(' Generos con el nombre de '+nombre+' ')
            for genero in generos:
                self.view.show_a_genero(genero)
            self.view.show_genero_midder()
            self.view.show_genero_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS GENEROS. REVISA')
        return

    def read_genero_sub_gen(self):
        self.view.ask('Subgenero: ')
        subgenero = input()
        generos = self.model.read_genero_sub_gen(subgenero)
        if type(generos) == list:
            self.view.show_genero_header(' Generos con el subgenero de '+subgenero+' ')
            for genero in generos:
                self.view.show_a_genero(genero)
            self.view.show_genero_midder()
            self.view.show_genero_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS GENEROS. REVISA')
        return

    def update_genero(self):
        self.view.ask('ID del genero a modificar: ')
        id_genero = input()
        genero = self.model.read_a_genero(id_genero)
        if type(genero) == tuple:
            self.view.show_genero_header(' Datos del genero '+id_genero+' ')
            self.view.show_a_genero(genero)
            self.view.show_genero_midder()
            self.view.show_genero_footer()
        else:
            if genero == None:
                self.view.error('EL GENERO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL GENERO. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_genero()
        fields, vals = self.update_list(['nombre', 'sub_gen'], whole_vals)
        vals.append(id_genero)
        vals = tuple(vals)
        out = self.model.update_genero(fields, vals)
        if type(out) == int:
            self.view.ok(id_genero, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL GENERO. REVISA')
        return

    def delete_genero(self):
        self.view.ask('ID del genero: ')
        id_genero = input()
        count = self.model.delete_genero(id_genero)
        if count != 0:
            self.view.ok(id_genero, 'borro')
        else:
            if count == 0:
                self.view.error('EL GENERO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL GENERO. REVISA')
        return

    """
    ********************************
    * Controllers for universities *
    ********************************
    """

    def alma_mater_menu(self):
        o = '100'
        while o != '0':
            self.view.alma_mater_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_alma_mater()
            elif o == '2':
                self.read_an_alma_mater()
            elif o == '3':
                self.read_all_alma_mater()
            elif o == '4':
                self.read_alma_mater_nombre()
            elif o == '5':
                self.read_alma_mater_pais()
            elif o == '6':
                self.update_alma_mater()
            elif o == '7':
                self.delete_alma_mater()
            elif o == '0':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_alma_mater(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('ID Pais')
        id_pais = input()
        return [nombre, id_pais]

    def create_alma_mater(self):
        nombre, id_pais = self.ask_alma_mater()
        out = self.model.create_alma_mater(nombre, id_pais)
        if type(out) == int:
            self.view.ok(nombre, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('LA UNIVERSIDAD ESTA REPETIDA')
            else:
                self.view.error('NO SE PUDO AGREGAR LA UNIVERSIDAD. REVISA')
        return
    
    def read_an_alma_mater(self):
        self.view.ask('ID universidad: ')
        id_alma_mater = input()
        alma_mater = self.model.read_an_alma_mater(id_alma_mater)
        if type(alma_mater) == tuple:
            self.view.show_alma_mater_header(' Datos de la universidad '+id_alma_mater+' ')
            self.view.show_a_alma_mater(alma_mater)
            self.view.show_alma_mater_midder()
            self.view.show_alma_mater_footer()
        else:
            if alma_mater == None:
                self.view.error('LA UNIVERSIDAD NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA UNIVERSIDAD. REVISA')
        return

    def read_all_alma_mater(self):
        alma_maters = self.model.read_all_alma_mater()
        if type(alma_maters) == list:
            self.view.show_alma_mater_header(' Todas las universidades ')
            for alma_mater in alma_maters:
                self.view.show_a_alma_mater(alma_mater)
            self.view.show_alma_mater_midder()
            self.view.show_alma_mater_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS UNIVERSIDADES')
        return

    def read_alma_mater_nombre(self):
        self.view.ask('Nombre: ')
        nombre = input()
        alma_maters = self.model.read_alma_mater_nombre(nombre)
        if type(alma_maters) == list:
            self.view.show_alma_mater_header(' Universidades con el nombre de '+nombre+' ')
            for alma_mater in alma_maters:
                self.view.show_a_alma_mater(alma_mater)
            self.view.show_alma_mater_midder()
            self.view.show_alma_mater_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS UNIVERSIDADES. REVISA')
        return

    def read_alma_mater_pais(self):
        self.view.ask('ID Pais: ')
        id_pais = input()
        alma_maters = self.model.read_alma_mater_pais(id_pais)
        if type(alma_maters) == list:
            self.view.show_genero_header(
                ' Universidades con el pais '+id_pais+' ')
            for alma_mater in alma_maters:
                self.view.show_a_alma_mater(alma_mater)
            self.view.show_alma_mater_midder()
            self.view.show_alma_mater_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS UNIVERSIDADES. REVISA')
        return

    def update_alma_mater(self):
        self.view.ask('ID de la universidad a modificar: ')
        id_alma_mater = input()
        alma_mater = self.model.read_an_alma_mater(id_alma_mater)
        if type(alma_mater) == tuple:
            self.view.show_alma_mater_header(' Datos de la universidad '+id_alma_mater+' ')
            self.view.show_a_alma_mater(alma_mater)
            self.view.show_alma_mater_midder()
            self.view.show_alma_mater_footer()
        else:
            if alma_mater == None:
                self.view.error('LA UNIVERSIDAD NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA UNIVERSIDAD. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_alma_mater()
        fields, vals = self.update_list(['nombre', 'id_pais'], whole_vals)
        vals.append(id_alma_mater)
        vals = tuple(vals)
        out = self.model.update_alma_mater(fields, vals)
        if type(out) == int:
            self.view.ok(id_alma_mater, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA UNIVERSIDAD. REVISA')
        return

    def delete_alma_mater(self):
        self.view.ask('ID de la universidad: ')
        id_alma_mater = input()
        count = self.model.delete_alma_mater(id_alma_mater)
        if count != 0:
            self.view.ok(id_alma_mater, 'borro')
        else:
            if count == 0:
                self.view.error('LA UNIVERSIDAD NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA UNIVERSIDAD. REVISA')
        return


    """
    *****************************
    * Controllers for directors *
    *****************************
    """

    def directores_menu(self):
        o = '100'
        while o != '0':
            self.view.directores_menu()
            self.view.option('11')
            o = input()
            if o == '1':
                self.create_directores()
            elif o == '2':
                self.read_a_directores()
            elif o == '3':
                self.read_all_directores()
            elif o == '4':
                self.read_directores_nombre()
            elif o == '5':
                self.read_directores_apellido()
            elif o == '6':
                self.read_directores_alma_mater()
            elif o == '7':
                self.read_directores_anio_act_in()
            elif o == '8':
                self.read_directores_anio_act_fin()
            elif o == '9':
                self.read_directores_anio_act_range()
            elif o == '10':
                self.update_directores()
            elif o == '11':
                self.delete_directores()
            elif o == '0':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_directores(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Apellido: ')
        apellido = input()
        self.view.ask('ID Universidad: ')
        id_alma_mater = input()
        self.view.ask('Año de inicio: ')
        anio_act_in = int(input())
        self.view.ask('Año fin: ')
        anio_act_fin = int(input())
        return [nombre, apellido, id_alma_mater, anio_act_in, anio_act_fin]

    def create_directores(self):
        nombre, apellido, id_alma_mater, anio_act_in, anio_act_fin = self.ask_directores()
        out = self.model.create_directores(
            nombre, apellido, id_alma_mater, anio_act_in, anio_act_fin)
        if type(out) == int:
            self.view.ok(nombre+' '+apellido,'agrego')
        else:
            if out.errno == 1062:
                self.view.error('EL DIRECTOR ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR EL DIRECTOR. REVISA')
        return

    def read_a_directores(self):
        self.view.ask('ID director: ')
        id_director = input()
        director = self.model.read_a_directores(id_director)
        if type(director) == tuple:
            self.view.show_directores_header(
                ' Datos del director '+id_director+' ')
            self.view.show_a_directores(director)
            self.view.show_directores_midder()
            self.view.show_directores_footer()
        else:
            if director == None:
                self.view.error('EL DIRECTOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL DIRECTOR. REVISA')
        return

    def read_all_directores(self):
        directores = self.model.read_all_directores()
        if type(directores) == list:
            self.view.show_directores_header(' Todos los directores ')
            for director in directores:
                self.view.show_a_directores(director)
                self.view.show_directores_midder()
            self.view.show_directores_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL DIRECTOR')
        return

    def read_directores_nombre(self):
        self.view.ask('Nombre: ')
        nombre = input()
        directores = self.model.read_directores_nombre(nombre)
        if type(directores) == list:
            self.view.show_directores_header(
                ' Directores que tienen el nombre '+nombre+' ')
            for director in directores:
                self.view.show_a_directores(director)
                self.view.show_directores_midder()
            self.view.show_directores_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL DIRECTOR. REVISA')
        return

    def read_directores_apellido(self):
        self.view.ask('Apellido: ')
        apellido = input()
        directores = self.model.read_directores_apellido(apellido)
        if type(directores) == list:
            self.view.show_directores_header(
                ' Directores que tienen el apellido '+apellido+' ')
            for director in directores:
                self.view.show_a_directores(director)
                self.view.show_directores_midder()
            self.view.show_directores_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL DIRECTOR. REVISA')
        return

    def read_directores_alma_mater(self):
        self.view.ask('ID universidad: ')
        id_alma_mater = input()
        directores = self.model.read_directores_alma_mater(id_alma_mater)
        if type(directores) == list:
            self.view.show_directores_header(
                ' Directores que tienen como Alma Mater '+id_alma_mater+' ')
            for director in directores:
                self.view.show_a_directores(director)
                self.view.show_directores_midder()
            self.view.show_directores_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL DIRECTOR. REVISA')
        return

    def read_directores_anio_act_in(self):
        self.view.ask('Año de inicio: ')
        anio_act_in = int(input())
        directores = self.model.read_directores_anio_act_in(anio_act_in)
        if type(directores) == list:
            self.view.show_directores_header(
                ' Directores que su carrera empezo en '+anio_act_in+' ')
            for director in directores:
                self.view.show_a_directores(director)
                self.view.show_directores_midder()
            self.view.show_directores_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL DIRECTOR. REVISA')
        return

    def read_directores_anio_act_fin(self):
        self.view.ask('Año fin: ')
        anio_act_fin = int(input())
        directores = self.model.read_directores_anio_act_fin(anio_act_fin)
        if type(directores) == list:
            self.view.show_directores_header(
                ' Directores que su carrera finalizo en '+anio_act_fin+' ')
            for director in directores:
                self.view.show_a_directores(director)
                self.view.show_directores_midder()
            self.view.show_directores_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL DIRECTOR. REVISA')
        return

    def read_directores_anio_act_range(self):
        self.view.ask('Año de inicio: ')
        anio_act_in = int(input())
        self.view.ask('Año fin: ')
        anio_act_fin = int(input())
        directores = self.model.read_directores_anio_act_range(anio_act_in, anio_act_fin)
        if type(directores) == list:
            self.view.show_directores_header(
                ' Directores donde su carrera se encuentra entre '+anio_act_in+' y '+anio_act_fin+' ')
            for director in directores:
                self.view.show_a_directores(director)
                self.view.show_directores_midder()
            self.view.show_directores_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL DIRECTOR. REVISA')
        return

    def update_directores(self):
        self.view.ask('ID del director modificar: ')
        id_director = input()
        director = self.model.read_a_directores(id_director)
        if type(director) == tuple:
            self.view.show_directores_header(
                ' Datos del director '+id_director+' ')
            self.view.show_a_directores(director)
            self.view.show_directores_midder()
            self.view.show_directores_footer()
        else:
            if director == None:
                self.view.error('EL DIRECTOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL DIRECTOR. REVISA')
            return
        self.view.msg(
            'Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_directores()
        fields, vals = self.update_list(['nombre', 'apellido', 'id_alma_mater', 'anio_act_in', 'anio_act_fin'], whole_vals)
        vals.append(id_director)
        vals = tuple(vals)
        out = self.model.update_directores(fields, vals)
        if type(out) == int:
            self.view.ok(id_director, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL DIRECTOR. REVISA')
        return

    def delete_directores(self):
        self.view.ask('ID del director: ')
        id_director = input()
        count = self.model.delete_directores(id_director)
        if count != 0:
            self.view.ok(id_director, 'borro')
        else:
            if count == 0:
                self.view.error('EL DIRECTOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL DIRECTOR. REVISA')
        return

    """
    ****************************
    * Controllers for writers  *
    ****************************
    """

    def escritores_menu(self):
        o = '100'
        while o != '0':
            self.view.escritores_menu()
            self.view.option('11')
            o = input()
            if o == '1':
                self.create_escritores()
            elif o == '2':
                self.read_a_escritores()
            elif o == '3':
                self.read_all_escritores()
            elif o == '4':
                self.read_escritores_nombre()
            elif o == '5':
                self.read_escritores_apellido()
            elif o == '6':
                self.read_escritores_alma_mater()
            elif o == '7':
                self.read_escritores_anio_act_in()
            elif o == '8':
                self.read_escritores_anio_act_fin()
            elif o == '9':
                self.read_escritores_anio_act_range()
            elif o == '10':
                self.update_escritores()
            elif o == '11':
                self.delete_escritores()
            elif o == '0':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_escritores(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Apellido: ')
        apellido = input()
        self.view.ask('ID Universidad: ')
        id_alma_mater = input()
        self.view.ask('Año de inicio: ')
        anio_act_in = int(input())
        self.view.ask('Año fin: ')
        anio_act_fin = int(input())
        return [nombre, apellido, id_alma_mater, anio_act_in, anio_act_fin]

    def create_escritores(self):
        nombre, apellido, id_alma_mater, anio_act_in, anio_act_fin = self.ask_escritores()
        out = self.model.create_escritores(
            nombre, apellido, id_alma_mater, anio_act_in, anio_act_fin)
        if type(out) == int:
            self.view.ok(nombre+' '+apellido, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('EL ESCRITOR ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR EL ESCRITOR. REVISA')
        return

    def read_a_escritores(self):
        self.view.ask('ID escritor: ')
        id_escritor = input()
        escritor = self.model.read_a_escritores(id_escritor)
        if type(escritor) == tuple:
            self.view.show_escritores_header(
                ' Datos del escritor '+id_escritor+' ')
            self.view.show_a_escritores(escritor)
            self.view.show_escritores_midder()
            self.view.show_escritores_footer()
        else:
            if escritor == None:
                self.view.error('EL ESCRITOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL ESCRITOR. REVISA')
        return

    def read_all_escritores(self):
        escritores = self.model.read_all_escritores()
        if type(escritores) == list:
            self.view.show_escritores_header(' Todos los escritores ')
            for escritor in escritores:
                self.view.show_a_escritores(escritor)
                self.view.show_escritores_midder()
            self.view.show_escritores_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL ESCRITOR')
        return

    def read_escritores_nombre(self):
        self.view.ask('Nombre: ')
        nombre = input()
        escritores = self.model.read_escritores_nombre(nombre)
        if type(escritores) == list:
            self.view.show_escritores_header(
                ' Escritores que tienen el nombre '+nombre+' ')
            for escritor in escritores:
                self.view.show_a_escritores(escritor)
                self.view.show_escritores_midder()
            self.view.show_escritores_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL ESCRITOR. REVISA')
        return

    def read_escritores_apellido(self):
        self.view.ask('Apellido: ')
        apellido = input()
        escritores = self.model.read_escritores_apellido(apellido)
        if type(escritores) == list:
            self.view.show_escritores_header(
                ' Escritores que tienen el apellido '+apellido+' ')
            for escritor in escritores:
                self.view.show_a_escritores(escritor)
                self.view.show_escritores_midder()
            self.view.show_escritores_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL ESCRITOR. REVISA')
        return

    def read_escritores_alma_mater(self):
        self.view.ask('ID universidad: ')
        id_alma_mater = input()
        escritores = self.model.read_escritores_alma_mater(id_alma_mater)
        if type(escritores) == list:
            self.view.show_escritores_header(
                ' Escritores que tienen como Alma Mater '+id_alma_mater+' ')
            for escritor in escritores:
                self.view.show_a_escritores(escritor)
                self.view.show_escritores_midder()
            self.view.show_escritores_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL ESCRITOR. REVISA')
        return

    def read_escritores_anio_act_in(self):
        self.view.ask('Año de inicio: ')
        anio_act_in = int(input())
        escritores = self.model.read_escritores_anio_act_in(anio_act_in)
        if type(escritores) == list:
            self.view.show_escritores_header(
                ' Escritores que su carrera empezo en '+anio_act_in+' ')
            for escritor in escritores:
                self.view.show_a_escritores(escritor)
                self.view.show_escritores_midder()
            self.view.show_escritores_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL ESCRITOR. REVISA')
        return

    def read_escritores_anio_act_fin(self):
        self.view.ask('Año fin: ')
        anio_act_fin = int(input())
        escritores = self.model.read_escritores_anio_act_fin(anio_act_fin)
        if type(escritores) == list:
            self.view.show_escritores_header(
                ' Escritores que su carrera finalizo en '+anio_act_fin+' ')
            for escritor in escritores:
                self.view.show_a_escritores(escritor)
                self.view.show_escritores_midder()
            self.view.show_escritores_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL ESCRITOR. REVISA')
        return

    def read_escritores_anio_act_range(self):
        self.view.ask('Año de inicio: ')
        anio_act_in = int(input())
        self.view.ask('Año fin: ')
        anio_act_fin = int(input())
        escritores = self.model.read_escritores_anio_act_range(
            anio_act_in, anio_act_fin)
        if type(escritores) == list:
            self.view.show_escritores_header(
                ' Escritores donde su carrera se encuentra entre '+anio_act_in+' y '+anio_act_fin+' ')
            for escritor in escritores:
                self.view.show_a_escritores(escritor)
                self.view.show_escritores_midder()
            self.view.show_escritores_footer()
        else:
            self.view.error('PROBLEMA AL LEER EL ESCRITOR. REVISA')
        return

    def update_escritores(self):
        self.view.ask('ID del escritor modificar: ')
        id_escritor = input()
        escritor = self.model.read_a_escritores(id_escritor)
        if type(escritor) == tuple:
            self.view.show_escritores_header(
                ' Datos del escritor '+id_escritor+' ')
            self.view.show_a_escritores(escritor)
            self.view.show_escritores_midder()
            self.view.show_escritores_footer()
        else:
            if escritor == None:
                self.view.error('EL ESCRITOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL ESCRITOR. REVISA')
            return
        self.view.msg(
            'Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_escritores()
        fields, vals = self.update_list(
            ['nombre', 'apellido', 'id_alma_mater', 'anio_act_in', 'anio_act_fin'], whole_vals)
        vals.append(id_escritor)
        vals = tuple(vals)
        out = self.model.update_escritores(fields, vals)
        if type(out) == int:
            self.view.ok(id_escritor, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL ESCRITOR. REVISA')
        return

    def delete_escritores(self):
        self.view.ask('ID del escritor: ')
        id_escritor = input()
        count = self.model.delete_escritores(id_escritor)
        if count != 0:
            self.view.ok(id_escritor, 'borro')
        else:
            if count == 0:
                self.view.error('EL ESCRITOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL ESCRITOR. REVISA')
        return


    """
    ***************************
    * Controllers for actors  *
    ***************************
    """

    def actores_menu(self):
        o = '100'
        while o != '0':
            self.view.actores_menu()
            self.view.option('11')
            o = input()
            if o == '1':
                self.create_actores()
            elif o == '2':
                self.read_a_actores()
            elif o == '3':
                self.read_all_actores()
            elif o == '4':
                self.read_actores_nombre()
            elif o == '5':
                self.read_actores_apellido()
            elif o == '6':
                self.read_actores_alma_mater()
            elif o == '7':
                self.read_actores_anio_act_in()
            elif o == '8':
                self.read_actores_anio_act_fin()
            elif o == '9':
                self.read_actores_anio_act_range()
            elif o == '10':
                self.update_actores()
            elif o == '11':
                self.delete_actores()
            elif o == '0':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_actores(self):
        self.view.ask('Nombre: ')
        nombre = input()
        self.view.ask('Apellido: ')
        apellido = input()
        self.view.ask('ID Universidad: ')
        id_alma_mater = input()
        self.view.ask('Año de inicio: ')
        anio_act_in = int(input())
        self.view.ask('Año fin: ')
        anio_act_fin = int(input())
        return [nombre, apellido, id_alma_mater, anio_act_in, anio_act_fin]

    def create_actores(self):
        nombre, apellido, id_alma_mater, anio_act_in, anio_act_fin = self.ask_actores()
        out = self.model.create_actores(
            nombre, apellido, id_alma_mater, anio_act_in, anio_act_fin)
        if type(out) == int:
            self.view.ok(nombre+' '+apellido, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('EL ACTOR ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR AL ACTOR. REVISA')
        return

    def read_a_actores(self):
        self.view.ask('ID actor: ')
        id_actor = input()
        actor = self.model.read_a_actores(id_actor)
        if type(actor) == tuple:
            self.view.show_actores_header(
                ' Datos del actor '+id_actor+' ')
            self.view.show_a_actores(actor)
            self.view.show_actores_midder()
            self.view.show_actores_footer()
        else:
            if actor == None:
                self.view.error('EL ACTOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER AL ACTOR. REVISA')
        return

    def read_all_actores(self):
        actores = self.model.read_all_actores()
        if type(actores) == list:
            self.view.show_actores_header(' Todos los actores ')
            for actor in actores:
                self.view.show_a_actores(actor)
                self.view.show_actores_midder()
            self.view.show_actores_footer()
        else:
            self.view.error('PROBLEMA AL LEER A LOS ACTORES')
        return

    def read_actores_nombre(self):
        self.view.ask('Nombre: ')
        nombre = input()
        actores = self.model.read_actores_nombre(nombre)
        if type(actores) == list:
            self.view.show_actores_header(
                ' Actores que tienen el nombre '+nombre+' ')
            for actor in actores:
                self.view.show_a_actores(actor)
                self.view.show_actores_midder()
            self.view.show_actores_footer()
        else:
            self.view.error('PROBLEMA AL LEER A LOS ACTORES. REVISA')
        return

    def read_actores_apellido(self):
        self.view.ask('Apellido: ')
        apellido = input()
        actores = self.model.read_actores_apellido(apellido)
        if type(actores) == list:
            self.view.show_actores_header(
                ' Actores que tienen el apellido '+apellido+' ')
            for actor in actores:
                self.view.show_a_actores(actor)
                self.view.show_actores_midder()
            self.view.show_actores_footer()
        else:
            self.view.error('PROBLEMA AL LEER A LOS ACTORES. REVISA')
        return

    def read_actores_alma_mater(self):
        self.view.ask('ID universidad: ')
        id_alma_mater = input()
        actores = self.model.read_actores_alma_mater(id_alma_mater)
        if type(actores) == list:
            self.view.show_actores_header(
                ' Actores que tienen como Alma Mater '+id_alma_mater+' ')
            for actor in actores:
                self.view.show_a_actores(actor)
                self.view.show_actores_midder()
            self.view.show_actores_footer()
        else:
            self.view.error('PROBLEMA AL LEER A LOS ACTORES. REVISA')
        return

    def read_actores_anio_act_in(self):
        self.view.ask('Año de inicio: ')
        anio_act_in = int(input())
        actores = self.model.read_actores_anio_act_in(anio_act_in)
        if type(actores) == list:
            self.view.show_actores_header(
                ' Actores que su carrera empezo en '+anio_act_in+' ')
            for actor in actores:
                self.view.show_a_actores(actor)
                self.view.show_actores_midder()
            self.view.show_actores_footer()
        else:
            self.view.error('PROBLEMA AL LEER A LOS ACTORES. REVISA')
        return

    def read_actores_anio_act_fin(self):
        self.view.ask('Año fin: ')
        anio_act_fin = int(input())
        actores = self.model.read_actores_anio_act_fin(anio_act_fin)
        if type(actores) == list:
            self.view.show_actores_header(
                ' Actores que su carrera finalizo en '+anio_act_fin+' ')
            for actor in actores:
                self.view.show_a_actores(actor)
                self.view.show_actores_midder()
            self.view.show_actores_footer()
        else:
            self.view.error('PROBLEMA AL LEER A LOS ACTORES. REVISA')
        return

    def read_actores_anio_act_range(self):
        self.view.ask('Año de inicio: ')
        anio_act_in = int(input())
        self.view.ask('Año fin: ')
        anio_act_fin = int(input())
        actores = self.model.read_actores_anio_act_range(
            anio_act_in, anio_act_fin)
        if type(actores) == list:
            self.view.show_actores_header(
                ' Actores donde su carrera se encuentra entre '+anio_act_in+' y '+anio_act_fin+' ')
            for actor in actores:
                self.view.show_a_actores(actor)
                self.view.show_actores_midder()
            self.view.show_actores_footer()
        else:
            self.view.error('PROBLEMA AL LEER A LOS ACTORES. REVISA')
        return

    def update_actores(self):
        self.view.ask('ID del actor modificar: ')
        id_actor = input()
        actor = self.model.read_a_actores(id_actor)
        if type(actor) == tuple:
            self.view.show_actores_header(
                ' Datos del actor '+id_actor+' ')
            self.view.show_a_actores(actor)
            self.view.show_actores_midder()
            self.view.show_actores_footer()
        else:
            if actor == None:
                self.view.error('EL ACTOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER AL ACTOR. REVISA')
            return
        self.view.msg(
            'Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_actores()
        fields, vals = self.update_list(
            ['nombre', 'apellido', 'id_alma_mater', 'anio_act_in', 'anio_act_fin'], whole_vals)
        vals.append(id_actor)
        vals = tuple(vals)
        out = self.model.update_actores(fields, vals)
        if type(out) == int:
            self.view.ok(id_actor, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR AL ACTOR. REVISA')
        return

    def delete_actores(self):
        self.view.ask('ID del actor: ')
        id_actor = input()
        count = self.model.delete_actores(id_actor)
        if count != 0:
            self.view.ok(id_actor, 'borro')
        else:
            if count == 0:
                self.view.error('EL ACTOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR AL ACTOR. REVISA')
        return

    """
    ***************************
    * Controllers for movies  *
    ***************************
    """

    def peliculas_menu(self):
        o = '100'
        while o != '0':
            self.view.peliculas_menu()
            self.view.option('12')
            o = input()
            if o == '1':
                self.create_peliculas()
            elif o == '2':
                self.read_a_peliculas()
            elif o == '3':
                self.read_all_peliculas()
            elif o == '4':
                self.read_peliculas_titulo()
            elif o == '5':
                self.read_peliculas_id_genero()
            elif o == '6':
                self.read_peliculas_id_director()
            elif o == '7':
                self.read_peliculas_anio()
            elif o == '8':
                self.read_peliculas_anio_range()
            elif o == '9':
                self.read_peliculas_id_pais()
            elif o == '10':
                self.read_peliculas_calif()
            elif o == '11':
                self.update_peliculas()
            elif o == '12':
                self.delete_peliculas()
            elif o == '0':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_peliculas(self):
        self.view.ask('Titulo: ')
        titulo = input()
        self.view.ask('ID Genero: ')
        id_genero = input()
        self.view.ask('ID Director: ')
        id_director = input()
        self.view.ask('Año de lanzamiento: ')
        anio = input()
        self.view.ask('ID Pais: ')
        id_pais = input()
        self.view.ask('Calificacion: ')
        calif = int(input())
        return [titulo, id_genero, id_director, anio, id_pais, calif]

    def create_peliculas(self):
        titulo, id_genero, id_director, anio, id_pais, calif = self.ask_peliculas()
        out = self.model.create_peliculas(
            titulo, id_genero, id_director, anio, id_pais, calif)
        if type(out) == int:
            self.view.ok(titulo, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('LA PELICULA ESTA REPETIDA')
            else:
                self.view.error('NO SE PUDO AGREGAR LA PELICULA. REVISA')
        return

    def read_a_peliculas(self):
        self.view.ask('ID pelicula: ')
        id_pelicula = input()
        pelicula = self.model.read_a_peliculas(id_pelicula)
        if type(pelicula) == tuple:
            self.view.show_peliculas_header(
                ' Datos de la pelicula '+id_pelicula+' ')
            self.view.show_a_peliculas(pelicula)
            self.view.show_peliculas_midder()
            self.view.show_peliculas_footer()
        else:
            if pelicula == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA')
        return

    def read_all_peliculas(self):
        peliculas = self.model.read_all_peliculas()
        if type(peliculas) == list:
            self.view.show_peliculas_header(' Todas las peliculas ')
            for pelicula in peliculas:
                self.view.show_a_peliculas(pelicula)
                self.view.show_peliculas_midder()
            self.view.show_peliculas_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS PELICULAS')
        return

    def read_peliculas_titulo(self):
        self.view.ask('Titulo: ')
        titulo = input()
        peliculas = self.model.read_peliculas_titulo(titulo)
        if type(peliculas) == list:
            self.view.show_peliculas_header(
                ' Peliculas que tienen el titulo '+titulo+' ')
            for pelicula in peliculas:
                self.view.show_a_peliculas(pelicula)
                self.view.show_peliculas_midder()
            self.view.show_peliculas_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA')
        return

    def read_peliculas_id_genero(self):
        self.view.ask('ID Genero: ')
        id_genero = input()
        peliculas = self.model.read_peliculas_id_genero(id_genero)
        if type(peliculas) == list:
            self.view.show_peliculas_header(
                ' Peliculas que tienen el genero '+id_genero+' ')
            for pelicula in peliculas:
                self.view.show_a_peliculas(pelicula)
                self.view.show_peliculas_midder()
            self.view.show_peliculas_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA')
        return

    def read_peliculas_id_director(self):
        self.view.ask('ID Director: ')
        id_director = input()
        peliculas = self.model.read_peliculas_id_director(id_director)
        if type(peliculas) == list:
            self.view.show_peliculas_header(
                ' Peliculas que tienen como director '+id_director+' ')
            for pelicula in peliculas:
                self.view.show_a_peliculas(pelicula)
                self.view.show_peliculas_midder()
            self.view.show_peliculas_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA')
        return

    def read_peliculas_anio(self):
        self.view.ask('Año de lanzamiento: ')
        anio = int(input())
        peliculas = self.model.read_peliculas_anio(anio)
        if type(peliculas) == list:
            self.view.show_peliculas_header(
                ' Peliculas que se publicaron en el año '+anio+' ')
            for pelicula in peliculas:
                self.view.show_a_peliculas(pelicula)
                self.view.show_peliculas_midder()
            self.view.show_peliculas_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA')
        return

    def read_peliculas_anio_range(self):
        self.view.ask('Desde el año: ')
        anio_in = int(input())
        self.view.ask('Hasta el año: ')
        anio_fin = int(input())
        peliculas = self.model.read_peliculas_anio_range(
            anio_in, anio_fin)
        if type(peliculas) == list:
            self.view.show_peliculas_header(
                ' Peliculas donde su año de lanzamiento se encuentra entre '+anio_in+' y '+anio_fin+' ')
            for pelicula in peliculas:
                self.view.show_a_peliculas(pelicula)
                self.view.show_peliculas_midder()
            self.view.show_peliculas_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS PELICULAS. REVISA')
        return

    def read_peliculas_id_pais(self):
        self.view.ask('ID Pais: ')
        id_pais = input()
        peliculas = self.model.read_peliculas_id_pais(id_pais)
        if type(peliculas) == list:
            self.view.show_peliculas_header(
                ' Peliculas donde su pais se filmo en '+id_pais+' ')
            for pelicula in peliculas:
                self.view.show_a_peliculas(pelicula)
                self.view.show_peliculas_midder()
            self.view.show_peliculas_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS PELICULAS. REVISA')
        return

    def read_peliculas_calif(self):
        self.view.ask('Calificacion: ')
        calif = int(input())
        peliculas = self.model.read_peliculas_calif(calif)
        if type(peliculas) == list:
            self.view.show_peliculas_header(
                ' Peliculas que su calificacion fue '+calif+' ')
            for pelicula in peliculas:
                self.view.show_a_peliculas(pelicula)
                self.view.show_peliculas_midder()
            self.view.show_peliculas_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS PELICULAS. REVISA')
        return

    def update_peliculas(self):
        self.view.ask('ID de la pelicula a modificar: ')
        id_pelicula = input()
        pelicula = self.model.read_a_peliculas(id_pelicula)
        if type(pelicula) == tuple:
            self.view.show_peliculas_header(
                ' Datos de la pelicula '+id_pelicula+' ')
            self.view.show_a_peliculas(pelicula)
            self.view.show_peliculas_midder()
            self.view.show_peliculas_footer()
        else:
            if pelicula == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA')
            return
        self.view.msg(
            'Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_peliculas()
        fields, vals = self.update_list(
            ['titulo', 'id_genero', 'id_director', 'anio', 'id_pais', 'calif'], whole_vals)
        vals.append(id_pelicula)
        vals = tuple(vals)
        out = self.model.update_peliculas(fields, vals)
        if type(out) == int:
            self.view.ok(id_pelicula, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA PELICULA. REVISA')
        return

    def delete_peliculas(self):
        self.view.ask('ID de la pelicula: ')
        id_pelicula = input()
        count = self.model.delete_peliculas(id_pelicula)
        if count != 0:
            self.view.ok(id_pelicula, 'borro')
        else:
            if count == 0:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA PELICULA. REVISA')
        return

    """
    ***********************************
    * Controllers for writers career  *
    ***********************************
    """

    def carrera_escritores_menu(self):
        o = '100'
        while o != '0':
            self.view.carrera_escritores_menu()
            self.view.option('10')
            o = input()
            if o == '1':
                self.create_carrera_escritores()
            elif o == '2':
                self.read_all_carrera_escritores()
            elif o == '3':
                self.read_a_carrera_escritores()
            elif o == '4':
                self.read_carrera_escritores_escritor()
            elif o == '5':
                self.read_carrera_escritores_pelicula()
            elif o == '6':
                self.read_carrera_escritores_remuneracion()
            elif o == '7':
                self.read_carrera_escritores_remuneracion_range()
            elif o == '8':
                self.update_carrera_escritores()
            elif o == '9':
                self.delete_carrera_escritores()
            elif o == '10':
                self.delete_carrera_escritores_escritor()
            elif o == '0':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_carrera_escritores(self):
        self.view.ask('ID Escritor: ')
        id_escritor = input()
        self.view.ask('ID Pelicula: ')
        id_pelicula = input()
        self.view.ask('Remuneracion: ')
        remuneracion = int(input())
        return [id_escritor, id_pelicula, remuneracion]

    def create_carrera_escritores(self):
        id_escritor, id_pelicula, remuneracion = self.ask_carrera_escritores()
        out = self.model.create_carrera_escritores(
            id_escritor, id_pelicula, remuneracion)
        if type(out) == int:
            self.view.ok(id_escritor+' '+id_pelicula, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('LA CARRERA DEL ESCRITOR ESTA REPETIDA')
            else:
                self.view.error('NO SE PUDO AGREGAR LA CARRERA DEL ESCRITOR. REVISA')
        return

    def read_all_carrera_escritores(self):
        carrera_escritores = self.model.read_all_carrera_escritores()
        if type(carrera_escritores) == list:
            self.view.show_carrera_escritores_header(' La carrera completa de todos los escritores ')
            for carrera_escritor in carrera_escritores:
                self.view.show_a_carrera_escritores(carrera_escritor)
                self.view.show_carrera_escritores_midder()
            self.view.show_carrera_escritores_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS CARRERAS DE LOS ESCRITORES')
        return

    def read_a_carrera_escritores(self):
        self.view.ask('ID Escritor: ')
        id_escritor = input()
        self.view.ask('ID Pelicula: ')
        id_pelicula = input()
        carrera_escritores = self.model.read_a_carrera_escritores(id_escritor, id_pelicula)
        if type(carrera_escritores) == tuple:
            self.view.show_carrera_escritores_header(
                ' Datos de la participacion del escritor '+id_escritor+' en la pelicula '+id_pelicula+' ')
            self.view.show_a_carrera_escritores(carrera_escritores)
            self.view.show_carrera_escritores_midder()
            self.view.show_carrera_escritores_footer()
        else:
            if carrera_escritores == None:
                self.view.error('LA PARTICIPACION DEL ESCRITOR NO EXISTE')
            else:
                self.view.error(
                    'PROBLEMA AL LEER LA PARTICIPACION DEL ESCRITOR. REVISA')
        return

    def read_carrera_escritores_escritor(self):
        self.view.ask('ID escritor: ')
        id_escritor = input()
        carrera_escritor = self.model.read_carrera_escritores_escritor(
            id_escritor)
        if type(carrera_escritor) == list:
            self.view.show_carrera_escritores_header(
                ' La carrera completa del escritor '+id_escritor+' ')
            for carrera in carrera_escritor:
                self.view.show_a_carrera_escritores(carrera)
                self.view.show_carrera_escritores_midder()
            self.view.show_carrera_escritores_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA CARRERA DEL ESCRITOR. REVISA')
        return

    def read_carrera_escritores_pelicula(self):
        self.view.ask('ID Pelicula: ')
        id_pelicula = input()
        carrera_escritor = self.model.read_carrera_escritores_pelicula(
            id_pelicula)
        if type(carrera_escritor) == list:
            self.view.show_carrera_escritores_header(
                ' Los escritores que participaron en la pelicula '+id_pelicula+' ')
            for carrera in carrera_escritor:
                self.view.show_a_carrera_escritores(carrera)
                self.view.show_carrera_escritores_midder()
            self.view.show_carrera_escritores_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS ESCRITORES DE LA PELICULA. REVISA')
        return

    def read_carrera_escritores_remuneracion(self):
        self.view.ask('Remuneracion: ')
        remuneracion = int(input())
        carrera_escritor = self.model.read_carrera_escritores_remuneracion(
            remuneracion)
        if type(carrera_escritor) == list:
            self.view.show_carrera_escritores_header(
                ' Los escritores que tuvieron como remuneracion '+remuneracion+' ')
            for carrera in carrera_escritor:
                self.view.show_a_carrera_escritores(carrera)
                self.view.show_carrera_escritores_midder()
            self.view.show_carrera_escritores_footer()
        else:
            self.view.error(
                'PROBLEMA AL LEER LOS ESCRITORES. REVISA')
        return

    def read_carrera_escritores_remuneracion_range(self):
        self.view.ask('Remuneracion minima: ')
        rem_min = int(input())
        self.view.ask('Remuneracion maxima: ')
        rem_max = int(input())
        carrera_escritor = self.model.read_carrera_escritores_remuneracion_range(
            rem_min, rem_max)
        if type(carrera_escritor) == list:
            self.view.show_carrera_escritores_header(
                ' Los escritores que su remuneracion esta entre '+rem_min+' y '+rem_max)
            for carrera in carrera_escritor:
                self.view.show_a_carrera_escritores(carrera)
                self.view.show_carrera_escritores_midder()
            self.view.show_carrera_escritores_footer()
        else:
            self.view.error(
                'PROBLEMA AL LEER LOS ESCRITORES. REVISA')
        return

    def update_carrera_escritores(self):
        self.view.ask('ID Escritor: ')
        id_escritor = input()
        self.view.ask('ID Pelicula: ')
        id_pelicula = input()
        carrera_escritores = self.model.update_carrera_escritores(
            id_escritor, id_pelicula)
        if type(carrera_escritores) == tuple:
            self.view.show_carrera_escritores_header(
                ' Datos del escritor '+id_escritor+' que participo en la pelicula '+id_pelicula+' ')
            self.view.show_a_carrera_escritores(carrera_escritores)
            self.view.show_carrera_escritores_midder()
            self.view.show_carrera_escritores_footer()
        else:
            if carrera_escritores == None:
                self.view.error('LA PARTICIPACION DEL ESCRITOR NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA PARTICIPACION DEL ESCRITOR. REVISA')
            return
        self.view.msg(
            'Ingresa los valores a modificar (vacio para dejarlo igual):')
        self.view.ask('Remuneracion: ')
        whole_vals = int(input())
        fields, vals = self.update_list(
            ['remuneracion'], whole_vals)
        vals.append(id_escritor, id_pelicula)
        vals = tuple(vals)
        out = self.model.update_peliculas(fields, vals)
        if type(out) == int:
            self.view.ok(id_escritor+' '+id_pelicula, 'actualizo')
        else:
            self.view.error(
                'NO SE PUDO ACTUALIZAR LA PARTICIPACION DEL ESCRITOR. REVISA')
        return

    def delete_carrera_escritores(self):
        self.view.ask('ID Escritor: ')
        id_escritor = input()
        self.view.ask('ID Pelicula: ')
        id_pelicula = input()
        count = self.model.delete_carrera_escritores(id_escritor, id_pelicula)
        if count != 0:
            self.view.ok(id_escritor, 'borro')
        else:
            if count == 0:
                self.view.error('LA PARTICIPACION DEL ESCRITOR NO EXISTE')
            else:
                self.view.error(
                    'PROBLEMA AL BORRAR LA PARTICIPACION DEL ESCRITOR. REVISA')
        return

    def delete_carrera_escritores_escritor(self):
        self.view.ask('ID Escritor: ')
        id_escritor = input()
        count = self.model.delete_carrera_escritores_escritor(
            id_escritor)
        if count != 0:
            self.view.ok(id_escritor, 'borro')
        else:
            if count == 0:
                self.view.error('EL ESCRITOR NO EXISTE')
            else:
                self.view.error(
                    'PROBLEMA AL BORRAR LA CARRERA DEL ESCRITOR. REVISA')
        return
    
    """
    **********************************
    * Controllers for actors career  *
    **********************************
    """

    def carrera_actores_menu(self):
        o = '100'
        while o != '0':
            self.view.carrera_actores_menu()
            self.view.option('10')
            o = input()
            if o == '1':
                self.create_carrera_actores()
            elif o == '2':
                self.read_all_carrera_actores()
            elif o == '3':
                self.read_a_carrera_actores()
            elif o == '4':
                self.read_carrera_actores_actor()
            elif o == '5':
                self.read_carrera_actores_pelicula()
            elif o == '6':
                self.read_carrera_actores_remuneracion()
            elif o == '7':
                self.read_carrera_actores_remuneracion_range()
            elif o == '8':
                self.update_carrera_actores()
            elif o == '9':
                self.delete_carrera_actores()
            elif o == '10':
                self.delete_carrera_actores_actor()
            elif o == '0':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_carrera_actores(self):
        self.view.ask('ID Actor: ')
        id_actor = input()
        self.view.ask('ID Pelicula: ')
        id_pelicula = input()
        self.view.ask('Remuneracion: ')
        remuneracion = int(input())
        return [id_actor, id_pelicula, remuneracion]

    def create_carrera_actores(self):
        id_actor, id_pelicula, remuneracion = self.ask_carrera_actores()
        out = self.model.create_carrera_actores(
            id_actor, id_pelicula, remuneracion)
        if type(out) == int:
            self.view.ok(id_actor+' '+id_pelicula, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('LA CARRERA DEL ACTOR ESTA REPETIDA')
            else:
                self.view.error(
                    'NO SE PUDO AGREGAR LA CARRERA DEL ACTOR. REVISA')
        return

    def read_all_carrera_actores(self):
        carrera_escritores = self.model.read_all_carrera_escritores()
        if type(carrera_escritores) == list:
            self.view.show_carrera_escritores_header(
                ' La carrera completa de todos los escritores ')
            for carrera_escritor in carrera_escritores:
                self.view.show_a_carrera_escritores(carrera_escritor)
                self.view.show_carrera_escritores_midder()
            self.view.show_carrera_escritores_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS CARRERAS DE LOS ESCRITORES')
        return

    def read_a_carrera_actores(self):
        self.view.ask('ID Actor: ')
        id_actor = input()
        self.view.ask('ID Pelicula: ')
        id_pelicula = input()
        carrera_actores = self.model.read_a_carrera_actores(
            id_actor, id_pelicula)
        if type(carrera_actores) == tuple:
            self.view.show_carrera_actores_header(
                ' Datos de la participacion del actor '+id_actor+' en la pelicula '+id_pelicula+' ')
            self.view.show_a_carrera_actores(carrera_actores)
            self.view.show_carrera_actores_midder()
            self.view.show_carrera_actores_footer()
        else:
            if carrera_actores == None:
                self.view.error('LA PARTICIPACION DEL ACTOR NO EXISTE')
            else:
                self.view.error(
                    'PROBLEMA AL LEER LA PARTICIPACION DEL ACTOR. REVISA')
        return

    def read_carrera_actores_actor(self):
        self.view.ask('ID actor: ')
        id_actor = input()
        carrera_actor = self.model.read_carrera_actores_actor(
            id_actor)
        if type(carrera_actor) == list:
            self.view.show_carrera_actores_header(
                ' La carrera completa del actor '+id_actor+' ')
            for carrera in carrera_actor:
                self.view.show_a_carrera_actores(carrera)
                self.view.show_carrera_actores_midder()
            self.view.show_carrera_actores_footer()
        else:
            self.view.error('PROBLEMA AL LEER LA CARRERA DEL ACTOR. REVISA')
        return

    def read_carrera_actores_pelicula(self):
        self.view.ask('ID Pelicula: ')
        id_pelicula = input()
        carrera_actor = self.model.read_carrera_actores_pelicula(
            id_pelicula)
        if type(carrera_actor) == list:
            self.view.show_carrera_actores_header(
                ' Los actores que participaron en la pelicula '+id_pelicula+' ')
            for carrera in carrera_actor:
                self.view.show_a_carrera_actores(carrera)
                self.view.show_carrera_actores_midder()
            self.view.show_carrera_actores_footer()
        else:
            self.view.error(
                'PROBLEMA AL LEER LOS ACTORES DE LA PELICULA. REVISA')
        return

    def read_carrera_actores_remuneracion(self):
        self.view.ask('Remuneracion: ')
        remuneracion = int(input())
        carrera_actor = self.model.read_carrera_actores_remuneracion(
            remuneracion)
        if type(carrera_actor) == list:
            self.view.show_carrera_actores_header(
                ' Los actores que tuvieron como remuneracion '+remuneracion+' ')
            for carrera in carrera_actor:
                self.view.show_a_carrera_actores(carrera)
                self.view.show_carrera_actores_midder()
            self.view.show_carrera_actores_footer()
        else:
            self.view.error(
                'PROBLEMA AL LEER LOS ACTORES. REVISA')
        return

    def read_carrera_actores_remuneracion_range(self):
        self.view.ask('Remuneracion minima: ')
        rem_min = int(input())
        self.view.ask('Remuneracion maxima: ')
        rem_max = int(input())
        carrera_actor = self.model.read_carrera_actores_remuneracion_range(
            rem_min, rem_max)
        if type(carrera_actor) == list:
            self.view.show_carrera_actores_header(
                ' Los actores que su remuneracion esta entre '+rem_min+' y '+rem_max)
            for carrera in carrera_actor:
                self.view.show_a_carrera_actores(carrera)
                self.view.show_carrera_actores_midder()
            self.view.show_carrera_actores_footer()
        else:
            self.view.error(
                'PROBLEMA AL LEER LOS ACTORES. REVISA')
        return

    def update_carrera_actores(self):
        self.view.ask('ID Actor: ')
        id_actor = input()
        self.view.ask('ID Pelicula: ')
        id_pelicula = input()
        carrera_actores = self.model.update_carrera_actores(
            id_actor, id_pelicula)
        if type(carrera_actores) == tuple:
            self.view.show_carrera_actores_header(
                ' Datos del actor '+id_actor+' que participo en la pelicula '+id_pelicula+' ')
            self.view.show_a_carrera_actores(carrera_actores)
            self.view.show_carrera_actores_midder()
            self.view.show_carrera_actores_footer()
        else:
            if carrera_actores == None:
                self.view.error('LA PARTICIPACION DEL ACTOR NO EXISTE')
            else:
                self.view.error(
                    'PROBLEMA AL LEER LA PARTICIPACION DEL ACTOR. REVISA')
            return
        self.view.msg(
            'Ingresa los valores a modificar (vacio para dejarlo igual):')
        self.view.ask('Remuneracion: ')
        whole_vals = int(input())
        fields, vals = self.update_list(
            ['remuneracion'], whole_vals)
        vals.append(id_actor, id_pelicula)
        vals = tuple(vals)
        out = self.model.update_peliculas(fields, vals)
        if type(out) == int:
            self.view.ok(id_actor+' '+id_pelicula, 'actualizo')
        else:
            self.view.error(
                'NO SE PUDO ACTUALIZAR LA PARTICIPACION DEL ACTOR. REVISA')
        return

    def delete_carrera_actores(self):
        self.view.ask('ID Actor: ')
        id_actor = input()
        self.view.ask('ID Pelicula: ')
        id_pelicula = input()
        count = self.model.delete_carrera_actores(id_actor, id_pelicula)
        if count != 0:
            self.view.ok(id_actor, 'borro')
        else:
            if count == 0:
                self.view.error('LA PARTICIPACION DEL ACTOR NO EXISTE')
            else:
                self.view.error(
                    'PROBLEMA AL BORRAR LA PARTICIPACION DEL ACTOR. REVISA')
        return

    def delete_carrera_actores_actor(self):
        self.view.ask('ID Actor: ')
        id_actor = input()
        count = self.model.delete_carrera_actores_actor(
            id_actor)
        if count != 0:
            self.view.ok(id_actor, 'borro')
        else:
            if count == 0:
                self.view.error('EL ACTOR NO EXISTE')
            else:
                self.view.error(
                    'PROBLEMA AL BORRAR LA CARRERA DEL ACTOR. REVISA')
        return
