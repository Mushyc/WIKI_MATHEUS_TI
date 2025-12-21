# 🏢 Curso: Windows Server & Active Directory

Domine a administração de redes corporativas Windows.

---

## 📚 Módulo 1: Fundamentos do Windows Server

### Diferenças: Windows Client vs Server
| Recurso | Windows 10/11 | Windows Server |
|---------|--------------|----------------|
| Máximo de usuários simultâneos | 20 | Ilimitado |
| Active Directory | Não | ✅ Sim |
| DHCP/DNS Server | Limitado | ✅ Completo |
| Hyper-V | Básico | ✅ Avançado |
| Licenciamento | Por dispositivo | Por núcleo/CAL |

### Versões do Windows Server
- **Standard**: Até 2 VMs
- **Datacenter**: VMs ilimitadas
- **Essentials**: Pequenas empresas (<25 usuários)

---

## 🌳 Módulo 2: Active Directory (AD)

### O que é Active Directory?
**Definição:** Banco de dados centralizado que gerencia:
- Usuários
- Computadores
- Grupos
- Políticas de segurança

**Vantagem:** Login único (SSO) = um usuário, várias máquinas.

### Componentes Principais

**Domain Controller (DC)**
- Servidor que hospeda o AD
- Armazena banco de dados de usuários
- Autentica logins

**Domain**
- Domínio (ex: `empresa.local`)
- Agrupa usuários e máquinas

**Organizational Unit (OU)**
- Pasta lógica para organizar objetos
- Exemplo: OU "TI", OU "Vendas", OU "RH"

**Group Policy (GPO)**
- Políticas aplicadas a usuários/computadores
- Exemplo: Bloquear pen-drive, definir senha forte

---

## 👤 Módulo 3: Gerenciamento de Usuários

### Criar Usuário no AD
```powershell
New-ADUser -Name "João Silva" `
           -GivenName "João" `
           -Surname "Silva" `
           -SamAccountName "joao.silva" `
           -UserPrincipalName "joao.silva@empresa.local" `
           -Path "OU=Vendas,DC=empresa,DC=local" `
           -AccountPassword (ConvertTo-SecureString "Senha@123" -AsPlainText -Force) `
           -Enabled $true
```

### Resetar Senha de Usuário
```powershell
Set-ADAccountPassword -Identity joao.silva -NewPassword (ConvertTo-SecureString "NovaSenha@123" -AsPlainText -Force)
Set-ADUser -Identity joao.silva -ChangePasswordAtLogon $true
```

### Desativar/Ativar Usuário
```powershell
Disable-ADAccount -Identity joao.silva  # Desativar
Enable-ADAccount -Identity joao.silva   # Ativar
```

### Listar Usuários de Uma OU
```powershell
Get-ADUser -Filter * -SearchBase "OU=Vendas,DC=empresa,DC=local" | Select Name, SamAccountName
```

---

## 👥 Módulo 4: Grupos e Permissões

### Tipos de Grupos

**Security Groups**
- Controle de acesso a recursos
- Exemplo: Grupo "TI" tem acesso à pasta "Suporte"

**Distribution Groups**
- Lista de distribuição de email
- Sem controle de acesso

### Escopos de Grupo
- **Domain Local**: Acesso dentro do domínio
- **Global**: Membros do domínio, acesso em toda floresta
- **Universal**: Qualquer domínio da floresta

### Criar Grupo
```powershell
New-ADGroup -Name "Equipe_Vendas" `
            -GroupScope Global `
            -GroupCategory Security `
            -Path "OU=Grupos,DC=empresa,DC=local"
```

### Adicionar Usuário a Grupo
```powershell
Add-ADGroupMember -Identity "Equipe_Vendas" -Members joao.silva, maria.souza
```

### Ver Membros de um Grupo
```powershell
Get-ADGroupMember -Identity "Equipe_Vendas" | Select Name
```

---

## 📜 Módulo 5: Group Policy (GPO)

### O que são GPOs?
Políticas que configuram automaticamente:
- Segurança (senhas complexas obrigatórias)
- Desktop (papel de parede corporativo)
- Aplicações (instalar software automaticamente)
- Bloqueios (desabilitar painel de controle)

