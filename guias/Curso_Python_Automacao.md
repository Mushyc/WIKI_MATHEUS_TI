# 🐍 Curso: Python para Automação de TI

Aprenda Python focado em RESOLVER problemas reais do dia a dia de técnico.

---

## 📚 Módulo 1: Python Básico Express

### Instalação
**Windows:** Baixe de python.org (marque "Add to PATH")
**Linux:** Já vem instalado (teste com `python3 --version`)

### Seu Primeiro Script
```python
# ola_mundo.py
print("Olá, Mundo!")
```

Execute: `python ola_mundo.py`

### Variáveis e Tipos
```python
nome = "Matheus"           # String
idade = 25                 # Integer
altura = 1.75              # Float
ativo = True               # Boolean

print(f"Nome: {nome}, Idade: {idade}")  # f-string
```

### Estruturas de Controle
```python
# IF/ELSE
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# FOR
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# WHILE
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

### Listas e Dicionários
```python
# Lista (array)
ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
print(ips[0])  # Primeiro elemento

# Dicionário (chave-valor)
servidor = {
    "hostname": "SRV-WEB-01",
    "ip": "192.168.1.100",
    "status": "online"
}
print(servidor["hostname"])
```

### Funções
```python
def verificar_ping(ip):
    import os
    resultado = os.system(f"ping -n 1 {ip}")
    if resultado == 0:
        return "Online"
    else:
        return "Offline"

print(verificar_ping("8.8.8.8"))
```

---

## 🛠️ Módulo 2: Automações para Técnicos

### Script 1: Ping em Massa
```python
import os

ips = ["192.168.1.1", "192.168.1.10", "192.168.1.20", "8.8.8.8"]

for ip in ips:
    resposta = os.system(f"ping -n 1 {ip} > nul")
    if resposta == 0:
        print(f"✅ {ip} - ONLINE")
    else:
        print(f"❌ {ip} - OFFLINE")
```

### Script 2: Verificar Espaço em Disco
```python
import shutil

def verificar_disco(caminho):
    total, usado, livre = shutil.disk_usage(caminho)
    
    total_gb = total // (2**30)
    livre_gb = livre // (2**30)
    percentual_usado = (usado / total) * 100
    
    print(f"Disco: {caminho}")
    print(f"Total: {total_gb} GB")
    print(f"Livre: {livre_gb} GB")
    print(f"Usado: {percentual_usado:.1f}%")
    
    if percentual_usado > 90:
        print("⚠️ ALERTA: Disco quase cheio!")

verificar_disco("C:\\")
```

### Script 3: Listar Processos por Uso de CPU
```python
import psutil

processos = []
for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
    processos.append(proc.info)

# Ordenar por CPU (maior primeiro)
processos_ordenados = sorted(processos, key=lambda x: x['cpu_percent'], reverse=True)

print("Top 10 Processos por CPU:")
for i, proc in enumerate(processos_ordenados[:10], 1):
    print(f"{i}. {proc['name']} - CPU: {proc['cpu_percent']}% - PID: {proc['pid']}")
```

### Script 4: Backup Automático de Pastas
```python
import shutil
from datetime import datetime
import os

def fazer_backup(origem, destino_base):
    # Criar nome com data
    data_atual = datetime.now().strftime("%Y%m%d_%H%M%S")
    destino = os.path.join(destino_base, f"backup_{data_atual}")
    
    # Copiar pasta
    shutil.copytree(origem, destino)
    print(f"✅ Backup concluído: {destino}")

# Uso
fazer_backup("C:\\Documentos", "D:\\Backups")
```

### Script 5: Renomear Arquivos em Massa
```python
import os

def renomear_em_massa(pasta, prefixo):
    arquivos = os.listdir(pasta)
    
    for i, arquivo in enumerate(arquivos, 1):
        extensao = os.path.splitext(arquivo)[1]
        novo_nome = f"{prefixo}_{i:03d}{extensao}"
        
        caminho_antigo = os.path.join(pasta, arquivo)
        caminho_novo = os.path.join(pasta, novo_nome)
        
        os.rename(caminho_antigo, caminho_novo)
        print(f"Renomeado: {arquivo} → {novo_nome}")

