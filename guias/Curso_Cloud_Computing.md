# ☁️ Curso: Cloud Computing Essentials

Fundamentos de computação em nuvem para entrar no mercado que mais cresce em TI.

---

## 📚 Módulo 1: O que é Cloud Computing?

### Definição
**Cloud Computing** = Usar recursos de TI (servidores, storage, bancos de dados) através da internet, pagando apenas pelo que usar.

### Vantagens vs Data Center Próprio
| Tradicional | Cloud |
|------------|-------|
| Compra de servidores | Aluguel por demanda |
| Manutenção física | Provedor cuida |
| Capacidade fixa | Escalável |
| Custo inicial alto | Pague conforme usa |
| Demora para provisionar | Instantâneo |

### Modelos de Serviço

**IaaS (Infrastructure as a Service)**
- Você gerencia: SO, apps, dados
- Provedor gerencia: Hardware, rede, storage
- Exemplo: AWS EC2, Azure Virtual Machines

**PaaS (Platform as a Service)**
- Você gerencia: Só os apps e dados
- Provedor gerencia: SO, runtime, middleware
- Exemplo: AWS Elastic Beanstalk, Azure App Service

**SaaS (Software as a Service)**
- Você usa pronto
- Provedor gerencia TUDO
- Exemplo: Gmail, Office 365, Salesforce

---

## ☁️ Módulo 2: AWS (Amazon Web Services)

### Principais Serviços

**EC2 (Elastic Compute Cloud)**
- Máquinas virtuais na nuvem
- Escolhe: CPU, RAM, Disco, SO
- Pague por hora/segundo de uso

**S3 (Simple Storage Service)**
- Armazenamento de objetos (arquivos)
- Alta disponibilidade (99.999999999%)
- Casos de uso: Backup, hospedagem de imagens

**RDS (Relational Database Service)**
- Banco de dados gerenciado
- PostgreSQL, MySQL, SQL Server, Oracle
- Backup automático, alta disponibilidade

**Lambda**
- Código serverless (sem gerenciar servidor)
- Pague apenas quando o código executar
- Exemplo: Processar imagem quando uploadada no S3

**VPC (Virtual Private Cloud)**
- Rede virtual isolada
- Definir sub-redes, firewalls, VPNs

---

## 🔷 Módulo 3: Azure (Microsoft)

### Principais Serviços

**Virtual Machines**
- Equivalente ao EC2 da AWS
- Integração com Windows Server/Active Directory

**App Service**
- Hospedar aplicações web (Node, Python, .NET)
- Auto-scaling, SSL, CI/CD integrado

**Azure SQL Database**
- Banco SQL Server gerenciado
- Backup automático, geo-replicação

**Storage Account**
- Blob Storage (equivalente ao S3)
- File Share (compartilhamento SMB na nuvem)

**Active Directory (Azure AD)**
- Gerenciamento de identidade na cloud
- SSO para aplicações SaaS

---

## 🎯 Módulo 4: Conceitos Fundamentais

### Regiões e Zonas de Disponibilidade

**Região**
- Localização geográfica (ex: US East, Brazil South)
- Cada região tem múltiplos data centers

**Zona de Disponibilidade (AZ)**
- Data centers isolados dentro de uma região
- Alta disponibilidade: Distribua recursos em múltiplas AZs

**Latência**
- Servidores nos EUA = ~200ms de latência do Brasil
- Servidores no Brasil (São Paulo) = ~15ms

### Auto-Scaling
**O que é:** Adicionar/remover servidores automaticamente conforme demanda.

**Exemplo:**
- 10h-18h (horário comercial): 5 servidores
- 18h-22h (baixa demanda): 2 servidores
- Economia: Paga menos quando não precisa

### Load Balancer
**Função:** Distribui tráfego entre múltiplos servidores.

**Vantagem:**
- Se um servidor cair, o outro assume
- Melhor performance (divide carga)

---

## 💰 Módulo 5: Precificação e Economia

### Modelos de Cobrança

**On-Demand**
- Pague por hora/segundo
- Sem compromisso
- Mais caro

**Reserved Instances (RI)**
- Compromisso de 1-3 anos
- Desconto de até 75%
- Para workloads previsíveis

**Spot Instances (AWS)**
- Leilão de capacidade ociosa
- Desconto de até 90%
- Pode ser interrompido a qualquer momento
- Para jobs que podem parar/recomeçar