### Exemplos Práticos

**Política de Senha Forte**
1. Abra `gpmc.msc` (Group Policy Management)
2. Crie GPO "Politica_Senhas"
3. Computer Configuration > Policies > Windows Settings > Security Settings > Account Policies > Password Policy
4. Configure:
   - Comprimento mínimo: 8 caracteres
   - Complexidade: Habilitada
   - Idade máxima: 90 dias

**Mapear Drive de Rede Automaticamente**
1. User Configuration > Preferences > Windows Settings > Drive Maps
2. Novo > Mapped Drive
3. Location: `\\servidor\compartilhamento`
4. Drive Letter: `P:`

**Bloquear USB (Pen-drives)**
1. Computer Configuration > Policies > Administrative Templates > System > Removable Storage Access
2. Habilite "All Removable Storage: Deny all access"

### Aplicar GPO
```powershell
gpupdate /force  # Força atualização de políticas no PC
```

---

## 🌐 Módulo 6: DHCP e DNS no Server

### DHCP Server
**O que faz:** Distribui IPs automaticamente.

**Configuração típica:**
```
Scope: 192.168.1.100 - 192.168.1.200
Gateway: 192.168.1.1
DNS: 192.168.1.10 (IP do domain controller)
Lease: 8 dias
```

**Reservar IP para Impressora:**
1. DHCP Console > Scope > Reservations
2. Add Reservation
3. MAC Address da impressora
4. IP fixo: 192.168.1.50

### DNS Server
**Função:** Resolve nomes internos.

**Exemplo:**
- Servidor: `SRV-FILES.empresa.local` → 192.168.1.20
- Impressora: `IMP-RH.empresa.local` → 192.168.1.50

**Criar registro DNS:**
```powershell
Add-DnsServerResourceRecordA -Name "servidor-web" -ZoneName "empresa.local" -IPv4Address "192.168.1.100"
```

---

## 📁 Módulo 7: Compartilhamento de Arquivos

### Criar Pasta Compartilhada
```powershell
New-Item -Path "C:\Compartilhamentos\Vendas" -ItemType Directory
New-SmbShare -Name "Vendas" -Path "C:\Compartilhamentos\Vendas" -FullAccess "EMPRESA\Equipe_Vendas"
```

### Permissões NTFS
```powershell
$acl = Get-Acl "C:\Compartilhamentos\Vendas"
$permission = "EMPRESA\Equipe_Vendas","Modify","Allow"
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule $permission
$acl.SetAccessRule($rule)
Set-Acl "C:\Compartilhamentos\Vendas" $acl
```

### Mapear no Cliente
```
\\servidor\Vendas
```

---

## 🔐 Módulo 8: Segurança Corporativa

### Política de Bloqueio de Conta
Configurar via GPO:
- Tentativas de login inválidas: 5
- Duração do bloqueio: 30 minutos
- Resetar contador após: 15 minutos

### Auditoria de Eventos
Habilitar audit de:
- Tentativas de login fracassadas
- Modificações em grupos
- Acessos a pastas confidenciais

**Ver log:**
```powershell
Get-EventLog -LogName Security -Newest 100 | Where-Object {$_.EventID -eq 4625}  # Logins falhados
```

---

## 🎓 Para a Faculdade

Na faculdade você vai ver:
- Arquitetura de domínios (Trust relationships)
- Replicação de Domain Controllers
- Backup e Disaster Recovery

**Vantagem que você terá:**
- Sabe administrar AD na prática
- Só precisa entender a teoria de replicação e infraestrutura

---

## 📖 Recursos de Estudo

**Gratuitos:**
- Microsoft Learn (módulos de Windows Server)
- Windows Server Administration Fundamentals (Virtual Academy)

**Certificação:**
- MCSA: Windows Server (descontinuado mas material válido)
- Microsoft 365 Certified: Modern Desktop Administrator

---

**Veja também:**
- [Redes de Computadores](/guias/Curso_Redes_Computadores)
- [Roadmap de Certificações](/guias/Guia_Roadmap_Certificacoes)
