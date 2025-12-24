# 💀 Capítulo 1: O Preparo do Campo de Batalha (Predator's Setup)

Bem-vindo à arena. Antes de disparar o primeiro comando, você precisa entender que no mundo do Hacking Ético, a sua maior arma não é o seu conhecimento em exploits, mas sim a sua **invisibilidade**. Um predador barulhento nunca captura sua presa.

Neste capítulo, vamos configurar o seu laboratório de forma que você seja um "fantasma" digital.

---

## 🕵️ 1.1 O Protocolo Ghost (Anonimato Absoluto)

No Kali, ser anônimo não é apenas usar uma VPN. É garantir que nenhum dado saia da sua rede sem ser mascarado.

### 1.1.1 Proxychains & Tor (Sua Sombra)
O Proxychains permite que você "encadeie" vários servidores proxy. Se um hacker te rastrear, ele vai chegar na Holanda, depois no Japão, depois na Rússia, antes de chegar (talvez) em você.

**Configuração Passo a Passo:**
1. Instale o serviço Tor: `sudo apt install tor -y`
2. Ative o Tor: `sudo service tor start`
3. Configure o Proxychains: `sudo nano /etc/proxychains4.conf`
   - Remova o `#` de `dynamic_chain`.
   - Adicione `#` em `strict_chain`.
   - No final do arquivo, garanta que tenha: `socks5 127.0.0.1 9050`.

**Uso Profissional:**
Para rodar qualquer ferramenta (como o Nmap) via Proxychains:
```bash
proxychains4 nmap -sT -PN 8.8.8.8
```

---

## 🎭 1.2 MacChanger (Mudando sua Identidade de Fábrica)

O endereço MAC é a sua assinatura física no mundo. Se você está em uma rede Wi-Fi pública e usa seu MAC original, você já era.

**Comando de Elite:**
```bash
sudo ifconfig eth0 down
sudo macchanger -r eth0
sudo ifconfig eth0 up
```
*Dica: O `-r` gera um MAC aleatório de um fabricante real (Apple, Samsung, Intel), o que te faz parecer um dispositivo comum na rede.*

---

## ⚡ 1.3 O Terminal do Guerreiro (Customização para Velocidade)

Um hacker lento é um hacker capturado. Vamos otimizar o seu terminal (ZSH) para que você tenha informações vitais na tela o tempo todo.

### 1.3.1 Aliases Indispensáveis
Não perca tempo digitando comandos longos. Adicione isso ao seu `.zshrc`:
```bash
alias update='sudo apt update && sudo apt upgrade -y'
alias myip='curl ifconfig.me'
alias sniff='sudo tshark -i eth0'
```

---

## 🧪 Desafio do Mestre: O Teste de Vazamento

Não confie apenas na teoria. Prove que você é invisível:
1. Ative seu `Proxychains` com `Tor`.
2. Rode o comando: `proxychains4 firefox dnsleaktest.com`.
3. Se os IPs que aparecerem forem de outros países e não do seu provedor, **você passou no teste.**

::: warning ⚠️ Regra de Ouro
Nunca confie em uma única camada de segurança. Use VPN + Proxychains + MAC Randomizer. Se uma falhar, as outras te protegem.
:::

---

> [!TIP]
> No próximo capítulo, vamos aprender a **Coleta de Informações (OSINT)**, onde você aprenderá a descobrir segredos de empresas e pessoas usando apenas ferramentas públicas. A caçada está apenas começando.
