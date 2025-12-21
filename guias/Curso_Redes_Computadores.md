# 🌐 Curso: Redes de Computadores

Domine os fundamentos de rede que você usa TODO DIA como técnico.

---

## 📚 Módulo 1: Fundamentos de Rede

### Modelo OSI (7 Camadas)
1. **Física** - Cabos, sinais elétricos
2. **Enlace** - MAC Address, Switch
3. **Rede** - IP, Roteamento
4. **Transporte** - TCP/UDP, Portas
5. **Sessão** - Conexões persistentes
6. **Apresentação** - Criptografia, Compressão
7. **Aplicação** - HTTP, FTP, DNS

**Na prática:** Problemas na camada 1 (cabo desconectado) ou camada 3 (IP errado) são os mais comuns.

### TCP/IP (Modelo de 4 Camadas)
- **Acesso à Rede** (Física + Enlace)
- **Internet** (IP)
- **Transporte** (TCP/UDP)
- **Aplicação** (HTTP, DNS, etc)

---

## 🔢 Módulo 2: Endereçamento IP

### IPv4 Básico
**Formato:** `192.168.1.100`

**Classes de IP:**
- **Classe A:** 10.0.0.0 a 10.255.255.255 (redes grandes)
- **Classe B:** 172.16.0.0 a 172.31.255.255 (redes médias)
- **Classe C:** 192.168.0.0 a 192.168.255.255 (redes pequenas/domésticas)

### Máscara de Sub-rede
`255.255.255.0` = `/24` (254 hosts disponíveis)
`255.255.0.0` = `/16` (65534 hosts)

**Cálculo rápido:**
- `/24` = 256 IPs totais (1 rede, 1 broadcast, 254 hosts)
- `/25` = 128 IPs
- `/26` = 64 IPs
- `/27` = 32 IPs

### Gateway Padrão
É o roteador que leva tráfego para fora da rede local.

**Exemplo prático:**
```
IP do PC: 192.168.1.50
Máscara: 255.255.255.0
Gateway: 192.168.1.1 (o roteador)
DNS: 8.8.8.8 (Google) ou 1.1.1.1 (Cloudflare)
```

---

## 🛠️ Módulo 3: Serviços Essenciais

### DNS (Domain Name System)
**O que faz:** Traduz nomes (google.com) para IPs (142.250.185.46)

**Comandos de diagnóstico:**
```bash
nslookup google.com        # Windows
dig google.com             # Linux
```

**Problema comum:** Cliente não acessa sites mas consegue pingar IPs = DNS com problema.

### DHCP (Dynamic Host Configuration Protocol)
**O que faz:** Distribui IPs automaticamente.

**Configuração típica:**
- Range: 192.168.1.100 a 192.168.1.200
- Gateway: 192.168.1.1
- DNS: 8.8.8.8
- Lease Time: 24 horas

**Problema comum:** "Sem acesso à internet" mas conectado ao Wi-Fi = DHCP não atribuiu IP ou deu IP inválido.

### NAT (Network Address Translation)
**O que faz:** Permite vários dispositivos compartilharem um IP público.

**Exemplo:**
- IP Público do roteador: 200.123.45.67
- IPs privados internos: 192.168.1.x
- Quando você acessa um site, o NAT traduz o IP privado para o público

---

## 🔌 Módulo 4: Hardware de Rede

### Switch
**Função:** Conecta dispositivos dentro da MESMA rede.
**Trabalha na camada:** 2 (Enlace - usa MAC Address)

### Roteador
**Função:** Conecta REDES DIFERENTES.
**Trabalha na camada:** 3 (Rede - usa IP)

### Access Point (AP)
**Função:** Fornece Wi-Fi.
Basicamente um switch sem fio.

### Firewall
**Função:** Controla tráfego (permite/bloqueia)
**Tipos:**
- Stateless: Regras simples (bloqueia porta X)
- Stateful: Analisa conexões completas

---

## 🔍 Módulo 5: Troubleshooting de Rede

### Comandos Essenciais (Windows)

**1. Verificar configuração de IP**
```cmd
ipconfig /all
```
Mostra: IP, máscara, gateway, DNS, MAC address

**2. Testar conectividade**
```cmd
ping 8.8.8.8          # Testa se há internet
ping 192.168.1.1      # Testa conexão com o roteador
ping google.com       # Testa DNS + Internet
```

**3. Rastrear rota de pacotes**
```cmd
tracert google.com
```
Mostra cada salto (hop) até o destino.

**4. Ver tabela de roteamento**
```cmd
route print
```

**5. Renovar IP (DHCP)**
```cmd
ipconfig /release      # Libera IP atual
ipconfig /renew        # Pede novo IP ao DHCP
```

**6. Limpar cache DNS**
```cmd
ipconfig /flushdns
```

**7. Ver portas abertas**
```cmd
netstat -ano
```

