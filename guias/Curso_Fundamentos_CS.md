# 🧮 Curso: Fundamentos de Ciência da Computação

Teoria que a faculdade exige: Arquitetura, Matemática e Sistemas Operacionais.

---

## 💻 Módulo 1: Arquitetura de Computadores

### Componentes Básicos
**CPU (Processador)**
- ALU: Operações aritméticas/lógicas
- UC: Controla fluxo de dados
- Registradores: Memória ultra-rápida

**Memória Hierarquia**
1. Registradores (mais rápido, menor)
2. Cache L1, L2, L3
3. RAM
4. SSD/HDD
5. Armazenamento em nuvem (mais lento, maior)

### Sistemas Numéricos

**Binário (Base 2)**
```
Decimal 5 = Binário 101
Decimal 10 = Binário 1010
```

**Hexadecimal (Base 16)**
```
Decimal 255 = Hex FF
Decimal 16 = Hex 10
```

**Conversões Python**
```python
# Decimal para Binário
bin(10)  # '0b1010'

# Decimal para Hex
hex(255)  # '0xff'

# Binário para Decimal
int('1010', 2)  # 10
```

---

## 🧠 Módulo 2: Lógica Booleana

### Operadores
| Operador | Python | Resultado |
|----------|--------|-----------|
| AND | `and` | True se AMBOS verdadeiros |
| OR | `or` | True se PELO MENOS 1 verdadeiro |
| NOT | `not` | Inverte |
| XOR | `^` | True se APENAS 1 verdadeiro |

### Tabelas Verdade
```
A AND B:
0 AND 0 = 0
0 AND 1 = 0
1 AND 0 = 0
1 AND 1 = 1

A OR B:
0 OR 0 = 0
0 OR  1 = 1
1 OR 0 = 1
1 OR 1 = 1
```

---

## 📐 Módulo 3: Matemática Discreta

### Teoria dos Conjuntos
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# União
A | B  # {1, 2, 3, 4, 5, 6}

# Interseção
A & B  # {3, 4}

# Diferença
A - B  # {1, 2}
```

### Análise Combinatória
**Permutação:** Ordem importa
```
P(n) = n!
P(3) = 3! = 6
```

**Combinação:** Ordem não importa
```
C(n,k) = n! / (k! * (n-k)!)
C(5,2) = 10
```

---

## 🖥️ Módulo 4: Sistemas Operacionais

### Processos vs Threads
**Processo:** Programa em execução
**Thread:** Tarefa dentro de um processo

### Escalonamento de CPU
- **FCFS:** First Come First Served
- **SJF:** Shortest Job First
- **Round Robin:** Revezamento com quantum

### Deadlock (Travamento)
**4 Condições:**
1. Exclusão mútua
2. Posse e espera
3. Não preempção
4. Espera circular

---

## 💾 Módulo 5: Gerenciamento de Memória

### Memória Virtual
Sistema usa HD como extensão da RAM.

### Paginação
Memória dividida em páginas fixas.

### Segmentação
Memória dividida em segmentos lógicos.

---

## 🔐 Módulo 6: Criptografia Básica

### Hash (MD5, SHA-256)
```python
import hashlib

senha = "123456"
hash_senha = hashlib.sha256(senha.encode()).hexdigest()
print(hash_senha)
# 8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92
```

**Propriedades:**
- Determinística (mesma entrada = mesmo hash)
- Unidirecional (não dá pra reverter)
- Avalanche (pequena mudança = hash totalmente diferente)

### Criptografia Simétrica vs Assimétrica
**Simétrica:** Mesma chave para criptografar/descriptografar (AES)
**Assimétrica:** Par de chaves pública/privada (RSA)

---

## 📊 Módulo 7: Complexidade Computacional

### Problemas P vs NP
**P:** Resolúveis em tempo polinomial
**NP:** Verificáveis em tempo polinomial

### Problemas NP-Completos
- Caixeiro Viajante
- Satisfabilidade Booleana (SAT)
- Coloração de Grafos

**Por quê importa?** Alguns problemas não têm solução eficiente conhecida.

---

## 🎯 Aplicação Prática

### Calculadora Binária
```python
def soma_binaria(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

print(soma_binaria('1010', '0101'))  # '1111' (15)
```

### Simulador de Memória Cache
```python
class CacheLRU:
    def __init__(self, capacidade):
        self.cache = {}
        self.capacidade = capacidade
        self.ordem = []
    
    def get(self, chave):
        if chave in self.cache:
            self.ordem.remove(chave)
            self.ordem.append(chave)
            return self.cache[chave]
        return -1
    
    def put(self, chave, valor):
        if chave in self.cache:
            self.ordem.remove(chave)
        elif len(self.cache) >= self.capacidade:
            removida = self.ordem.pop(0)
            del self.cache[removida]
        
        self.cache[chave] = valor
        self.ordem.append(chave)
```

---

## 📖 Conceitos para Faculdade

**Disciplinas que usam isso:**
- Arquitetura de Computadores
- Sistemas Operacionais
- Matemática Discreta
- Teoria da Computação
- Compiladores

**Dica:** Você já sabe a PRÁTICA (programar). Agora vai aprender a TEORIA (por que funciona).

---

**Veja também:**
- [Algoritmos e Estruturas de Dados](/guias/Curso_Algoritmos_Estruturas_Dados)
- [Redes de Computadores](/guias/Curso_Redes_Computadores)
- [Montagem de PCs](/guias/Curso_Montagem_Manutencao_PC)
