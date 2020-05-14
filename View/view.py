class View:
    """
    *************************
    * A view for a movie DB *
    *************************
    """

    def start(self):
        print('==================================================')
        print('= ¡Bienvenido a nuestra biblioteca de peliculas! =')
        print('==================================================')
    
    def end(self):
        print('==================================================')
        print('=    Que tengas un buen dia ¡Hasta la proxima!   =')
        print('==================================================')

    def main_menu(self):
        print('********************************')
        print('*   --   Menu Principal   --   *')
        print('********************************')
        print('1. Paises')
        print('2. Generos')
        print('3. Universidades')
        print('4. Directores')
        print('5. Escritores')
        print('6. Actores')
        print('7. Peliculas')
        print('8. Carrera de los escritores')
        print('9. Carrera de los actores')
        print('0. Salir')

    def option(self, last):
        print('Selecciona una opcion (1-'+last+'): ', end = '')

    def not_valid_option(self):
        print('¡Opcion no valida!\nIntenta otra opcion')

    def ask(self, output):
        print(output, end = '')
    
    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))

    def error(self, err):
        print(' ¡Error! '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))

    """
    ************************
    * Views for countries *
    ************************
    """

    def pais_menu(self):
        print('********************************')
        print('*   --   Submenu Paises   --   *')
        print('********************************')
        print('1. Agregar pais')
        print('2. Mostrar pais')
        print('3. Mostrar todos los paises')
        print('4. Mostrar pais por nombre')
        print('5. Actualizar nombre del pais')
        print('6. Eliminar pais')
        print('0. Regresar')

    def show_a_pais(self, record):
        print(f'{record[0]:<6}|{record[1]:<30}')

    def show_pais_header(self, header):
        print(header.center(38,'*'))
        print('ID Pais'.ljust(6)+'|'+'Nombre'.ljust(30))
        print('-'*38)

    def show_pais_midder(self):
        print('-'*38)

    def show_pais_footer(self):
        print('*'*38)

    """
    ********************
    * Views for genres *
    ********************
    """

    def genero_menu(self):
        print('*********************************')
        print('*   --   Submenu Generos   --   *')
        print('*********************************')
        print('1. Agregar genero')
        print('2. Mostrar genero')
        print('3. Mostrar todos los generos')
        print('4. Mostrar generos por nombre')
        print('5. Mostrar generos por subgenero')
        print('6. Actualizar genero')
        print('7. Eliminar genero')
        print('0. Regresar')

    def show_a_genero(self, record):
        print(f'{record[0]:<6}|{record[1]:<30}|{record[2]:<30}')

    def show_genero_header(self, header):
        print(header.center(68, '*'))
        print('ID Genero'.ljust(6)+'|'+
              'Nombre'.ljust(30)+'|'+'Subgenero'.ljust(30))
        print('-'*68)

    def show_genero_midder(self):
        print('-'*68)

    def show_genero_footer(self):
        print('*'*68)

    """
    **************************
    * Views for universities *
    **************************
    """

    def alma_mater_menu(self):
        print('***************************************')
        print('*   --   Submenu Universidades   --   *')
        print('***************************************')
        print('1. Agregar alma mater')
        print('2. Mostrar alma mater')
        print('3. Mostrar todas las alma mater')
        print('4. Mostrar alma maters por nombre')
        print('5. Mostrar alma maters por pais')
        print('6. Actualizar alma mater')
        print('7. Eliminar alma mater')
        print('0. Regresar')
        
    def show_a_alma_mater(self, record):
        print(f'{record[0]:<6}|{record[1]:<40}|{record[2]:<30}')

    def show_alma_mater_header(self, header):
        print(header.center(78, '*'))
        print('ID Alma mater'.ljust(6)+'|' +
              'Nombre'.ljust(40)+'|'+'Pais'.ljust(30))
        print('-'*78)

    def show_alma_mater_midder(self):
        print('-'*78)

    def show_alma_mater_footer(self):
        print('*'*78)

    """
    ***********************
    * Views for directors *
    ***********************
    """

    def directores_menu(self):
        print('************************************************')
        print('*      --      Submenu Directores      --      *')
        print('************************************************')
        print('1. Agregar director')
        print('2. Mostrar director')
        print('3. Mostrar todos los directores')
        print('4. Mostrar directores por nombre')
        print('5. Mostrar directores por apellido')
        print('6. Mostrar directores por alma mater')
        print('7. Mostrar directores por año inical de carrera')
        print('8. Mostrar directores por año final de carrera')
        print('9. Mostrar directores por rango de años')
        print('10. Actualizar director')
        print('11. Eliminar director')
        print('0. Regresar')

    def show_a_directores(self, record):
        print('ID: ', record[0])
        print('Nombre: ', record[1])
        print('Apellido: ', record[2])
        print('Alma mater: ', record[3])
        print('Año de inicio de carrera: ', record[4])
        print('Año final de carrera: ', record[5])

    def show_directores_header(self, header):
        print(header.center(54, '*'))
        print('-'*54)

    def show_directores_midder(self):
        print('-'*54)

    def show_directores_footer(self):
        print('*'*54)

    """
    *********************
    * Views for writers *
    *********************
    """

    def escritores_menu(self):
        print('************************************************')
        print('*      --      Submenu Escritores      --      *')
        print('************************************************')
        print('1. Agregar escritor')
        print('2. Mostrar escritor')
        print('3. Mostrar todos los escritores')
        print('4. Mostrar escritores por nombre')
        print('5. Mostrar escritores por apellido')
        print('6. Mostrar escritores por alma mater')
        print('7. Mostrar escritores por año inical de carrera')
        print('8. Mostrar escritores por año final de carrera')
        print('9. Mostrar escritores por rango de años')
        print('10. Actualizar escritor')
        print('11. Eliminar escritor')
        print('0. Regresar')

    def show_a_escritores(self, record):
        print('ID: ', record[0])
        print('Nombre: ', record[1])
        print('Apellido: ', record[2])
        print('Alma mater: ', record[3])
        print('Año de inicio de carrera: ', record[4])
        print('Año final de carrera: ', record[5])

    def show_escritores_header(self, header):
        print(header.center(54, '*'))
        print('-'*54)

    def show_escritores_midder(self):
        print('-'*54)

    def show_escritores_footer(self):
        print('*'*54)

    """
    ********************
    * Views for actors *
    ********************
    """

    def actores_menu(self):
        print('*********************************************')
        print('*      --      Submenu actores      --      *')
        print('*********************************************')
        print('1. Agregar actor')
        print('2. Mostrar actor')
        print('3. Mostrar todos los actores')
        print('4. Mostrar actores por nombre')
        print('5. Mostrar actores por apellido')
        print('6. Mostrar actores por alma mater')
        print('7. Mostrar actores por año inical de carrera')
        print('8. Mostrar actores por año final de carrera')
        print('9. Mostrar actores por rango de años')
        print('10. Actualizar actor')
        print('11. Eliminar actor')
        print('0. Regresar')

    def show_a_actores(self, record):
        print('ID: ', record[0])
        print('Nombre: ', record[1])
        print('Apellido: ', record[2])
        print('Alma mater: ', record[3])
        print('Año de inicio de carrera: ', record[4])
        print('Año final de carrera: ', record[5])

    def show_actores_header(self, header):
        print(header.center(54, '*'))
        print('-'*54)

    def show_actores_midder(self):
        print('-'*54)

    def show_actores_footer(self):
        print('*'*54)

    """
    ********************
    * Views for movies *
    ********************
    """

    def peliculas_menu(self):
        print('***********************************************')
        print('*      --      Submenu peliculas      --      *')
        print('***********************************************')
        print('1. Agregar pelicula')
        print('2. Mostrar pelicula')
        print('3. Mostrar todas las peliculas')
        print('4. Mostrar peliculas por titulo')
        print('5. Mostrar peliculas por genero')
        print('6. Mostrar peliculas por director')
        print('7. Mostrar peliculas por año')
        print('8. Mostrar peliculas por rango de años')
        print('9. Mostrar peliculas por pais')
        print('10. Mostrar peliculas por calificacion')
        print('11. Actualizar pelicula')
        print('12. Eliminar pelicula')
        print('0. Regresar')

    def show_a_peliculas(self, record):
        print('ID: ', record[0])
        print('Titulo: ', record[1])
        print('Genero: ', record[2])
        print('Director: '+record[3]+' '+record[4])
        print('Año: ', record[5])
        print('Pais: ', record[6])
        print('Calificacion: ', record[7])

    def show_peliculas_header(self, header):
        print(header.center(113, '*'))
        print('-'*113)

    def show_peliculas_midder(self):
        print('-'*113)

    def show_peliculas_footer(self):
        print('*'*113)

    """
    ****************************
    * Views for writers career *
    ****************************
    """

    def carrera_escritores_menu(self):
        print('*******************************************************************')
        print('*       --       Submenu de carreras de escritores       --       *')
        print('*******************************************************************')
        print('1. Agregar participacion del escritor')
        print('2. Mostrar la carrera de todos los escritores')
        print('3. Mostrar participacion del escritor en una pelicula')
        print('4. Mostrar la carrera del escritor')
        print('5. Mostrar los escritores de una pelicula')
        print('6. Mostrar participacion de escritores por remuneracion')
        print('7. Mostrar participacion de escritores por rango de remuneracion')
        print('8. Actualizar una participacion de un escritor')
        print('9. Eliminar una participacion de un escritor')
        print('10. Eliminar la carrera de un escritor')
        print('0. Regresar')

    def show_a_carrera_escritores(self, record):
        print('ID escritor: ', record[0])
        print('Escritor: '+record[1]+' '+record[2])
        print('ID pelicula: ', record[3])
        print('Pelicula: ', record[4])
        print('Remuneracion: ', record[5])

    def show_carrera_escritores_header(self, header):
        print(header.center(113, '*'))
        print('-'*113)

    def show_carrera_escritores_midder(self):
        print('-'*113)

    def show_carrera_escritores_footer(self):
        print('*'*113)

    """
    ***************************
    * Views for actors career *
    ***************************
    """

    def carrera_actores_menu(self):
        print('****************************************************************')
        print('*       --       Submenu de carreras de actores       --       *')
        print('****************************************************************')
        print('1. Agregar participacion del actor')
        print('2. Mostrar la carrera de todos los actores')
        print('3. Mostrar participacion del actor en una pelicula')
        print('4. Mostrar la carrera del actor')
        print('5. Mostrar los actores de una pelicula')
        print('6. Mostrar participacion de actores por remuneracion')
        print('7. Mostrar participacion de actores por rango de remuneracion')
        print('8. Actualizar una participacion de un actor')
        print('9. Eliminar una participacion de un actor')
        print('10. Eliminar la carrera de un actor')
        print('0. Regresar')

    def show_a_carrera_actores(self, record):
        print('ID actor: ', record[0])
        print('Actor: ' +record[1]+' '+record[2])
        print('ID pelicula: ', record[3])
        print('Pelicula: ', record[4])
        print('Remuneracion: ', record[5])

    def show_carrera_actores_header(self, header):
        print(header.center(110, '*'))
        print('-'*110)

    def show_carrera_actores_midder(self):
        print('-'*110)

    def show_carrera_actores_footer(self):
        print('*'*110)
