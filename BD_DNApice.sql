create database DNApice;
use DNApice;

create table organismo(id_avatar int auto_increment primary key,
			nome varchar(100) not null,
			idade int not null,
			peso decimal(10,2) not null,
			energia int not null,#### e ver bioma em poo como obj
			intensidade_dor int not null ####);

create table utero(id_utero int auto_increment primary key,

		###mesma coisa com a pele, só que elas ainda não têm atributos

);

create table bioma(id_bioma int auto_increment primary key,
		nome varchar(50) not null,
		clima varchar(50) not null,
		região varchar(50) not null,
		temp_min int not null,
		temp_max int not null,
		especificidade varchar(70) not null,
		tipo_solo varchar(50) not null,
		
		id_avatar_bioma int, ###
		foreing key (id_avatar_bioma) references organismo(id_avatar));

create table tipo_protecao(id_tipo varchar(10) primary key, 
		       informacoes varchar(100) not null);###como se fosse categoria em vendas_bd


###se organismo usar proteção teria que criar um alter table pra alterar a intensidade da dor, algo assim eu acho =)

create table protecao(id_protecao int auto_increment primary key,
			tipo varchar(10) not null,
			id_avatar int not null,

			foreing key (id_avatar) references organismo(id_avatar)
			foreing key (tipo) references tipo_protecao(id_tipo));

