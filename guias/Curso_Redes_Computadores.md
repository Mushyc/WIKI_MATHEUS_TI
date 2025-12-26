# 🌐 Redes de Computadores: Master Class Edition
![Banner Redes](/banner_redes.png)
> **Nível:** Iniciante ao Avançado | **Foco:** Infraestrutura e Segurança
---

## 📖 Introdução: O que é uma Rede?

Imagine uma rede de pesca ou uma teia de aranha. Cada nó é um dispositivo (computador, celular, impressora) e as linhas são a conexão (cabos ou Wi-Fi). O objetivo de uma rede é **compartilhar recursos** (arquivos, internet, impressoras). Sem redes, cada computador seria uma ilha isolada.

---

## 📂 Módulo 1: O Modelo OSI (O Mapa da Mina)

Para que computadores de marcas diferentes se entendam, existe uma regra universal: o **Modelo OSI**. Ele divide a comunicação em **7 camadas**.

### 📝 No seu Caderno (Anote isso!):
A forma mais fácil de decorar é a frase: **"A APresentação de SESSÃO de TRANSPORTE de REDE em ENLACE FÍSICO"**.

| **1** | Física | Sinais puros | Cabos, Placa de Wi-Fi, Pulsos Elétricos |

> [!TIP]
> **Visão Técnica Avançada:**
> ![Infográfico OSI e Ataques](/assets/academy/infografico_camadas_osi_ataques.jpg)
> *Este infográfico mostra como cada camada do modelo OSI pode sofrer ataques específicos e quais as defesas recomendadas.*

---

## ⚡ Módulo 2: TCP vs UDP (Segurança vs Velocidade)

No transporte de dados (Camada 4), existem dois protocolos principais:

1.  **TCP (Transmission Control Protocol):** É como uma carta registrada. Ele envia o dado, espera o destinatário confirmar que recebeu, e se o dado se perder no caminho, ele envia de novo. 
    *   *Uso:* E-mails, Sites, Transferência de arquivos.
2.  **UDP (User Datagram Protocol):** É como um canhão de confetes. Ele dispara os dados o mais rápido possível e não se importa se alguns caíram no chão.
    *   *Uso:* Chamadas de vídeo, Jogos online, Streaming (onde um pequeno "engasgo" é melhor que o vídeo travar esperando confirmação).

---

## 🔢 Módulo 3: Endereçamento IP e Máscaras

O IP é o seu **endereço digital**. Sem ele, a internet não sabe para onde mandar a resposta do site que você acessou.

### 3.1 IPv4 (O formato clássico)
Exemplo: `192.168.0.1`. São 4 números de 0 a 255.

### 3.2 A Máscara de Subrede (O muro da rede)
A máscara define **onde termina a sua rede e onde começa a internet**. 
- A máscara `/24` (255.255.255.0) é a mais comum. Ela diz que os primeiros 3 números são o "nome da rede" e o último é o "número do aparelho".

---

## ⚙️ Módulo 4: Protocolos que Fazem a Mágica

### 4.1 DHCP (O Garçom da Rede)
Sempre que você conecta no Wi-Fi, o seu celular recebe um IP automaticamente. Isso acontece graças ao processo **DORA**:
1.  **Discover:** Seu PC grita por um IP.
2.  **Offer:** O Roteador oferece um IP.
3.  **Request:** Seu PC pede para ficar com aquele IP.
4.  **Acknowledge:** O Roteador confirma e entrega o IP.

### 4.2 DNS (A Lista Telefônica)
Os computadores amam números (IPs), mas humanos amam nomes. O DNS traduz `google.com` para `142.250.217.110`. Sem o DNS, você teria que decorar o IP de todos os sites do mundo.

---

## 🧪 Módulo 5: Laboratório Profissional (Troubleshooting)

Se o Wi-Fi parou, você precisa saber diagnosticar. Use estes comandos no Terminal (CMD ou PowerShell):

4.  `tracert google.com`: Mostra todos os roteadores pelos quais seu pacote passa até chegar no Google.

### 🔌 Extra: Padronização de Cabos (Cat6/Cat6a)
![Cores de Cabos RJ45](/assets/academy/infografico_cores_cabo_rede.jpg)

### 📋 Guia de Referência Rápida (Cheat Sheet)
![Cheat Sheet Redes](/assets/academy/infografico_cheatsheet_redes_br.jpg)

---

## 📝 Exercícios de Fixação (Para responder no caderno!)

1.  Qual a diferença fundamental entre um **Switch** (Camada 2) e um **Roteador** (Camada 3)?
2.  Se você estiver assistindo uma Live e o vídeo começar a falhar mas não parar, qual protocolo está sendo usado (TCP ou UDP)? Por quê?
3.  O que significa a sigla **DNS** e qual sua função principal?
4.  No processo **DORA** do DHCP, o que acontece na fase "Discover"?
5.  Qual comando você usaria para descobrir o seu endereço físico (**MAC Address**)?
6.  Calcule: Em uma rede `/24`, quantos hosts (aparelhos) usáveis podemos ter?
7.  Para que serve o comando `tracert`?
8.  Explique a Camada 1 do Modelo OSI com suas próprias palavras.
9.  O que acontece se dois aparelhos tiverem o mesmo IP na mesma rede?
10. **Desafio:** Se o comando `ping 8.8.8.8` funciona, mas o seu navegador não abre nenhum site, qual é o provável culpado (DNS ou Roteador)?

---

### 🚀 Próximos Passos
- [🐧 Domínio Linux](/guias/Curso_Dominio_Linux) - Aprenda a configurar redes no terminal Linux.
- [💀 Kali Linux Expert](/guias/Curso_Pratico_Kali_Expert) - Aprenda como proteger (e atacar) essas redes.
