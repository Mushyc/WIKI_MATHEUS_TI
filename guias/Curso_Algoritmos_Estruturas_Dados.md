# 📊 Curso: Algoritmos e Estruturas de Dados

O curso mais importante para faculdade e entrevistas técnicas.

---

## 🎯 Por Que Este é o Curso Mais Importante?

**Na faculdade:** 50% das disciplinas usam isso.
**Em entrevistas:** Google, Meta, Amazon testam algoritmos.
**No dia a dia:** Código eficiente = app rápido.

---

## 📚 Módulo 1: Análise de Complexidade (Big O)

### O Que é Big O?
Mede o **tempo de execução** conforme **entrada cresce**.

### Complexidades Comuns

**O(1) - Constante** ⭐
```python
def pegar_primeiro(lista):
    return lista[0]  # Sempre 1 operação
```
**Exemplo:** Acessar array por índice.

**O(n) - Linear** ⭐⭐
```python
def buscar_linear(lista, valor):
    for item in lista:
        if item == valor:
            return True
    return False
```
**Exemplo:** Percorrer lista uma vez.

**O(n²) - Quadrática** ⭐⭐⭐ (Evite!)
```python
def bubble_sort(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
```
**Exemplo:** Loops aninhados.

**O(log n) - Logarítmica** ⭐⭐⭐⭐ (Ótima!)
```python
def busca_binaria(lista, valor):
    inicio, fim = 0, len(lista)-1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1
```
**Exemplo:** Busca em lista ordenada.

**O(n log n)** ⭐⭐⭐⭐
**Exemplo:** Merge Sort, Quick Sort (algoritmos eficientes).

### Comparação Prática
Para n = 1.000.000:
- O(1): 1 operação
- O(log n): ~20 operações
- O(n): 1.000.000 operações
- O(n²): 1.000.000.000.000 operações (inviável!)

---

## 📋 Módulo 2: Listas e Arrays

### Array (Lista em Python)
```python
# Criar
numeros = [1, 2, 3, 4, 5]

# Acessar - O(1)
print(numeros[0])  # 1

# Inserir no final - O(1)
numeros.append(6)

# Inserir no início - O(n) (move todos!)
numeros.insert(0, 0)

# Buscar - O(n)
if 3 in numeros:
    print("Encontrado")

# Remover - O(n)
numeros.remove(3)
```

### Lista Ligada (Linked List)
```python
class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaLigada:
    def __init__(self):
        self.cabeca = None
    
    def inserir_inicio(self, valor):  # O(1)
        novo_no = No(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no
    
    def buscar(self, valor):  # O(n)
        atual = self.cabeca
        while atual:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False
```

**Quando usar:**
- Array: Acesso rápido por índice
- Lista Ligada: Muitas inserções/remoções no início

---

## 🥞 Módulo 3: Pilha (Stack)

### Conceito: LIFO (Last In, First Out)
**Analogia:** Pilha de pratos - último colocado é o primeiro removido.

### Implementação
```python
class Pilha:
    def __init__(self):
        self.itens = []
    
    def push(self, item):  # O(1)
        self.itens.append(item)
    
    def pop(self):  # O(1)
        if not self.vazia():
            return self.itens.pop()
    
    def topo(self):  # O(1)
        if not self.vazia():
            return self.itens[-1]
    
    def vazia(self):
        return len(self.itens) == 0

# Uso
pilha = Pilha()
pilha.push(1)
pilha.push(2)
pilha.push(3)
print(pilha.pop())  # 3 (último)
```

### Casos de Uso Reais
- **Navegador:** Botão "Voltar" (pilha de páginas)
- **Editor:** Ctrl+Z (pilha de ações)
- **Compilador:** Verificar parênteses balanceados

### Exercício: Validar Parênteses
```python
def validar_parenteses(expressao):
    pilha = Pilha()
    pares = {'(': ')', '[': ']', '{': '}'}
    
    for char in expressao:
        if char in pares.keys():
            pilha.push(char)
        elif char in pares.values():
            if pilha.vazia() or pares[pilha.pop()] != char:
                return False
    
    return pilha.vazia()

print(validar_parenteses("({[]})"))  # True
print(validar_parenteses("({[}])"))  # False
```

---

## 🚶 Módulo 4: Fila (Queue)

### Conceito: FIFO (First In, First Out)
**Analogia:** Fila de banco - primeiro a chegar é o primeiro atendido.

### Implementação
```python
from collections import deque

class Fila:
    def __init__(self):
        self.itens = deque()
    
    def enfileirar(self, item):  # O(1)
        self.itens.append(item)
    
    def desenfileirar(self):  # O(1)
        if not self.vazia():
            return self.itens.popleft()
    
    def frente(self):
        if not self.vazia():
            return self.itens[0]
    
    def vazia(self):
        return len(self.itens) == 0

# Uso
fila = Fila()
fila.enfileirar("João")
fila.enfileirar("Maria")
fila.enfileirar("Pedro")
print(fila.desenfileirar())  # João (primeiro)
```

