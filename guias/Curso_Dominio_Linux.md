# 🐧 Domínio do Linux: Master Class Edition
![Banner Linux](/banner_linux.png)
> **Nível:** Iniciante ao Administrador | **Foco:** Shell, Arquitetura e Servidores
---

## 📖 Introdução: O que é o Linux?

O Linux não é apenas um sistema operacional, é um **Kernel** (o coração do sistema). Ele nasceu para ser livre, estável e poderoso. Enquanto no Windows você clica em botões, no Linux você dá ordens diretas através do **Terminal**. Dominar o Linux é como ter a chave mestra de qualquer servidor ou supercomputador do mundo.

---

## 🏗️ Módulo 1: A Estrutura de Diretórios (O Mapa)

Diferente do Windows (C:\, D:\), no Linux tudo começa na raiz: `/`.

### 📂 Diretórios Essenciais (Anote no Caderno!):
*   `/bin` e `/usr/bin`: Onde moram as ferramentas (comandos) que você usa.
*   `/etc`: Aqui fica o cérebro do sistema. Todos os arquivos de configuração estão aqui.
*   `/var`: Local onde os dados que mudam ficam (logs de erro, bancos de dados).
*   `/home`: Onde ficam os usuários comuns (o seu "Meus Documentos").
*   `/root`: A casa do superusuário. Ninguém entra aqui sem permissão.
*   `/tmp`: Arquivos temporários que são apagados ao reiniciar.

---

## 👤 Módulo 2: O Poder do Superusuário (Root vs Sudo)

No Linux, existe um deus chamado **Root**. Ele pode apagar todo o sistema com um comando. Por segurança, usamos o **Sudo** (SuperUser Do).

### 📝 No seu Caderno:
- **Usuario Comum ($):** Pode fazer coisas básicas.
- **Root (#):** Tem poder total sobre o hardware e software.
- **Sudo:** É como pedir permissão momentânea ao Root para uma tarefa específica.

---

## 🔐 Módulo 3: Permissões de Arquivos (r-w-x)

Cada arquivo no Linux tem 3 tipos de donos e 3 tipos de poderes:

1.  **Dono (User):** Quem criou.
2.  **Grupo (Group):** Membros do time.
3.  **Outros (Other):** O resto do mundo.

### 📝 A Linguagem Proibida (Matemática Binária):
*   **Read (Ler):** 4
*   **Write (Escrever):** 2
*   **Execute (Executar):** 1

**Exemplo:** Um comando `chmod 755 arquivo` significa:
- **7** (4+2+1): Dono pode tudo.
- **5** (4+0+1): Grupo pode ler e executar.
- **5** (4+0+1): Outros podem ler e executar.

---

## ⚙️ Módulo 4: Manipulação de Texto e Pipes

O Linux trata tudo como se fosse um arquivo de texto. Isso permite que você combine comandos usando o caractere "Pipe" (`|`).

### 📝 Comandos que você vai usar TODO DIA:
*   `ls -la`: Lista tudo com detalhes.
*   `cat [arquivo]`: Lê o que está dentro do arquivo.
*   `grep "palavra"`: Filtra apenas a linha que tem o que você busca.
*   `nano` ou `vim`: Editores de texto direto no terminal.

**O Combo Mestre:**
```bash
cat logs.txt | grep "erro"
# Lê o arquivo e mostra APENAS as linhas que têm erro.
```

---

## 🛠️ Módulo 5: Monitoramento e Gerenciamento

Um administrador precisa saber se o servidor está "vivo".
1.  `top` ou `htop`: O "Gerenciador de Tarefas" do Linux.
2.  `df -h`: Mostra quanto espaço ainda tem no disco.
3.  `systemctl status [serviço]`: Verifica se um site ou banco de dados está rodando.

---

## 📝 Exercícios de Fixação (Para responder no caderno!)

1.  Qual diretório do Linux armazena os arquivos de configuração do sistema?
2.  Qual a diferença entre o símbolo `$` e o símbolo `#` no prompt do terminal?
3.  Se um arquivo tem permissão `chmod 777`, o que isso significa na prática? (E por que isso é perigoso?)
4.  Para que serve o comando `cd ..` e como ele difere do `cd /`?
5.  Como você faria para ler um arquivo chamado `config.txt` mas exibindo apenas as linhas que contém a palavra \"senha\"?
6.  Qual comando usamos para mudar o dono de um arquivo (**Owner**)?
7.  Como você verifica quanto de memória RAM o sistema está usando no momento?
8.  O que acontece se você rodar o comando `rm -rf /` como Root? (Não teste!)
9.  Para que serve o comando `mkdir -p curso/linux/aula1`?
10. **Desafio:** Imagine que você baixou um script e ele não quer rodar, dizendo \"Permissão negada\". Qual comando de 3 números você usaria para dar poder total de execução para você (dono)?

---

### 🚀 Próximos Passos
- [🐍 Python e Automação](/guias/Curso_Python_Automacao) - Aprenda a automatizar o Linux com código.
- [🏢 Windows Server & AD](/guias/Curso_Windows_Server_AD) - Veja como o Linux conversa com o Windows.
- [💀 Kali Linux Expert](/guias/Curso_Pratico_Kali_Expert) - Use seu domínio do Linux para segurança ofensiva.
