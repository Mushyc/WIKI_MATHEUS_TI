# 🧮 Fundamentos de Ciência da Computação: Master Class Edition

![Banner CS](/banner_cs.png)

A ciência por trás do código. Entenda como impulsos elétricos se transformam em softwares complexos. Este guia fornece a base teórica necessária para cursos superiores e para o desenvolvimento de arquiteturas de software de alta performance.

---

## 📂 Módulo 1: A Matemática da Máquina (Sistemas de Numeração)

Computadores não entendem "10", eles entendem estados de voltagem (Ligado/Desligado).

### 1.1 Binário e Hexadecimal
- **Binário (Base 2):** 0 e 1.
- **Hexadecimal (Base 16):** 0 a 9 + A a F. Usado para endereços de memória e cores CSS.

| Decimal | Binário | Hexadecimal |
| :--- | :--- | :--- |
| 10 | 1010 | A |
| 15 | 1111 | F |
| 255 | 11111111 | FF |

::: tip 💡 Cálculo de Bits
1 Byte = 8 Bits. O maior número que um Byte pode representar é **255** (2^8 - 1). É por isso que os canais de cores RGB vão de 0 a 255!
:::

---

## 🧠 Módulo 2: Arquitetura de Computadores (Von Neumann)

### 2.1 O Ciclo de Instrução (Fetch-Decode-Execute)
1.  **Busca (Fetch):** A CPU busca a instrução na RAM.
2.  **Decodificação:** A Unidade de Controle entende o que deve ser feito.
3.  **Execução:** A ALU (Unidade Lógica e Aritmética) faz a conta.

### 2.2 Hierarquia de Memória
A velocidade custa caro. Por isso usamos camadas:
1.  **Registradores:** Na CPU (Ultra rápidos, espaço minúsculo).
2.  **Cache (L1, L2, L3):** Perto da CPU (Muito rápidos).
3.  **RAM:** Memória principal (Rápida, volátil).
4.  **Armazenamento (SSD/HD):** Memória persistente (Lenta).

---

## ⚙️ Módulo 3: Sistemas Operacionais (O Maestro)

O SO é o software que gerencia o hardware e permite que vários programas rodem "ao mesmo tempo".

### 3.1 Gerenciamento de Processos e Escalonamento
Como o Windows decide qual programa ganha a atenção da CPU?
- **Round Robin:** Cada programa ganha um pequeno tempo (Time Slice).
- **Prioridade:** Processos críticos do sistema passam na frente.

### 3.2 O Kernel (Núcleo)
- **Monolítico (Linux/Windows):** Todo o gerenciamento de hardware está no núcleo. Mais rápido, mas um driver ruim pode derrubar o sistema (Tela Azul).
- **Microkernel:** Apenas o essencial está no núcleo. Mais estável e seguro, porém mais lento.

---

## 🔐 Módulo 4: Criptografia e Segurança Teórica

### 4.1 Hashing vs Criptografia
- **Hashing (SHA-256):** É uma via de mão única. Você transforma a senha em um código único, mas não consegue voltar ao original. Útil para salvar senhas no Banco de Dados.
- **Criptografia (AES/RSA):** É de mão dupla. Você tranca com uma chave e abre com outra.

### 4.2 Criptografia Assimétrica (Chaves Públicas)
A base da internet segura (HTTPS). Você envia sua **Chave Pública** para o mundo trancar a mensagem, mas apenas sua **Chave Privada** consegue abrir.

---

## 🧪 Módulo 5: Compiladores vs Interpretadores

Como o seu código vira algo que a CPU entende?
- **Compiladores (C++, Rust):** Traduzem o código inteiro antes de rodar. O resultado é um `.exe` ultra veloz.
- **Interpretadores (Python, JS):** Traduzem o código linha por linha enquanto rodam. Mais fácil de testar, mas um pouco mais lento.

::: info 🛡️ Caso Real: O Bug do Milênio
Em 1999, o mundo temeu o "Y2K". Muitos sistemas antigos guardavam o ano com apenas 2 dígitos (98, 99). Quando chegasse em 00, o computador acharia que era 1900, não 2000. Isso custou bilhões em revisões de código. **Lição:** Fundamentos de como os dados são guardados (Tipagem e Tamanho de Variáveis) evitam desastres globais.
:::

---

### Links de Referência Master
- [📊 Algoritmos e Estruturas de Dados](/guias/Curso_Algoritmos_Estruturas_Dados) - Aplicação da lógica.
- [🖥️ Montagem e Manutenção](/guias/Curso_Montagem_Manutencao_PC) - Teoria na prática do hardware.
- [🐧 Domínio do Linux](/guias/Curso_Dominio_Linux) - O Kernel na prática.
- [🎨 POO na Prática](/guias/Curso_POO_Pratica) - Abstração de software.
