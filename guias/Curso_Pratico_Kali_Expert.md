# 🎓 Curso Prático: Engenharia de Segurança Kali Linux

Este curso foca na **prática real**. Não é só digitar comandos, é saber **por que** usar cada um.

---

## 🛰️ MÓDULO 1: Reconhecimento Dinâmico (NMAP)
**Cenário:** Você chegou em um cliente e ele quer saber o que tem ligado na rede.

1. **Varredura Rápida (Ping Sweep):**
   `nmap -sn 192.168.1.0/24`
   *Serve para ver quem está vivo sem chamar atenção.*

2. **Varredura de Serviços e Versões:**
   `nmap -sV -p 80,443 [IP]`
   *Identifica o que está rodando exatamente na porta.*

---

## 🕷️ MÓDULO 2: Exploração de Falhas (Metasploit)
**Cenário:** Você descobriu que o Windows do servidor está desatualizado.

1. **Busca de Exploit:**
   `msfconsole` -> `search bluekeep`
2. **Configuração:**
   `use [caminho_do_exploit]` -> `set RHOSTS [IP_ALVO]`
3. **Ataque:**
   `exploit`

---

## 🕵️ MÓDULO 3: Sniffing e Engenharia Social (Wireshark & SET)
**Cenário:** Testar se as senhas internas do escritório passam limpas (sem criptografia) na rede.

1. **Captura:** Abra o Wireshark, escolha a interface (eth0 ou wlan0) e use o filtro `http`.
2. **Engenharia:** Use o SET (`setoolkit`) para clonar a página de login do roteador e ver se os funcionários caem.

---

## 🔐 MÓDULO 4: Cracking de Alta Performance (John & Hydra)
**Cenário:** Você capturou um arquivo de backup com senhas criptografadas.

1. **John (Offline):** Use o John para quebrar o hash usando uma wordlist potente como a `rockyou.txt`.
2. **Hydra (Online):** Se o cliente usa senhas padrões tipo `admin123`, o Hydra resolve rápido.

---

## 🛠️ Exercício de Fixação (Missão 01)
*Objetivo: Descobrir o sistema operacional do seu próprio roteador e quais portas estão abertas.*
**Dica:** Use o comando `nmap -O [IP_DO_ROTEADOR]`.

---

> [!IMPORTANT]
> **Ética Profissional:** Use este conhecimento apenas em ambientes controlados ou com autorização por escrito. O Pen-drive com persistência permite que você salve os logs de cada ataque para estudar depois.
