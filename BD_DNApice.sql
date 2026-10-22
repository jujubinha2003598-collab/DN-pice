drop database is exists DNApice;
create database DNApice;
use DNApice;

create table organismo(id_avatar int auto_increment primary key,
			nome varchar(100) not null,
			idade int not null,
			peso decimal(10,2) not null,
			energia int not null,
			intensidade_dor int not null
			fome INT NOT NULL DEFAULT 0,
    		id_bioma INT NOT NULL,
    		FOREIGN KEY (id_bioma) REFERENCES bioma(id_bioma)
	);

CREATE TABLE pele (
    id_avatar_pele INT PRIMARY KEY,
    melanina NOT NULL,
    protecao float NOT NULL DEFAULT FALSE,
    FOREIGN KEY (id_avatar_pele) REFERENCES organismo(id_avatar)
);

create table utero(
		id_avatar_utero int primary key,
	 	tamanho_utero int not null DEFAULT 10,
    	saude int not null DEFAULT 10,
		foreign key (id_avatar_utero) references organismo(id_avatar)
);

create table bioma(id_bioma int auto_increment primary key,
		id_avatar_bioma int, 
		foreign key (id_avatar_bioma) references organismo(id_avatar),
        nome varchar(50) not null,
		clima varchar(50) not null,
		região varchar(50) not null,
		temp_min int not null,
		temp_max int not null,
		especificidade varchar(70) not null,
		tipo_solo varchar(50) not null,
		id_item_correto INT NOT NULL, 
        espessura_neve int,
        nivel_queimada float,
        umidade float,
        densidade_c float
		FOREIGN KEY (id_item_correto) REFERENCES tipo_protecao(id_tipo)
        );

create table tipo_protecao(id_tipo varchar(10) primary key, 
				nome varchar(50) not null,
		       informacoes varchar(100) not null);

INSERT INTO tipo_protecao VALUES
(1, 'Protetor solar', 'Protege contra o sol forte da Savana'),
(2, 'Repelente', 'Afasta os insetos da Floresta Tropical'),
(3, 'Blusa de frio', 'Mantém o corpo aquecido na Tundra');

INSERT INTO bioma (tipo_bioma, nome, clima, regiao, temp_min, temp_max,
                   especificidade, tipo_solo, id_item_correto, nivel_queimada)
VALUES ('Savana', 'Savana', 'Tropical Semiárido', 'África / América do Sul',
        20.0, 40.0, 'Estação seca prolongada',
        'Arenoso e poroso (Pobre em nutrientes)', 1, 2);

INSERT INTO bioma (tipo_bioma, nome, clima, regiao, temp_min, temp_max,
                   especificidade, tipo_solo, id_item_correto,
                   umidade_relativa, densidade_copada)
VALUES ('Floresta Tropical', 'Floresta Tropical', 'Equatorial / Tropical Úmido',
        'Amazônia / Bacia do Congo', 22.0, 32.0,
        'Canópia densa e solo com serrapilheira',
        'Argiloso e úmido', 2, 85.0, 90.0);

INSERT INTO bioma (tipo_bioma, nome, clima, regiao, temp_min, temp_max,
                   especificidade, tipo_solo, id_item_correto, espessura_neve)
VALUES ('Tundra', 'Tundra', 'Frio Polar', 'Ártico', -20.0, 0.0,
        'Periglacial', 'Permafrost', 3, 30.0);

INSERT INTO organismo (nome, idade, peso, id_bioma)
VALUES ('Laura', 15, 52.5, 1);

INSERT INTO pele (id_avatar_pele, melanina) VALUES (1, 'media');
INSERT INTO utero (id_avatar_utero) VALUES (1);

