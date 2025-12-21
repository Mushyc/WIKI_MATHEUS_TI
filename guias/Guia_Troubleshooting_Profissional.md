# 🔍 Guia: Troubleshooting Profissional

Metodologia sistemática para diagnosticar QUALQUER problema técnico.

---

## 🎯 A Metodologia (5 Passos)

### 1️⃣ IDENTIFICAR o Problema
**Perguntas-chave:**
- O que EXATAMENTE não está funcionando?
- Quando começou?
- O que mudou recentemente?
- Consegue reproduzir o erro?

**Exemplo ruim:** "O computador está lento"
**Exemplo bom:** "O PC demora 5 minutos para abrir o Chrome desde ontem após instalação de um programa"

### 2️⃣ COLETAR Informações
**Logs e Evidências:**
- Event Viewer (Windows)
- Mensagens de erro (screenshot!)
- Configurações atuais do sistema

**Perguntas ao usuário:**
- Já tentou reiniciar?
- Mudou alguma configuração?
- Instalou algo novo?

### 3️⃣ FORMULAR Hipóteses
Liste possíveis causas em ordem de probabilidade:
1. Mais provável (comum)
2. Provável (menos comum)
3. Improvável (raro)

**Exemplo - PC lento:**
1. Disco cheio (90%+)
2. Muitos programas na inicialização
3. Malware
4. Hardware com defeito

### 4️⃣ TESTAR Hipóteses (uma por vez!)
**Regra de ouro:** Mude UMA coisa por vez!

Se mudar 3 coisas e funcionar, você não sabe qual resolveu.

**Teste a hipótese mais provável primeiro.**

### 5️⃣ DOCUMENTAR a Solução
Anote:
- Qual era o problema
- O que tentou
- O que funcionou
- Tempo gasto

**Por quê?** Quando aparecer problema similar, você já sabe resolver!

---

## 🛠️ Ferramentas de Diagnóstico

### Windows
- **Event Viewer** - `eventvwr.msc`
- **Task Manager** - Ctrl+Shift+Esc
- **Resource Monitor** - `resmon`
- **Device Manager** - `devmgmt.msc`
- **System Information** - `msinfo32`
- **Disk Cleanup** - `cleanmgr`
- **Check Disk** - `chkdsk C: /f /r`
- **SFC (System File Checker)** - `sfc /scannow`
- **DISM** - `DISM /Online /Cleanup-Image /RestoreHealth`

### Linux
- **dmesg** - Mensagens do kernel
- **journalctl** - Logs do systemd
- **top/htop** - Monitor de processos
- **df -h** - Espaço em disco
- **free -m** - Memória RAM
- **lsblk** - Listar discos
- **systemctl status** - Status de serviços

---

## 📋 Checklists por Categoria

### PC Não Liga
- [ ] Cabo de força conectado?
- [ ] Botão da fonte ligado (I/O)?
- [ ] Conexão do botão power na placa-mãe?
- [ ] Teste a fonte em outro dispositivo
- [ ] LEDs da placa-mãe acendem?
- [ ] Beeps ao ligar? (consulte manual)
- [ ] Teste sem placa de vídeo (use vídeo integrado)
- [ ] Remova RAM e recoloque (uma por vez)

### PC Lento
- [ ] Ver uso de CPU/RAM no Task Manager
- [ ] Disco cheio? (>90%)
- [ ] Muitos programas na inicialização? (`msconfig` > Inicialização)
- [ ] Antivírus fazendo scan?
- [ ] HDD ou SSD? (HDD é naturalmente mais lento)
- [ ] Temperatura alta? (use HWiNFO)
- [ ] Windows Update rodando em background?
- [ ] Malware? (scan com Malwarebytes)

### Sem Internet
- [ ] Outros dispositivos na mesma rede funcionam?
- [ ] LED do cabo de rede acende?
- [ ] Wi-Fi conectado mas sem internet?
- [ ] Ping no gateway funciona?
- [ ] Ping no DNS (8.8.8.8) funciona?
- [ ] IP é válido (192.168.x.x) ou APIPA (169.254.x.x)?
- [ ] Firewall bloqueando?
- [ ] Driver de rede instalado?
- [ ] Testar com cabo (não Wi-Fi)

