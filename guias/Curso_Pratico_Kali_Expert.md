# 💀 Curso Prático Kali Linux Expert: Master Class Edition
> **Nível:** Intermediário ao Especialista | **Foco:** Pentest, Anonimato e Exploração
---

## 📖 Introdução: A Ética do Guerreiro

No mundo da cibersegurança, o Kali Linux é a sua armadura e o seu arsenal. Mas lembre-se: "Com grandes poderes vêm grandes responsabilidades". Use este conhecimento apenas em ambientes controlados (Labs) ou com autorização por escrito. O objetivo aqui é aprender a **defender** sistemas, pensando como um atacante.

---

## 🕵️ Módulo 1: Anonimato e Ocultação (Protocolo Ghost)

Um especialista nunca deixa rastros. Antes de qualquer teste, você precisa se tornar invisível.

### 📝 No seu Caderno (O Check-list do Fantasma):
1.  **MacChanger:** Altera o endereço físico da sua placa de rede (`macchanger -r eth0`).
2.  **Tor + Proxychains:** Faz sua conexão "pular" por vários países antes de chegar no alvo.
3.  **VPN:** Camada extra de túnel criptografado.
4.  **Limpeza de Logs:** Sempre use `history -c` ao terminar uma sessão.

---

## 🔍 Módulo 2: Reconhecimento e Scan (Nmap Profissional)

O reconhecimento é 70% de um Pentest. Se você não conhece o alvo, não consegue invadir.
*   `nmap -sV [IP]`: Descobre a versão dos serviços rodando.
*   `nmap -O [IP]`: Tenta descobrir qual o Sistema Operacional do alvo.
*   **Stealth Scan (`-sS`):** Um scan mais silencioso que não completa a conexão TCP, dificultando a detecção pelo Firewall.

---

## 🧨 Módulo 3: Exploração (Metasploit Framework)

O Metasploit é o maior banco de dados de falhas (exploits) do mundo.
- **Exploit:** O código que aproveita a falha.
- **Payload:** O que você quer que aconteça depois da invasão (ex: abrir um terminal remoto - Meterpreter).

### 📝 No seu Caderno (O Fluxo MSF):
*   `search [serviço]`: Procura a falha.
*   `use [caminho/do/exploit]`: Seleciona a arma.
*   `set RHOSTS [IP_ALVO]`: Mira no alvo.
*   `exploit`: Fogo!

---

## 📝 Exercícios de Fixação (Para responder no caderno!)

1.  O que diferencia um **Hacker Ético** de um Cibercriminoso?
2.  Para que serve o comando `macchanger` e por que ele é importante no início de um Pentest?
3.  Explique o que o **Nmap** faz quando usamos a flag `-sV`.
4.  O que é um **Exploit** e o que é um **Payload**?
5.  Qual a função do **Proxychains** e como ele ajuda no anonimato?
6.  O que o comando `netdiscover` faz em uma rede local?
7.  Como o comando `whois` ajuda na fase de reconhecimento de um domínio web?
8.  Qual a diferença entre um scan **TCP Connect** e um **SYN Scan**?
9.  O que é o **John the Ripper** e para que ele é usado?
10. **Desafio:** No seu caderno, descreva o passo a passo ético que você deve seguir antes de realizar um teste de invasão em uma empresa de um amigo.

---

### 🚀 Próximos Passos
- [🌐 Redes de Computadores](/guias/Curso_Redes_Computadores) - Sem entender redes, você nunca será um bom hacker.
- [🐧 Domínio Linux](/guias/Curso_Dominio_Linux) - O Kali é Linux; domine o terminal primeiro.
- [🐍 Python para Automação](/guias/Curso_Python_Automacao) - Crie suas próprias ferramentas de ataque.
