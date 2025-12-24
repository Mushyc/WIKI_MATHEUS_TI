# 🔍 Capítulo 2: A Arte do Reconhecimento (OSINT & Scans)

Hacking não é sair tentando quebrar portas. Hacking é encontrar a porta que foi deixada aberta por engano. 90% de um ataque bem-sucedido acontece no **Reconhecimento**.

Neste capítulo, vamos aprender a mapear o seu alvo sem que ele saiba que você existe.

---

## 🌎 2.1 OSINT: Inteligência de Fontes Abertas

OSINT é a arte de coletar informações públicas para criar um dossiê do alvo.

### 2.1.1 Google Dorks (Pesquisa Avançada)
O Google é seu melhor amigo. Use estes comandos para encontrar arquivos "escondidos":
- `site:alvo.com filetype:pdf`: Encontra todos os PDFs do site (podem ter metadados valiosos).
- `site:alvo.com intitle:"index of"`: Encontra diretórios expostos.
- `site:alvo.com intext:"password"`: Busca por senhas em texto puro no site.

---

## 🕸️ 2.2 Automatizando a Coleta com TheHarvester

O `theHarvester` é uma ferramenta que busca e-mails, subdomínios, IPs e nomes de funcionários em motores de busca (Google, Bing, LinkedIn).

**Comando Profissional:**
```bash
theHarvester -d empresa.com -l 500 -b google
```
*Tradução: Busque pela "empresa.com", limite a 500 resultados, usando o motor do Google.*

---

## 🛰️ 2.3 Mapeamento de Rede (Nmap Expert)

Agora que temos o domínio, precisamos saber o que está rodando nos servidores. O Nmap é a ferramenta definitiva para isso.

### 2.3.1 O Scan Silencioso (Stealth Scan)
O parâmetro `-sS` envia um pacote SYN mas não fecha a conexão (não completa o Three-way Handshake). Isso faz com que o scan não seja registrado em muitos logs antigos.

**O Comando "Canivete Suíço":**
```bash
sudo nmap -sS -sV -O -p- 192.168.1.1
```
- `-sS`: Stealth Scan.
- `-sV`: Detecta a **versão** do serviço (ex: Apache 2.4.41).
- `-O`: Detecta o **Sistema Operacional**.
- `-p-`: Escaneia as **65.535 portas** (demora mais, mas é completo).

---

## 🛠️ 2.4 Metadados: A Digital Invisível

Ao baixar um PDF ou imagem de um site, você pode usar o `ExifTool` para ver quem criou o arquivo, qual programa usou e às vezes até as coordenadas GPS de onde a foto foi tirada.

```bash
exiftool documento_secreto.pdf
```

---

## 🧪 Desafio do Mestre: O Dossiê Digital
1. Escolha um domínio de teste (ex: `hackthissite.org`).
2. Use o Google Dorks para achar arquivos PDFs.
3. Use o `theHarvester` para listar possíveis subdomínios.
4. Use o `Nmap` para ver quais portas estão abertas no servidor principal.

::: info 🛡️ Por que fazemos isso?
Ao mapear o alvo, você descobre que ele usa um "servidor Windows Server 2008" (Antigo e vulnerável) ou que o funcionário "João Silva" usa o e-mail `joao@empresa.com`. Isso será a base do seu ataque no próximo capítulo.
:::

---

> [!TIP]
> No próximo capítulo, vamos entrar na fase de **Exploração (Ataque)**, usando o poderoso Metasploit para transformar essas vulnerabilidades em acesso real. Prepare seus exploits!
