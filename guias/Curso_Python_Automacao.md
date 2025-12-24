# 🐍 Python para Automação de TI: Master Class Edition

![Banner Python](/banner_python.png)

Aprenda a criar robôs que trabalham por você. No mundo da TI de elite, não trabalhamos duro, trabalhamos de forma inteligente. Este guia transforma você de um digitador em um arquiteto de automações.

---

## 📂 Módulo 1: O Ambiente de Desenvolvimento (Lab do Desenvolvedor)

Um profissional nunca polui o Python do sistema. Usamos Ambientes Virtuais (VENV).

### 1.1 Isolamento de Projeto
```bash
python -m venv .venv        # Cria o ambiente
source .venv/bin/activate  # Ativa (Linux)
.venv\Scripts\activate     # Ativa (Windows)
```

### 1.2 Gestão de Ferramentas
Use o `pip` para instalar bibliotecas de guerra:
- `pip install requests`: O rei das requisições web.
- `pip install pandas`: Manipulação de dados e planilhas.
- `pip install selenium`: Automação de navegador (clicar em botões).
- `pip install psutil`: Controle total dos recursos do Hardware.

---

## 🕸️ Módulo 2: Web Scraping e Consumo de APIs

A internet é o seu banco de dados. Aprenda a extrair informações automaticamente.

### 2.1 Requisições com `Requests` e `JSON`
A maioria das APIs modernas fornece dados em formato JSON.
```python
import requests

response = requests.get("https://api.exemplo.com/dados")
if response.status_code == 200:
    dados = response.json()
    print(f"Sucesso! Recebido: {dados['status']}")
else:
    print(f"Erro {response.status_code}")
```

### 2.2 Web Scraping com `BeautifulSoup`
Quando o site não tem API, nós "raspamos" o HTML.
- **Utilidade:** Monitorar preços de hardware, capturar notícias de segurança ou verificar mudanças em sites de clientes.

---

## 🤖 Módulo 3: Automação de Sistemas e Redes

### 3.1 O "Canivete Suíço" das Funções de TI
| Funcionalidade | Biblioteca | Comando Exemplo |
| :--- | :--- | :--- |
| **Mover Arquivos** | `shutil` | `shutil.move(origem, destino)` |
| **Executar Comandos**| `subprocess` | `subprocess.run(["nmap", "-sT", ip])` |
| **Monitoramento** | `psutil` | `psutil.cpu_percent(interval=1)` |
| **E-mail Automático**| `smtplib` | Enviar relatórios de erro para o suporte. |

---

## 🛡️ Módulo 4: Scripts Robustos (Tratamento de Erros e Logs)

Um script que trava sem dizer o porquê é um script inútil.

### 4.1 Try / Except / Finally
```python
try:
    with open("configuracao.txt", "r") as f:
        config = f.read()
except FileNotFoundError:
    print("❌ Erro: Arquivo de configuração não encontrado!")
    # Aqui você poderia criar um arquivo padrão
except Exception as e:
    print(f"⚠️ Ocorreu um erro inesperado: {e}")
finally:
    print("🔚 Processamento finalizado.")
```

### 4.2 Logging (O Diário do Robô)
Em vez de `print()`, use a biblioteca `logging` para salvar os erros em um arquivo `.log`. Isso permite que você saiba o que deu errado de madrugada sem precisar estar na frente do PC.

---

## 🚀 Módulo 5: Projeto Final - O Organizador de Servidores

::: details 🛠️ Laboratório: Automação Total de Documentos (Clique para expandir)
Este script monitora pastas e move arquivos para as categorias corretas, mantendo o servidor limpo.
```python
import os
import shutil

# Configurações
DOWNLOADS_DIR = "C:/Gestao/Entrada"
MAP_EXTENSOES = {
    "PDFs": [".pdf"],
    "Executaveis": [".exe", ".msi"],
    "Imagens": [".jpg", ".png", ".webp"]
}

def organizar():
    for arquivo in os.listdir(DOWNLOADS_DIR):
        ext = os.path.splitext(arquivo)[1].lower()
        for pasta, extensoes in MAP_EXTENSOES.items():
            if ext in extensoes:
                caminho_pasta = os.path.join(DOWNLOADS_DIR, pasta)
                os.makedirs(caminho_pasta, exist_ok=True)
                shutil.move(os.path.join(DOWNLOADS_DIR, arquivo), os.path.join(caminho_pasta, arquivo))

if __name__ == "__main__":
    organizar()
    print("✨ Sistema Organizado!")
```
:::

---

### Links de Referência Master
- [🌐 Redes de Computadores](/guias/Curso_Redes_Computadores) - Integre Python com scans de rede.
- [🐧 Domínio do Linux](/guias/Curso_Dominio_Linux) - Rode seus scripts em modo servidor.
- [🗄️ Banco de Dados Avançado](/guias/Curso_Banco_Dados_Avancado) - Salve os dados da sua automação.