### Tela Azul (BSOD)
- [ ] Anotou o código de erro?
- [ ] Acontece sempre na mesma situação?
- [ ] RAM com problema? (MemTest86)
- [ ] Driver desatualizado/corrompido?
- [ ] HD/SSD com setores ruins?
- [ ] Superaquecimento?
- [ ] Atualização recente do Windows?

---

## 🎓 Princípios do Troubleshooting de Elite

### 1. Divida e Conquiste
Isole o problema:
- Software vs Hardware?
- Rede vs Sistema local?
- Aplicação específica vs sistema todo?

### 2. Compare com Sistema Funcional
- Teste em outro PC que funciona
- Use Live USB do Linux para testar hardware
- Compare configurações de rede com PC funcionando

### 3. Substitua Componentes Sistematicamente
**Exemplo - Impressora não imprime:**
1. Troque o cabo USB
2. Teste em outra porta USB
3. Teste em outro PC
4. Reinstale o driver

### 4. Mantenha Baseline
Documente configurações quando ESTÁ FUNCIONANDO:
- IP, máscara, gateway, DNS
- Programas instalados
- Versão do SO

**Por quê?** Você pode voltar ao estado funcional.

### 5. Pense Probabilisticamente
O que é mais comum?
- Cabo solto > Placa-mãe queimada
- Driver desatualizado > CPU defeituoso
- Configuração errada > Vírus

Teste o mais provável primeiro!

---

## 🚨 Erros Comuns de Técnicos Iniciantes

### ❌ Erro 1: Mudar Várias Coisas de Uma Vez
**Problema:** Não sabe o que funcionou.
**Solução:** Mude UMA coisa, teste, documente.

### ❌ Erro 2: Não Fazer Backup
**Problema:** Perde dados do cliente.
**Solução:** SEMPRE faça backup antes de mexer.

### ❌ Erro 3: Não Perguntar o Suficiente
**Problema:** Assume sem confirmar.
**Solução:** Pergunte "O que mudou?" 3 vezes.

### ❌ Erro 4: Pular para Solução Sem Diagnóstico
**Problema:** Formata PC quando era só limpar temp.
**Solução:** Diagnostique PRIMEIRO, aja DEPOIS.

### ❌ Erro 5: Não Documentar
**Problema:** Esquece como resolveu.
**Solução:** Crie sua base de conhecimento (essa Wiki!)

---

## 📖 Casos Reais Resolvidos

### Caso 1: "PC reinicia sozinho"
**Diagnóstico:**
- Temperatura normal ✓
- Teste de RAM ok ✓
- Event Viewer: Erro "Kernel Power"

**Solução:** Fonte subdimensionada. Trocou de 400W para 600W = resolvido.

### Caso 2: "Wi-Fi conecta mas não navega"
**Diagnóstico:**
- Ping no gateway ok ✓
- Ping em 8.8.8.8 falha ✗

**Solução:** Problema no roteador (ISP). Cliente ligou para provedor.

### Caso 3: "Impressora imprime caracteres estranhos"
**Diagnóstico:**
- Driver instalado correto ✓
- Cabo USB testado em outro PC = mesmo problema ✗

**Solução:** Cabo USB defeituoso. Trocou cabo = resolvido.

---

## 🎯 Template de Atendimento

```
TICKET #___
Cliente: ___________
Data: __/__/____

PROBLEMA RELATADO:
___________________________

SINTOMAS OBSERVADOS:
___________________________

TESTES REALIZADOS:
[ ] _____________________
[ ] _____________________

HIPÓTESE:
___________________________

SOLUÇÃO APLICADA:
___________________________

RESULTADO:
[ ] Resolvido
[ ] Parcialmente resolvido
[ ] Não resolvido

OBSERVAÇÕES:
___________________________
```

---

**Veja também:**
- [Redes de Computadores](/guias/Curso_Redes_Computadores)
- [Montagem e Manutenção](/guias/Curso_Montagem_Manutencao_PC)
- [Ferramentas do Pen-drive](/guias/Curso_Ferramentas_Pendrive)
