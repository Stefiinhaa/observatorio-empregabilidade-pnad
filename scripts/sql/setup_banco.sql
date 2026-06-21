-- 1. Criação da Base de Dados
CREATE DATABASE IF NOT EXISTS observatorio_pnad DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE observatorio_pnad;

-- 2. Criação da Tabela Temporária (para receber o CSV do Pandas)
CREATE TABLE IF NOT EXISTS pnad_staging (
    ano INT,
    uf VARCHAR(2),
    sexo VARCHAR(20),
    idade INT,
    cor_raca VARCHAR(20),
    renda_mensal DECIMAL(10,2),
    frequentou_curso VARCHAR(10),
    concluiu_curso VARCHAR(10),
    motivo_evasao VARCHAR(100)
);

-- 3. Criação das Tabelas 
CREATE TABLE IF NOT EXISTS Dim_Pessoa (
    id_pessoa INT AUTO_INCREMENT PRIMARY KEY,
    sexo VARCHAR(20),
    cor_raca VARCHAR(20),
    idade INT
);

CREATE TABLE IF NOT EXISTS Dim_Motivo_Evasao (
    id_motivo INT AUTO_INCREMENT PRIMARY KEY,
    descricao_motivo VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Fato_Qualificacao (
    id_fato INT AUTO_INCREMENT PRIMARY KEY,
    id_pessoa INT,
    id_motivo INT,
    ano INT,
    uf VARCHAR(2),
    renda_mensal DECIMAL(10,2),
    frequentou_curso VARCHAR(10),
    concluiu_curso VARCHAR(10),
    FOREIGN KEY (id_pessoa) REFERENCES Dim_Pessoa(id_pessoa),
    FOREIGN KEY (id_motivo) REFERENCES Dim_Motivo_Evasao(id_motivo)
);