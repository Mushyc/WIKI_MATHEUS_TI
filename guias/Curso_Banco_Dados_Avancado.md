# 🗄️ Bancos de Dados Avançado: Master Class Edition
![Banner DB](/banner_db.png)
> **Nível:** Intermediário ao DBA | **Foco:** SQL, Modelagem e Performance
---

## 📖 Introdução: A Memória do Sistema

Se o código é o cérebro, o **Banco de Dados** é a memória a longo prazo. Sem ele, todos os dados sumiriam quando você fechasse o programa. Mas não basta salvar; é preciso organizar para que a busca seja instantânea, mesmo com milhões de linhas.

---

## 🏗️ Módulo 1: Modelagem Relacional (O Desenho)

Antes de criar tabelas, você precisa desenhar o **DER (Diagrama Entidade-Relacionamento)**.

### 📝 No seu Caderno (Dica de Modelagem):
- **Entidade:** É o que você quer salvar (ex: Cliente, Produto).
- **Atributo:** É a informação daquela entidade (ex: Nome, Preço).
- **Relacionamento:** Como eles se ligam (ex: Um Cliente *faz* um Pedido).

---

## ⚡ Módulo 2: SQL - A Linguagem das Perguntas

O SQL (Structured Query Language) é como você conversa com o banco.
*   `SELECT`: "Me mostre..."
*   `INSERT`: "Salve isso aqui..."
*   `UPDATE`: "Mude aquele dado..."
*   `DELETE`: "Apague isso!"

### 🔍 O Poder dos JOINS
A vida real não cabe em uma tabela só. Usamos `JOIN` para unir os dados.
*   **INNER JOIN:** Traz o que tem nos dois lados. (Ex: Cliente que tem pedido).
*   **LEFT JOIN:** Traz tudo da esquerda, mesmo que não tenha nada na direita.

---

## 🚀 Módulo 3: Performance e Índices

Sabe quando um sistema fica lento para buscar um CPF? É falta de **Índice**.
O Índice é como o sumário de um livro. Em vez de ler o banco todo (Full Table Scan), o banco vai direto na página certa.

### ⚖️ Propriedades ACID (Anote isso!):
Para um banco ser confiável, ele precisa ser:
1.  **Atomicidade:** Ou a transação acontece toda, ou nada.
2.  **Consistência:** O banco tem que estar íntegro antes e depois.
3.  **Isolamento:** Uma transação não atrapalha a outra.
4.  **Durabilidade:** Uma vez salvo, o dado não some.

---

## 🛡️ Módulo 4: Segurança e Prevenção

O maior ataque a bancos de dados é o **SQL Injection**.
*   *O que é:* Quando um hacker coloca comandos SQL em campos de texto (como login) para roubar senhas.
*   *Como evitar:* Nunca confie no que o usuário digita. Use "Prepared Statements".

---

## 📝 Exercícios de Fixação (Para responder no caderno!)

1.  Qual a função da **Chave Primária (Primary Key)** em uma tabela?
2.  O que é uma **Chave Estrangeira (Foreign Key)** e para que ela serve?
3.  Explique a diferença entre um `DELETE` e um `TRUNCATE`.
4.  Para que serve a cláusula `GROUP BY` no SQL?
5.  O que acontece se você rodar um `DELETE` sem a cláusula `WHERE`? (Cuidado!)
6.  Defina o que é a **Atomicidade** dentro das propriedades ACID.
7.  Quando devemos usar um **Índice** e qual o "custo" de ter muitos índices em uma tabela?
8.  O que é a **Normalização** e por que paramos na 3ª Forma Normal (3NF) na maioria das vezes?
9.  Dê um exemplo de um banco de dados **NoSQL** e explique quando usá-lo em vez do SQL.
10. **Desafio:** Escreva o comando SQL que seleciona o nome e o e-mail de todos os clientes que moram na cidade de \"Cuiabá\".

---

### 🚀 Próximos Passos
- [🧩 POO na Prática](/guias/Curso_POO_Pratica) - Aprenda a mapear objetos para o banco (ORM).
- [🐍 Python para Automação](/guias/Curso_Python_Automacao) - Crie robôs que alimentam seu banco de dados.