### Comandos Linux

```bash
ip a                   # Mostra interfaces e IPs
ip route               # Tabela de roteamento
ping -c 4 8.8.8.8     # 4 pacotes
traceroute google.com  # Rastreamento
ss -tunlp              # Portas abertas
systemctl status NetworkManager  # Status do gerenciador de rede
```

---

## 🎯 Cenários Práticos de Troubleshooting

### Cenário 1: "Não consigo acessar a internet"
1. `ping 8.8.8.8` → Funciona? 
   - ✅ Sim = Problema é DNS
   - ❌ Não = Continue

2. `ping 192.168.1.1` (gateway) → Funciona?
   - ✅ Sim = Problema no roteador/ISP
   - ❌ Não = Problema local

3. `ipconfig` → Tem IP válido (192.168.x.x)?
   - ✅ Sim = Verificar firewall
   - ❌ Não (169.254.x.x) = DHCP não funcionou

**Solução comum:** `ipconfig /release` + `ipconfig /renew`

### Cenário 2: "Internet lenta"
1. `ping 8.8.8.8` → Veja o tempo de resposta
   - < 50ms = Bom
   - 50-100ms = Aceitável
   - > 100ms = Problema de latência

2. `tracert google.com` → Identifique onde aumenta o delay
3. Teste com cabo (não Wi-Fi) → Se melhorar = problema no Wi-Fi
4. Use speedtest.net → Compare com velocidade contratada

### Cenário 3: "Consigo acessar IPs mas não sites"
**Problema:** DNS

**Solução:**
1. `ipconfig /flushdns`
2. Trocar DNS manualmente:
   - Google: 8.8.8.8 / 8.8.4.4
   - Cloudflare: 1.1.1.1 / 1.0.0.1

---

## 📡 Módulo 6: Wi-Fi e Wireless

### Padrões Wi-Fi
- **802.11n** - Até 300 Mbps (2.4 GHz e 5 GHz)
- **802.11ac (Wi-Fi 5)** - Até 1 Gbps (5 GHz)
- **802.11ax (Wi-Fi 6)** - Até 10 Gbps (2.4 e 5 GHz)

### Canais Wi-Fi (2.4 GHz)
**Canais sem interferência:** 1, 6, 11

**Problema comum:** Vários roteadores no mesmo canal = lentidão.

**Solução:** Use apps como "WiFi Analyzer" para ver canais menos congestionados e mude nas configurações do roteador.

### Segurança Wi-Fi
- **WEP:** NUNCA USE (quebrado)
- **WPA:** Vulnerável
- **WPA2:** Bom (mínimo aceitável)
- **WPA3:** Melhor (use se o roteador suportar)

---

## 🔐 Módulo 7: Portas e Protocolos

### Portas Mais Importantes
| Porta | Protocolo | Uso |
|-------|-----------|-----|
| 20/21 | FTP | Transferência de arquivos |
| 22 | SSH | Acesso remoto seguro (Linux) |
| 23 | Telnet | Acesso remoto INSEGURO |
| 25 | SMTP | Envio de email |
| 53 | DNS | Resolução de nomes |
| 80 | HTTP | Sites (não criptografado) |
| 443 | HTTPS | Sites (criptografado) |
| 3389 | RDP | Área de trabalho remota (Windows) |
| 3306 | MySQL | Banco de dados |
| 5432 | PostgreSQL | Banco de dados |

### TCP vs UDP
**TCP (Transmission Control Protocol)**
- Confiável (garante entrega)
- Mais lento
- Uso: HTTP, FTP, Email

**UDP (User Datagram Protocol)**
- Rápido
- Não garante entrega
- Uso: Streaming, VoIP, Games

---

## 📖 Exercícios Práticos

### Exercício 1: Configurar IP Estático
Configure um PC com:
- IP: 192.168.1.50
- Máscara: 255.255.255.0
- Gateway: 192.168.1.1
- DNS: 8.8.8.8

### Exercício 2: Diagnosticar Rede
1. Anote seu IP atual (`ipconfig`)
2. Ping no gateway
3. Ping no DNS (8.8.8.8)
4. Faça um `tracert` para um site

### Exercício 3: Encontrar Dispositivos na Rede
Use `arp -a` para listar todos os IPs conectados na sua rede local.

---

## 🎓 Para a Faculdade

Na faculdade você vai ver:
- Cálculo de sub-redes (CIDR)
- Algoritmos de roteamento (RIP, OSPF, BGP)
- Redes definidas por software (SDN)
- IPv6

**Dica:** Você já tem a BASE prática. A faculdade vai dar a teoria profunda. Combine os dois!

---

**Veja também:**
- [Troubleshooting Profissional](/guias/Guia_Troubleshooting_Profissional)
- [Galeria: Comandos de Suporte](/referencias/Galeria_Imagens)
