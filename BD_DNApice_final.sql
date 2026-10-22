drop database if exists DNApice;
create database DNApice;
use DNApice;

create table tipo_protecao(id_tipo int primary key, 
				nome varchar(50) not null,
		        informacoes varchar(100) not null);
               
create table bioma(id_bioma int auto_increment primary key,
        nome varchar(50) not null,
		clima varchar(50) not null,
		regiao varchar(50) not null,
		temp_min int not null,
		temp_max int not null,
		especificidade varchar(70) not null,
		tipo_solo varchar(50) not null,
		id_item_correto int NOT NULL, 
        espessura_neve int,
        nivel_queimada float,
        umidade float,
        densidade_copada float,
		FOREIGN KEY (id_item_correto) REFERENCES tipo_protecao(id_tipo)
        );

create table organismo(id_avatar int auto_increment primary key,
			nome varchar(100) not null,
			idade int not null,
			peso decimal(10,2) not null,
			energia int not null,
			intensidade_dor int not null,
			fome INT NOT NULL,
    		id_bioma INT NOT NULL,
    		FOREIGN KEY (id_bioma) REFERENCES bioma(id_bioma)
	);

CREATE TABLE pele (
    id_avatar_pele INT PRIMARY KEY,
    melanina varchar(10) not NULL,
    protecao float NOT NULL DEFAULT FALSE,
    FOREIGN KEY (id_avatar_pele) REFERENCES organismo(id_avatar)
);

create table utero(
		id_avatar_utero int primary key,
	 	tamanho_utero int not null DEFAULT 10,
    	saude int not null DEFAULT 10,
		foreign key (id_avatar_utero) references organismo(id_avatar)
);


INSERT INTO tipo_protecao VALUES
(1, 'Protetor solar', 'Protege contra o sol forte da Savana'),
(2, 'Repelente', 'Afasta os insetos da Floresta Tropical'),
(3, 'Blusa de frio', 'Mantém o corpo aquecido na Tundra');

INSERT INTO bioma (nome, clima, regiao, temp_min, temp_max,
                   especificidade, tipo_solo, id_item_correto, nivel_queimada)
VALUES ('Savana', 'Tropical Semiárido', 'África / América do Sul',
        20.0, 40.0, 'Estação seca prolongada',
        'Arenoso e poroso (Pobre em nutrientes)', 1, 2);

INSERT INTO bioma (nome, clima, regiao, temp_min, temp_max,
                   especificidade, tipo_solo, id_item_correto,
                   umidade, densidade_copada)
VALUES ('Floresta Tropical', 'Equatorial / Tropical Úmido',
        'Amazônia / Bacia do Congo', 22.0, 32.0,
        'Canópia densa e solo com serrapilheira',
        'Argiloso e úmido', 2, 85.0, 90.0);

INSERT INTO bioma (nome, clima, regiao, temp_min, temp_max,
                   especificidade, tipo_solo, id_item_correto, espessura_neve)
VALUES ('Tundra', 'Frio Polar', 'Ártico', -20.0, 0.0,
        'Periglacial', 'Permafrost', 3, 30.0);

INSERT INTO organismo (id_avatar, nome, idade, peso, id_bioma, energia, intensidade_dor, fome)
VALUES (1, 'Laura', 15, 52.5, 1, 63, 10, 0);

INSERT INTO organismo (id_avatar, nome, idade, peso, id_bioma, energia, intensidade_dor, fome)
VALUES (2, 'Angela', 33, 54.0, 2, 86, 4, 0);

INSERT INTO organismo (id_avatar, nome, idade, peso, id_bioma, energia, intensidade_dor, fome)
VALUES (3, 'Gabrielly', 21, 62.3, 2, 80, 20, 2);

INSERT INTO organismo (id_avatar, nome, idade, peso, id_bioma, energia, intensidade_dor, fome)
VALUES (4, 'Maria de Lourde', 45, 57.6, 3, 55, 15, 12);

INSERT INTO organismo (id_avatar, nome, idade, peso, id_bioma, energia, intensidade_dor, fome)
VALUES (5, 'Olívia', 21, 60.9, 1, 90, 2, 7);

INSERT INTO pele (id_avatar_pele, melanina) VALUES (1, 'media');
INSERT INTO utero (id_avatar_utero) VALUES (1);

INSERT INTO pele (id_avatar_pele, melanina) VALUES (2, 'media');
INSERT INTO utero (id_avatar_utero) VALUES (2);

INSERT INTO pele (id_avatar_pele, melanina) VALUES (3, 'alta');
INSERT INTO utero (id_avatar_utero) VALUES (3);

INSERT INTO pele (id_avatar_pele, melanina) VALUES (4, 'alta');
INSERT INTO utero (id_avatar_utero) VALUES (4);

INSERT INTO pele (id_avatar_pele, melanina) VALUES (5, 'baixa');
INSERT INTO utero (id_avatar_utero) VALUES (5);


SELECT * FROM bioma;
SELECT * FROM organismo;

SELECT o.id_avatar, o.nome, p.id_avatar_pele, p.melanina 
FROM organismo o, pele p 
where p.id_avatar_pele = o.id_avatar;

SELECT id_avatar_pele as "ID dos avatares com pele de melanina 'média':"
from pele 
WHERE melanina = 'media';

SELECT b.nome as "Nome do Bioma", o.nome as "Nome do Avatar"
FROM organismo o, bioma b 
where b.id_bioma = o.id_bioma;