# Uso: renomeia todos os arquivos como "foto_001.jpg", "foto_002.jpg"
renomear_em_massa("C:\\Fotos", "foto")
```

---

## 📁 Módulo 3: Manipulação de Arquivos

### Ler Arquivo de Texto
```python
with open("log.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
```

### Escrever em Arquivo
```python
with open("relatorio.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Relatório de Manutenção\n")
    arquivo.write("Data: 21/12/2025\n")
```

### Processar CSV
```python
import csv

# Ler CSV
with open("usuarios.csv", "r") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(f"Nome: {linha['nome']}, Email: {linha['email']}")

# Escrever CSV
dados = [
    {"nome": "João", "email": "joao@email.com"},
    {"nome": "Maria", "email": "maria@email.com"}
]

with open("saida.csv", "w", newline="") as arquivo:
    campos = ["nome", "email"]
    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    
    escritor.writeheader()
    escritor.writerows(dados)
```

---

## 🌐 Módulo 4: Requisições Web (APIs)

### Buscar Dados de API
```python
import requests

# Buscar CEP
cep = "01310100"
resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
dados = resposta.json()

print(f"Logradouro: {dados['logradouro']}")
print(f"Bairro: {dados['bairro']}")
print(f"Cidade: {dados['localidade']}")
```

### Verificar Status de Sites
```python
import requests

sites = [
    "https://google.com",
    "https://github.com",
    "https://stackoverflow.com"
]

for site in sites:
    try:
        resposta = requests.get(site, timeout=5)
        if resposta.status_code == 200:
            print(f"✅ {site} - ONLINE")
        else:
            print(f"⚠️ {site} - Código {resposta.status_code}")
    except:
        print(f"❌ {site} - OFFLINE ou timeout")
```

---

## ⏰ Módulo 5: Agendamento de Tarefas

### Executar Script a Cada X Segundos
```python
import time

def tarefa_periodica():
    print("Executando verificação...")
    # Seu código aqui

while True:
    tarefa_periodica()
    time.sleep(300)  # 300 segundos = 5 minutos
```

### Agendar com Schedule
```python
import schedule
import time

def backup():
    print("Fazendo backup...")
    # Código do backup

# Agendar para rodar todo dia às 3h da manhã
schedule.every().day.at("03:00").do(backup)

# Rodar a cada hora
schedule.every().hour.do(backup)

while True:
    schedule.run_pending()
    time.sleep(60)
```

---

## 📧 Módulo 6: Enviar Emails Automaticamente

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email(destinatario, assunto, corpo):
    # Configurações
    remetente = "seu_email@gmail.com"
    senha = "sua_senha_app"  # Use senha de app do Gmail
    
    # Criar mensagem
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.attach(MIMEText(corpo, 'plain'))
    
    # Enviar
    with smtplib.SMTP('smtp.gmail.com', 587) as servidor:
        servidor.starttls()
        servidor.login(remetente, senha)
        servidor.send_message(msg)
    
    print("Email enviado!")

# Uso
enviar_email(
    "cliente@email.com",
    "Manutenção Concluída",
    "A manutenção do seu PC foi finalizada com sucesso."
)
```

---

## 🎯 Projetos Práticos para Portfólio

### Projeto 1: Monitor de Saúde do Sistema
Crie um script que:
- Verifica CPU, RAM e disco
- Se algum estiver acima de 80%, envia alerta
- Salva log em arquivo com timestamp

### Projeto 2: Organizador de Downloads
Crie um script que:
- Monitora pasta de Downloads
- Move PDFs para "Documentos"
- Move imagens para "Imagens"
- Move vídeos para "Vídeos"

### Projeto 3: Gerador de Relatórios
Crie um script que:
- Faz ping em lista de servidores
- Verifica portas abertas
- Gera relatório HTML com resultados

---

## 📚 Bibliotecas Essenciais para Instalar

```bash
pip install requests      # Requisições HTTP
pip install psutil        # Informações do sistema
pip install schedule      # Agendamento
pip install openpyxl      # Trabalhar com Excel
pip install pandas        # Análise de dados
pip install pyautogui     # Automação de GUI
```

---

## 🎓 Para a Faculdade

Na faculdade você vai aprender:
- Algoritmos e estruturas de dados
- Programação orientada a objetos
- Complexidade computacional

**Vantagem que você já tem:**
- Sabe resolver problemas REAIS
- Conhece a sintaxe básica
- Só precisa entender a TEORIA por trás

---

## 📖 Recursos de Estudo

**Gratuitos:**
- Automate the Boring Stuff with Python (livro online)
- Python.org Docs
- Real Python (blog)

**Práticas:**
- Codecademy (Python Track)
- HackerRank (Python Challenges)

---

**Veja também:**
- [Domínio do Linux](/guias/Curso_Dominio_Linux) (combinar Python + Shell = poder)
- [Desenvolvimento Web](/guias/Guia_Desenvolvimento_Web) (backend com Python)
