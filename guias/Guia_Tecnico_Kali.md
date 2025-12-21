# 💀 Kali Linux: Guia Técnico de Elite

Este guia foca no **Top 10** de ferramentas essenciais para começar seus estudos de segurança e pentest.

---

## 1. Nmap (Network Mapper)
- **O que é:** O rei da varredura de rede.
- **Para que serve:** Descobrir máquinas ligadas e quais portas (serviços) estão abertas.
- **Comando Básico:** `nmap -sV 192.168.1.1` (Descobre serviços e versões).

## 2. Metasploit Framework
- **O que é:** Uma plataforma completa de exploração.
- **Para que serve:** Testar vulnerabilidades conhecidas e ganhar acesso (explorar).
- **Comando Básico:** `msfconsole` (Inicia o console).

## 3. Wireshark
- **O que é:** Analisador de tráfego de rede.
- **Para que serve:** "Ver" tudo o que passa pelo cabo ou Wi-Fi em tempo real.
- **Ação:** Interface gráfica para capturar pacotes.

## 4. Burp Suite
- **O que é:** Proxy para testes em aplicações Web.
- **Para que serve:** Interceptar e modificar requisições entre o navegador e o site.
- **Foco:** Encontrar falhas em sites/sistemas online.

## 5. John the Ripper
- **O que é:** Quebrador de senhas.
- **Para que serve:** Realizar ataques de força bruta ou dicionário contra arquivos de senhas.
- **Comando Básico:** `john --wordlist=lista.txt hash.txt`

## 6. Hydra
- **O que é:** Quebrador de login remoto em tempo real.
- **Para que serve:** Tentar senhas em serviços como SSH, FTP, Telnet.
- **Comando Básico:** `hydra -l admin -P senhas.txt ssh://192.168.1.1`

## 7. Aircrack-ng
- **O que é:** Suíte de auditoria Wi-Fi.
- **Para que serve:** Testar a segurança de senhas de redes Wi-Fi (WPA/WPA2).
- **Foco:** Redes sem fio.

## 8. SQLmap
- **O que é:** Automatizador de SQL Injection.
- **Para que serve:** Encontrar falhas em bancos de dados de sites automaticamente.
- **Comando Básico:** `sqlmap -u "http://site.com/id=1" --dbs`

## 9. Social Engineering Toolkit (SET)
- **O que é:** Ferramenta para engenharia social.
- **Para que serve:** Criar páginas falsas (phishing) para testar se usuários caem em golpes.
- **Comando Básico:** `setoolkit`

## 10. Gobuster
- **O que é:** Localizador de diretórios ocultos.
- **Para que serve:** Encontrar pastas "escondidas" em sites (ex: /admin, /config).
- **Comando Básico:** `gobuster dir -u http://site.com -w lista.txt`

---

> [!TIP]
> **Dica de Ouro:** O comando `man [ferramenta]` (ex: `man nmap`) dentro do terminal do Kali abre o manual completo de qualquer ferramenta.