### Free Tier (Camada Gratuita)

**AWS Free Tier:**
- 750h/mês de EC2 t2.micro (12 meses)
- 5GB de S3 (para sempre)
- 750h/mês de RDS (12 meses)

**Azure Free:**
- 750h/mês de VM B1S (12 meses)
- 5GB de Blob Storage (12 meses)
- $200 de crédito (30 dias)

---

## 🔐 Módulo 6: Segurança na Nuvem

### Shared Responsibility Model

**Provedor (AWS/Azure) é responsável por:**
- Segurança física dos data centers
- Hardware
- Rede física
- Infraestrutura de virtualização

**Você é responsável por:**
- Dados
- Configuração de firewall
- Criptografia
- Gerenciamento de usuários/acessos
- Patches do SO

### IAM (Identity and Access Management)

**Princípio do Menor Privilégio:**
Dê apenas as permissões ESSENCIAIS.

**Exemplo:**
- Dev de frontend: Acesso ao S3 (upload de imagens)
- Dev de backend: Acesso ao RDS (banco de dados)
- Ninguém tem acesso admin sem necessidade

**MFA (Multi-Factor Authentication)**
Sempre habilite MFA na conta root!

---

## 🛠️ Módulo 7: Casos de Uso Práticos

### 1. Hospedar Site Estático
**Serviço:** S3 + CloudFront (AWS) ou Storage + CDN (Azure)
**Custo:** ~$1-5/mês para site pequeno
**Vantagem:** Alta disponibilidade, performance global

### 2. Aplicação Web com Banco
**Arquitetura:**
- Load Balancer
- 2+ Servidores EC2/VMs (auto-scaling)
- RDS/SQL Database (gerenciado)
- S3/Blob para arquivos estáticos

### 3. Backup na Nuvem
**Cenário:** Empresa quer backup off-site seguro.
**Solução:** S3 Glacier (AWS) ou Archive Storage (Azure)
**Custo:** $0.004/GB/mês (muito barato)

### 4. Ambiente de Desenvolvimento/Teste
**Problema:** Montar lab é caro.
**Solução:** Ligar VMs apenas quando estudar/testar.
**Custo:** ~$20-50/mês vs $500+ de hardware

---

## 📖 Labs Práticos (Grátis!)

### Lab 1: Criar VM na AWS
1. Crie conta na AWS (free tier)
2. EC2 > Launch Instance
3. Escolha Ubuntu (free tier eligible)
4. Conecte via SSH
5. Instale NGINX: `sudo apt install nginx`
6. Acesse o IP público no navegador

### Lab 2: Hospedar Site Estático no S3
1. Crie bucket no S3
2. Upload de arquivo HTML
3. Habilite "Static Website Hosting"
4. Acesse a URL do bucket

### Lab 3: Criar Banco de Dados RDS
1. RDS > Create Database
2. Escolha PostgreSQL (free tier)
3. Configure usuário/senha
4. Anote o endpoint
5. Conecte com DBeaver/pgAdmin

---

## 🎓 Para a Faculdade

Na faculdade você pode ver:
- Arquiteturas distribuídas
- Computação paralela
- Sistemas de alto desempenho

**Vantagem que você terá:**
- Conhece cloud na prática
- Sabe provisionar infraestrutura
- Pode fazer projetos da faculdade na nuvem

---

## 📜 Certificações Cloud

**AWS:**
- AWS Certified Cloud Practitioner (entrada)
- AWS Certified Solutions Architect Associate (intermediário)

**Azure:**
- Azure Fundamentals (AZ-900)
- Azure Administrator (AZ-104)

**Google Cloud:**
- Cloud Engineer Associate

**Recomendação:** Comece com Cloud Practitioner (AWS) ou AZ-900 (Azure) = são básicas e baratas ($100).

---

## 📖 Recursos de Estudo

**Gratuitos:**
- AWS Free Tier (12 meses de uso grátis)
- Microsoft Learn (Azure fundamentals)
- A Cloud Guru (trial grátis)

**YouTube:**
- Curso AWS para Iniciantes (Fabricio Veronez)
- FreeCodeCamp AWS Certified Cloud Practitioner

---

**Veja também:**
- [Roadmap de Certificações](/guias/Guia_Roadmap_Certificacoes)
- [Windows Server](/guias/Curso_Windows_Server_AD) (migração pra cloud)
