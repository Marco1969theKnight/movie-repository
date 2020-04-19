create database if not exists peliculas_db;

use peliculas_db;

create table if not exists pais(
	id_pais int not null auto_increment,
    nombre varchar(25) not null,
    primary key(id_pais)
) engine = INNODB; 

create table if not exists genero(
	id_genero int not null auto_increment,
    nombre varchar(25) not null,
    sub_gen varchar(25),
    
    primary key(id_genero)
) engine = INNODB;

create table if not exists alma_mater(
	id_alma_mater int not null auto_increment,
    nombre varchar(35) not null,
    id_pais int not null,
    
    primary key(id_alma_mater),
    
    constraint fk_id_pais foreign key(id_pais)
		references pais(id_pais)
) engine=INNODB;

create table if not exists directores ( 
	id_director int not null auto_increment,
    nombre varchar(30) not null,
    apellido varchar(30) not null,
    id_alma_mater int,
    anio_act_in year(4) not null,
    anio_act_fin year(4) not null,
    
    primary key(id_director),
    
    constraint fk_id_alma_mater_directores foreign key(id_alma_mater)
		references alma_mater(id_alma_mater)
        on delete set null
        on update cascade
) engine=INNODB;

create table if not exists escritores (
	id_escritor int not null auto_increment,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    id_alma_mater int,
    anio_act_in year(4) not null,
    anio_act_fin year(4) not null,
    
    primary key(id_escritor),
    
    constraint fk_id_alma_mater_escrirotes foreign key(id_alma_mater)
		references alma_mater(id_alma_mater)
        on delete set null
        on update cascade
) engine=INNODB;

create table if not exists actores(
	id_actor int not null auto_increment,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    id_alma_mater int,
    anio_act_in year(4) not null,
    anio_act_fin year(4) not null,
    
    primary key(id_actor),
    
    constraint fk_id_alma_mater_actores foreign key(id_alma_mater)
		references alma_mater(id_alma_mater)
        on delete set null
        on update cascade
)engine=INNODB;


create table if not exists peliculas(
	id_pelicula int not null auto_increment,
    titulo varchar(30) not null,
    id_genero int,
    id_director int,
    anio year(4) not null,
    id_pais int not null,
    calif int not null,
    
    primary key(id_pelicula),
    
    constraint fk_id_genero foreign key(id_genero)
		references genero(id_genero)
        on delete set null
        on update cascade,
        
	constraint fk_id_director foreign key(id_director)
		references directores(id_director)
        on delete set null
        on update cascade,
        
	constraint fk_id_pais_peliculas foreign key(id_pais)
		references pais(id_pais)
)engine=INNODB;


create table if not exists carrera_escritores(
	id_escritor int not null,
    id_pelicula int not null,
    remuneracion float not null,
    
    
    primary key(id_escritor, id_pelicula),
    
    constraint fk_id_escritor_carrera foreign key(id_escritor)
		references escritores(id_escritor),
	
    constraint fk_id_pelicula_escritor_carrera foreign key(id_pelicula)
		references peliculas(id_pelicula)
) engine=INNODB;

create table if not exists carrera_actores(
	id_actor int not null,
    id_pelicula int not null,
    remuneracion float not null,
    
    
    primary key(id_actor, id_pelicula),
    
    constraint fk_id_actor_carrera foreign key(id_actor)
		references escritores(id_escritor),
	
    constraint fk_id_pelicula_carrera_actor foreign key(id_pelicula)
		references peliculas(id_pelicula)
) engine=INNODB;





