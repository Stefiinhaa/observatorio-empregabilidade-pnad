# ↪ Observatório de Qualificação Profissional e Empregabilidade

Este repositório contém o desenvolvimento do Projeto Integrador Extensionista em Ciência de Dados, focado em analisar os desafios e impactos da qualificação profissional no Brasil.

## ⩥ Sobre o Projeto
O projeto utiliza dados da pesquisa suplementar PNAD 2014 (IBGE) sobre Educação e Qualificação Profissional. O objetivo principal é atuar como um observatório, extraindo insights analíticos sobre os motivos de evasão em cursos profissionalizantes e o impacto dessa formação na renda familiar. O público-alvo são instituições de ensino e gestores de políticas públicas.

## ⩥ Fonte dos Dados
* **Origem:** Instituto Brasileiro de Geografia e Estatística (IBGE)
* **Base:** PNAD 2014 - Educação e Qualificação Profissional (Formato CSV).
* Os dados são de domínio público, anonimizados, respeitando as diretrizes éticas e a LGPD.

## ⩥ Tecnologias Utilizadas
* **Python (Pandas):** Para limpeza e transformação inicial dos dados.
* **MySQL:** Armazenamento estruturado e consultas (Queries) analíticas.
* **Ferramenta de BI:** Para visualização e apresentação dos KPIs.
* **GitHub & Trello:** Versionamento de código e gestão ágil (Kanban).

## ⩥ Fluxograma de Dados
Abaixo está o fluxo detalhado das etapas do nosso processamento de dados (ETL):

![fluxograma](docs/escopo-1/AE1/imagens-kanban_e_digrama/diagrama.drawio.png)
https://drive.google.com/file/d/1Os8qotCLdyhJQgHWvCH-_Itqn0AZSgjf/view?usp=sharing

## ⩥ Gestão Ágil (Kanban)
O acompanhamento de entregas, EAP e mitigação de riscos está sendo gerido via Trello. Segue o registro do board atual:

![kanban](docs/escopo-1/AE1/imagens-kanban_e_digrama/kanban-trello.png)
https://trello.com/invite/b/6a0f0536261037067da72fe3/ATTI181a38c54d26145b37073634376d658f4B595489/pi-extensionista-cd1
Data: 20/05 a 27/05

## ⩥ Arquitetura e Desenho da Solução
Durante a segunda etapa do projeto, definimos as regras de negócio e a modelagem dos dados:

* **Dicionário de Dados & Qualidade:** Regras de limpeza, tratamento de nulos e de outliers mapeadas para execução via Pandas.

* **Modelo Lógico:** Estruturação no MySQL utilizando Star Schema, com uma Tabela Fato (Fato_Qualificacao) e dimensões sociodemográficas e de motivos de evasão.

* **Visualização:** Wireframe desenhado focando na jornada do usuário para o Dashboard.
  ![Modelo Lógico do banco de dados](docs/escopo-1/AE2/Diagrama-modelo-logico.drawio.png)

## ⩥ Escopo e Entregas (Fase 1)
- [x] Termo de Abertura e Briefing.
- [x] Definição das Perguntas Analíticas e KPIs.
- [x] EAP, Matriz de Riscos e Cronograma.
- [x] Estruturação inicial do GitHub.
 
## ⩥ Fase 2 - Desenho da Solução

- [x] Dicionário de Dados (versão 1).

- [x] Modelo Lógico (Diagrama de tabelas e relacionamentos).

- [x] Plano de Qualidade de Dados (Checagens Python/MySQL).

- [x] Plano de Análise e Esboço (Wireframe) do Dashboard.

- [x] Criação de Issues (tarefas de desenvolvimento) no GitHub.
