# 🕸️ Capítulo 5: Web Hacking (A Invasão de Sites)

A web é a maior superfície de ataque do planeta. Praticamente tudo o que usamos hoje é uma aplicação web. Neste capítulo, aprenderemos como encontrar falhas em sites, extrair bancos de dados inteiros e entender o **OWASP Top 10**, o manual das maiores vulnerabilidades do mundo.

---

## 🏗️ 5.1 Burp Suite: O Coração do Web Hacker

O Burp Suite é um "Proxy". Ele fica entre o seu navegador e o site, permitindo que você intercepte e altere os dados antes que eles cheguem ao servidor.

**Como Usar:**
1. Configure o navegador para usar o Proxy do Burp (127.0.0.1:8080).
2. Tente fazer um login no site.
3. No Burp, vá em `Proxy > Intercept`. Altere sua senha antes de clicar em "Forward".
4. Veja como o servidor responde a dados manipulados.

---

## 🛢️ 5.2 SQL Injection (O Roubo de Dados)

O SQLi ocorre quando um site aceita comandos de banco de dados diretamente em campos de texto (como login ou busca).

### 5.2.1 Automatizando com SQLMap
O `sqlmap` é a ferramenta definitiva que faz todo o trabalho duro de "conversar" com o banco de dados por você.

**Comando de Elite:**
```bash
sqlmap -u "https://alvo.com/produto.php?id=10" --dbs
```
- `-u`: A URL alvo (que tenha um parâmetro, como `?id=`).
- `--dbs`: Lista todos os **Bancos de Dados** do servidor.
- `--tables`: Lista as tabelas (ex: `Usuarios`).
- `--dump`: Extrai os logins e senhas da tabela.

---

## ⚡ 5.3 XSS (Cross-Site Scripting)

O XSS permite que você injete código JavaScript no navegador de **outro usuário**. Se bem sucedido, você pode roubar o **Cookie de Sessão** (o que permite entrar na conta dele sem senha).

**Payload de Teste Simples:**
Coloque isso em um campo de comentário ou busca:
```html
<script>alert('Você foi Hackeado!')</script>
```
Se o alerta aparecer na tela ao carregar a página, o site está vulnerável.

---

## 📂 5.4 Directory Brute-force (Achando Pastas Ocultas)

Muitos sites deixam pastas de administração (`/admin`) ou backups (`/backup.zip`) expostos. Use o **Dirb** ou **Gobuster** para encontrá-los.

```bash
gobuster dir -u https://alvo.com -w /usr/share/wordlists/dirb/common.txt
```

::: warning 🛡️ Regra de Ouro: Web Application Firewall (WAF)
Sites modernos usam firewalls (como Cloudflare) que bloqueiam o SQLMap ou Gobuster rapidamente. No Capítulo 6, falaremos sobre como ser mais sutil.
:::

---

## 🧪 Desafio do Mestre: O Bug Bounty Hunter
1. Escolha um laboratório legal (ex: `DVWA` ou `bWAPP`).
2. Use o `Burp Suite` para interceptar a requisição de login.
3. Use o `SQLMap` para extrair os usuários do banco de dados do lab.
4. **Resultado:** Você acabou de fazer a sua primeira auditoria de banco de dados.

---

> [!TIP]
> **A Fase Final:** Você já sabe invadir. Agora, precisamos aprender a **ficar** lá dentro e como apresentar esse trabalho de forma que ele valha dinheiro. Vamos para o **Capítulo 6: Pós-Exploração e Relatórios**.
