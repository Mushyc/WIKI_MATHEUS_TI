# 💀 Guia Técnico Kali Linux: Cheat Sheet de Elite
![Banner Kali](/banner_kali.png)
> **Nível:** Operacional | **Foco:** Comandos Rápidos e Referência
---

## 📖 Introdução: O Guia de Bolso

Um especialista não decora tudo, mas sabe onde encontrar a informação rápido. Este guia é o seu "Cheat Sheet" definitivo para quando você estiver no meio de um laboratório ou Pentest real e precisar do comando exato para uma ferramenta específica.

---

## 🕵️ Módulo 1: Comandos de Anonimato

| Objetivo | Comando |
| :--- | :--- |
| Trojanizar o MAC | `macchanger -r eth0` |
| Iniciar Serviço Tor | `service tor start` |
| Rodar via Proxy | `proxychains [comando]` |
| Limpar Histórico | `history -c` |

---

## 🔍 Módulo 2: Scan e Reconhecimento (Nmap)

### 📝 No seu Caderno (O "Combo" de Scan):
- `nmap -sS -sV -O -p- [IP]`: O scan mais completo. Tenta ser silencioso (`-sS`), pega versões (`-sV`), descobre o OS (`-O`) e varre TODAS as 65.535 portas (`-p-`).

---

## 🧨 Módulo 3: Senhas e Password Cracking

1.  **Hydra (Força Bruta):**
    `hydra -l [usuario] -P [lista_senhas.txt] [IP] ssh` - Tenta adivinhar a senha do SSH.
2.  **John the Ripper (Quebra de Hash):**
    `john --wordlist=[lista.txt] [arquivo_hash]` - Tenta quebrar a senha de um arquivo criptografado.

---

## 📝 Exercícios de Fixação (Para responder no caderno!)

1.  Qual comando do Nmap você usaria para descobrir apenas se um host está vivo (Ping Sweep)?
2.  Como você verifica o seu IP interno no Kali Linux via terminal?
3.  Qual a função da ferramenta **TheHarvester**?
4.  O que faz o comando `nmap -T4 -F [IP]`? (Dica: o `-F` é de Fast).
5.  Como você instalaria uma nova ferramenta no Kali que não veio instalada por padrão?
6.  Qual a diferença entre usar o Kali como **Live USB** e instalado em uma **Máquina Virtual**?
7.  Para que serve o comando `ip addr show`?
8.  O que é um **Dictionary Attack** dentro da quebra de senhas?
9.  Como o comando `dig` ajuda a coletar informações de um site?
10. **Desafio:** No seu caderno, escreva o comando completo do Nmap para varrer a rede `192.168.1.0/24` em busca de máquinas Windows ligadas.

---

### 🚀 Próximos Passos
- [🌐 Redes de Computadores](/guias/Curso_Redes_Computadores) - Domine os protocolos que você está escaneando.
- [🐧 Domínio Linux](/guias/Curso_Dominio_Linux) - Automatize seus comandos com scripts Bash.
- [🛠️ Ferramentas Pendrive](/guias/Curso_Ferramentas_Pendrive) - Aprenda a rodar o Kali direto do seu bolso.
