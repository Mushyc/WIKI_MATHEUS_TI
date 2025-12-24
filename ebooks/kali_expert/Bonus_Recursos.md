# 🎁 Bônus: The Ultimate Kali Cheat Sheet

Este é o seu guia rápido de bolso. Quando estiver no meio de um lab ou um teste real, consulte esta página para encontrar o comando exato que você precisa.

---

## 🕵️ Anonimato e Sistema
| Comando | O que faz? |
| :--- | :--- |
| `service tor start` | Inicia o serviço Tor para anonimato. |
| `proxychains4 [comando]` | Roda qualquer ferramenta via rede Tor. |
| `macchanger -r eth0` | Muda o endereço físico (MAC) para um aleatório. |
| `history -c` | Apaga o histórico de comandos do terminal. |

---

## 🔍 Reconhecimento (Nmap)
- **Scan Rápido:** `nmap -F [IP]`
- **Scan Completo:** `nmap -p- -sV -sC -O [IP]`
- **Scan Silencioso:** `nmap -sS -Pn [IP]`
- **Listar Subdomínios:** `theHarvester -d [alvo] -l 500 -b all`

---

## 🕷️ Exploração (Metasploit)
| Comando | O que faz? |
| :--- | :--- |
| `msfconsole` | Abre o console principal. |
| `search [nome]` | Busca exploits para um serviço específico. |
| `LHOST` | O **SEU** IP (onde você recebe a conexão). |
| `RHOST` | O IP da **VÍTIMA**. |
| `sessions -i [id]` | Interage com um shell aberto. |

---

## 📶 Wireless (Wi-Fi)
- **Modo Monitor:** `airmon-ng start wlan0`
- **Capturar Handshake:** `airodump-ng -c [canal] --bssid [MAC] -w [arquivo] wlan0mon`
- **Ataque de Deauth:** `aireplay-ng -0 5 -a [MAC] wlan0mon`
- **Brute Force:** `aircrack-ng -w wordlist.txt arquivo.cap`

---

## 🕸️ Web Hacking
- **SQLMap Básico:** `sqlmap -u "URL" --dbs`
- **Gobuster (Diretórios):** `gobuster dir -u URL -w wordlist.txt`
- **XSS Payload:** `<script>alert('xss')</script>`

---

## 📂 Recursos de Estudo Profissional

### Laboratórios para Prática (Legais)
- [TryHackMe](https://tryhackme.com) (Excelente para iniciantes)
- [Hack The Box](https://hackthebox.com) (Para quem quer desafio real)
- [VulnHub](https://vulnhub.com) (VMs para baixar e hackear offline)

### Documentação e Referências
- [Exploit Database](https://exploit-db.com) (Ondem ficam os exploits do mundo todo)
- [OWASP Foundation](https://owasp.org) (Referência em segurança web)
- [Kali Tools Documentation](https://www.kali.org/tools/) (Manual oficial)

---

> [!IMPORTANT]
> **A Prática Leva à Perfeição.** O melhor técnico não é o que decora todos os comandos, mas o que sabe exatamente **onde procurar** quando esquece. Guarde este bônus com você.
