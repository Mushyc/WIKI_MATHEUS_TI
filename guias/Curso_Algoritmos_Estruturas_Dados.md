# 📊 Algoritmos e Estruturas de Dados: Master Class Edition

![Banner Algoritmos](/banner_algoritmos.png)

Este é o alicerce de toda a computação de alto nível. Se você entende a lógica e como organizar os dados, você domina qualquer linguagem e resolve problemas que parecem impossíveis.

---

## 📈 Módulo 1: O Termômetro do Código (Notação Big O)

Como saber se seu código é rápido ou uma bomba de processamento? Usamos a notação Big O para medir a escalabilidade.

| Notação | Nome | Eficiência | Exemplo Real |
| :--- | :--- | :--- | :--- |
| **O(1)** | Constante | ⭐⭐⭐⭐⭐ | Pegar o primeiro item de uma lista. |
| **O(log n)**| Logarítmica | ⭐⭐⭐⭐ | Busca Binária (Dividir para conquistar). |
| **O(n)** | Linear | ⭐⭐⭐ | Percorrer uma lista inteira uma vez. |
| **O(n log n)**| Linearítmica | ⭐⭐ | Algoritmos de ordenação eficientes (MergeSort). |
| **O(n²)** | Quadrática | ❌ | Dois loops aninhados (Lento para dados grandes). |

```mermaid
graph LR
    O1["O(1) Perfeito"] --- OlogN["O(log n) Excelente"]
    OlogN --- ON["O(n) Aceitável"]
    ON --- ON2["O(n²) Perigoso"]
    
    style O1 fill:#27ae60,stroke:#fff,color:#fff
    style ON2 fill:#c0392b,stroke:#fff,color:#fff
```

---

## 🧱 Módulo 2: Estruturas Lineares (O Fluxo de Dados)

### 2.1 Pilhas (LIFO) e Filas (FIFO)
- **Pilhas (Last-In, First-Out):** O último a entrar é o primeiro a sair.
    - **Uso:** Função de "Desfazer" (Undo) no Word, Pilha de Chamadas (Call Stack).
- **Filas (First-In, First-Out):** O primeiro a entrar é o primeiro a sair.
    - **Uso:** Gerenciamento de processos na CPU, Fila de Impressão.

### 2.2 Listas Ligadas (Linked Lists)
Diferente de um Array (vetor), os itens não estão lado a lado na memória. Cada item (nó) sabe onde o próximo está através de um ponteiro.
- **Vantagem:** Inserir ou deletar itens no meio é muito rápido.

---

## 🔍 Módulo 3: Algoritmos de Busca e Ordenação

### 3.1 Busca Binária (O Poder do Log n)
Para buscar um número em 1 bilhão de registros:
- **Busca Linear:** Pode levar 1 bilhão de passos.
- **Busca Binária:** Leva apenas **30 passos**.
*A regra: A lista deve estar ordenada.*

### 3.2 Sorting (Ordenação)
| Algoritmo | Eficiência | Quando usar? |
| :--- | :--- | :--- |
| **Bubble Sort** | O(n²) | Apenas para grupos muito pequenos (didático). |
| **Quick Sort** | O(n log n) | Geralmente o mais rápido na prática. |
| **Merge Sort** | O(n log n) | Estável e garantido em pior caso. |

---

## 🌳 Módulo 4: Estruturas Não-Lineares (Árvores e Grafos)

### 4.1 Árvores Binárias de Busca (BST)
Imagine uma árvore onde tudo à esquerda é menor e tudo à direita é maior. Isso permite buscas instantâneas.
- **Uso:** Indexação de arquivos no Windows/Linux, Bancos de Dados SQL.

### 4.2 Grafos (A Teia de Conexões)
Conjunto de nós (Vértices) conectados por linhas (Arestas).
- **Uso:** Google Maps (Achar o caminho mais curto), Redes Sociais (Sugerir amigos), Roteamento de Internet (Protocolo BGP).

---

## 🧠 Módulo 5: Resolução de Problemas Profissional

::: info 🛡️ Caso Real: O Gargalo do Log
Um sistema de log de uma empresa salvava tudo em um arquivo de texto gigante. Para achar um erro, o script Python percorria o arquivo do início. O tempo de busca era de **15 minutos**. 
**Solução:** Implementei um **Hash Table (Dicionário)** que mapeia o timestamp para a posição do log. O tempo de busca caiu para **menos de 1 segundo**. **Estrutura de dados correta = Tempo economizado.**
:::

---

### Links de Referência Master
- [🎨 POO na Prática](/guias/Curso_POO_Pratica) - Transforme dados em objetos.
- [🐍 Python para Automação](/guias/Curso_Python_Automacao) - Implemente esses algoritmos.
- [🧮 Fundamentos CS](/guias/Curso_Fundamentos_CS) - Teoria da computação.
