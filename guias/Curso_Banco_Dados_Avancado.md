# 🗄️ Curso: Bancos de Dados Avançado

SQL + NoSQL + Performance + Design de Esquemas.

---

## 📚 Módulo 1: SQL Avançado

### Joins
```sql
-- INNER JOIN (apenas registros com correspondência)
SELECT usuarios.nome, pedidos.total
FROM usuarios
INNER JOIN pedidos ON usuarios.id = pedidos.usuario_id;

-- LEFT JOIN (todos da esquerda + correspondências)
SELECT usuarios.nome, pedidos.total
FROM usuarios
LEFT JOIN pedidos ON usuarios.id = pedidos.usuario_id;

-- RIGHT JOIN
SELECT usuarios.nome, pedidos.total
FROM usuarios
RIGHT JOIN pedidos ON usuarios.id = pedidos.usuario_id;
```

### Subqueries
```sql
-- Encontrar usuários com pedidos acima da média
SELECT nome
FROM usuarios
WHERE id IN (
    SELECT usuario_id
    FROM pedidos
    WHERE total > (SELECT AVG(total) FROM pedidos)
);
```

### Funções de Agregação
```sql
SELECT 
    categoria,
    COUNT(*) as total_produtos,
    AVG(preco) as preco_medio,
    MAX(preco) as mais_caro,
    MIN(preco) as mais_barato
FROM produtos
GROUP BY categoria
HAVING AVG(preco) > 100;
```

---

## 📋 Módulo 2: Normalização

### Formas Normais

**1NF:** Sem grupos repetidos
```sql
-- ❌ Errado
CREATE TABLE pedidos (
    id INT,
    produtos TEXT  -- "Arroz, Feijão, Macarrão"
);

-- ✅ Correto
CREATE TABLE pedidos_itens (
    pedido_id INT,
    produto_id INT
);
```

**2NF:** Sem dependências parciais
**3NF:** Sem dependências transitivas

### Desnormalização (Quando usar)
Para **performance**, às vezes quebrar normalização é OK.

---

## 🚀 Módulo 3: Performance e Índices

### Criar Índices
```sql
CREATE INDEX idx_email ON usuarios(email);
CREATE INDEX idx_categoria_preco ON produtos(categoria, preco);
```

### Explain (Ver plano de execução)
```sql
EXPLAIN SELECT * FROM usuarios WHERE email = 'teste@email.com';
```

### Otimização
```sql
-- ❌ Lento
SELECT * FROM produtos WHERE YEAR(data_criacao) = 2024;

-- ✅ Rápido
SELECT * FROM produtos 
WHERE data_criacao >= '2024-01-01' 
  AND data_criacao < '2025-01-01';
```

---

## 🔐 Módulo 4: Transações e ACID

### Transações
```sql
START TRANSACTION;

UPDATE contas SET saldo = saldo - 100 WHERE id = 1;
UPDATE contas SET saldo = saldo + 100 WHERE id = 2;

COMMIT;  -- Confirma
-- OU
ROLLBACK;  -- Desfaz
```

### ACID
- **A**tomicidade: Tudo ou nada
- **C**onsistência: Regras mantidas
- **I**solamento: Transações independentes
- **D**urabilidade: Dados persistidos

---

## 📦 Módulo 5: NoSQL (MongoDB)

### Quando Usar NoSQL?
- Dados não-estruturados
- Escalabilidade horizontal
- Flexibilidade de esquema

### MongoDB Básico
```javascript
// Inserir
db.usuarios.insertOne({
    nome: "João",
    email: "joao@email.com",
    idade: 25,
    interesses: ["programação", "games"]
});

// Buscar
db.usuarios.find({ idade: { $gt: 18 } });

// Atualizar
db.usuarios.updateOne(
    { email: "joao@email.com" },
    { $set: { idade: 26 } }
);

// Deletar
db.usuarios.deleteOne({ email: "joao@email.com" });
```

---

## 🎯 SQL vs NoSQL

| Aspecto | SQL | NoSQL |
|---------|-----|-------|
| Estrutura | Rígida (tabelas) | Flexível (documentos) |
| Escalabilidade | Vertical | Horizontal |
| Transações | Forte | Eventual |
| Uso | Financeiro, ERP | Redes sociais, Big Data |

---

## 🔧 Projeto Prático: E-commerce

```sql
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    senha_hash VARCHAR(255),
    criado_em TIMESTAMP DEFAULT NOW()
);

CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(200),
    preco DECIMAL(10,2),
    estoque INT,
    categoria_id INT REFERENCES categorias(id)
);

CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    usuario_id INT REFERENCES usuarios(id),
    total DECIMAL(10,2),
    status VARCHAR(20),
    criado_em TIMESTAMP DEFAULT NOW()
);

CREATE TABLE pedidos_itens (
    pedido_id INT REFERENCES pedidos(id),
    produto_id INT REFERENCES produtos(id),
    quantidade INT,
    preco_unitario DECIMAL(10,2),
    PRIMARY KEY (pedido_id, produto_id)
);
```

---

**Veja também:**
- [Desenvolvimento Web](/guias/Guia_Desenvolvimento_Web)
- [Python para Automação](/guias/Curso_Python_Automacao)
- [Windows Server](/guias/Curso_Windows_Server_AD)