### Casos de Uso
- **Impressora:** Fila de impressão
- **Sistema Operacional:** Fila de processos
- **Streaming:** Buffer de vídeo

---

## 🗂️ Módulo 5: Dicionário (Hash Map)

### Conceito
Armazena pares **chave-valor** com acesso O(1).

### Implementação (Python já tem built-in)
```python
# Dict nativo do Python
agenda = {}

# Inserir - O(1)
agenda["João"] = "11-9999-8888"
agenda["Maria"] = "11-8888-7777"

# Buscar - O(1)
print(agenda["João"])

# Verificar existência
if "Pedro" in agenda:
    print(agenda["Pedro"])

# Iterar
for nome, telefone in agenda.items():
    print(f"{nome}: {telefone}")
```

### Caso de Uso: Contar Frequência
```python
def contar_frequencia(lista):
    frequencia = {}
    for item in lista:
        if item in frequencia:
            frequencia[item] += 1
        else:
            frequencia[item] = 1
    return frequencia

palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
print(contar_frequencia(palavras))
# {'maçã': 3, 'banana': 2, 'laranja': 1}
```

---

## 🌳 Módulo 6: Árvores

### Árvore Binária
Cada nó tem **no máximo 2 filhos**.

```python
class NoArvore:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
    
    def inserir(self, valor):
        if not self.raiz:
            self.raiz = NoArvore(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)
    
    def _inserir_recursivo(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = NoArvore(valor)
            else:
                self._inserir_recursivo(no_atual.esquerda, valor)
        else:
            if no_atual.direita is None:
                no_atual.direita = NoArvore(valor)
            else:
                self._inserir_recursivo(no_atual.direita, valor)
    
    def buscar(self, valor):  # O(log n) em árvore balanceada
        return self._buscar_recursivo(self.raiz, valor)
    
    def _buscar_recursivo(self, no_atual, valor):
        if no_atual is None:
            return False
        if no_atual.valor == valor:
            return True
        elif valor < no_atual.valor:
            return self._buscar_recursivo(no_atual.esquerda, valor)
        else:
            return self._buscar_recursivo(no_atual.direita, valor)
```

### Percursos
```python
def percurso_em_ordem(no):  # Esquerda, Raiz, Direita
    if no:
        percurso_em_ordem(no.esquerda)
        print(no.valor)
        percurso_em_ordem(no.direita)

def percurso_pre_ordem(no):  # Raiz, Esquerda, Direita
    if no:
        print(no.valor)
        percurso_pre_ordem(no.esquerda)
        percurso_pre_ordem(no.direita)

def percurso_pos_ordem(no):  # Esquerda, Direita, Raiz
    if no:
        percurso_pos_ordem(no.esquerda)
        percurso_pos_ordem(no.direita)
        print(no.valor)
```

---

## 📈 Módulo 7: Algoritmos de Ordenação

### Bubble Sort - O(n²)
```python
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista
```
**Quando usar:** Listas pequenas ou quase ordenadas.

### Merge Sort - O(n log n) ⭐
```python
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0
    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado
```
**Quando usar:** Listas grandes (melhor performance).

### Quick Sort - O(n log n) médio
```python
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    
    pivo = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista if x > pivo]
    
    return quick_sort(menores) + iguais + quick_sort(maiores)
```
**Quando usar:** Geralmente o mais rápido na prática.

---

## 🔍 Módulo 8: Algoritmos de Busca

### Busca Linear - O(n)
```python
def busca_linear(lista, alvo):
    for i, valor in enumerate(lista):
        if valor == alvo:
            return i
    return -1
```

### Busca Binária - O(log n) ⭐
```python
def busca_binaria(lista, alvo):
    inicio, fim = 0, len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    
    return -1
```
**Pré-requisito:** Lista DEVE estar ordenada.

---

## 🎯 Projetos Práticos

### Projeto 1: Sistema de Tarefas com Prioridade
Use **heap** (fila de prioridade).

### Projeto 2: Autocomplete
Use **trie** (árvore de prefixos).

### Projeto 3: Cache LRU
Use **dict + lista ligada**.

---

## 🎓 Para Entrevistas Técnicas

**Padrões mais cobrados:**
1. Two Pointers (dois ponteiros)
2. Sliding Window (janela deslizante)
3. Fast & Slow Pointers
4. DFS/BFS em árvores
5. Backtracking

---

## 📖 Recursos de Estudo

**Plataformas de prática:**
- LeetCode (Easy → Medium)
- HackerRank
- Exercism

**Livros:**
- "Entendendo Algoritmos" - Aditya Bhargava
- "Algoritmos: Teoria e Prática" - Cormen (avançado)

---

**Veja também:**
- [POO na Prática](/guias/Curso_POO_Pratica)
- [Python para Automação](/guias/Curso_Python_Automacao)
