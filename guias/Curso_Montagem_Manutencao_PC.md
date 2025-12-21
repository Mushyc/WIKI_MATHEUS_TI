# 🖥️ Curso: Montagem e Manutenção de Computadores

Tudo que você precisa saber para montar, manter e diagnosticar PCs profissionalmente.

---

## 🔩 Módulo 1: Componentes e Compatibilidade

### Processador (CPU)
**Principais marcas:** Intel (Core i3/i5/i7/i9), AMD (Ryzen 3/5/7/9)

**Compatibilidade crítica:**
- **Socket:** O processador DEVE ser compatível com o socket da placa-mãe
  - Intel: LGA 1700 (12ª-14ª gen), LGA 1200 (10ª-11ª gen)
  - AMD: AM5 (Ryzen 7000), AM4 (Ryzen 1000-5000)

**Aplicação de pasta térmica:**
1. Limpe o processador e cooler com álcool isopropílico
2. Aplique uma quantidade do tamanho de um grão de arroz no centro
3. Pressione o cooler (a pasta vai se espalhar sozinha)

### Placa-Mãe (Motherboard)
**Fatores de forma:**
- ATX: Tamanho completo (mais slots)
- Micro-ATX: Compacta
- Mini-ITX: Muito pequena

**Checklist de compatibilidade:**
- [ ] Socket compatível com CPU
- [ ] Chipset suporta funções desejadas
- [ ] RAM: DDR4 ou DDR5?
- [ ] Slots PCIe suficientes

### Memória RAM
**Tipos:** DDR4 (mais comum) ou DDR5 (mais nova)

**Dual Channel:**
- SEMPRE instale em pares (2x8GB é melhor que 1x16GB)
- Use slots A2 e B2 (consulte manual da placa)

**Frequências comuns:**
- DDR4: 2666MHz, 3200MHz, 3600MHz
- DDR5: 4800MHz, 5600MHz

### Armazenamento
**SSD NVMe (M.2):** Mais rápido (leitura 3500MB/s+)
**SSD SATA:** Rápido (leitura 550MB/s)
**HDD:** Lento, use apenas para backup/armazenamento

**Dica profissional:** Sempre instale o sistema operacional no SSD.

### Placa de Vídeo (GPU)
**Quando é necessária:**
- Games
- Edição de vídeo profissional
- Renderização 3D
- Mineração

**Processadores com vídeo integrado:**
- Intel: série G ou F (F = sem vídeo integrado)
- AMD: série G (com vídeo Vega)

### Fonte de Alimentação (PSU)
**Cálculo de potência:**
- PC básico: 400W
- PC gamer intermediário: 600-750W
- PC gamer high-end: 850W+

**Certificações (do pior ao melhor):**
80 Plus → Bronze → Silver → Gold → Platinum → Titanium

**⚠️ Regra de ouro:** NUNCA economize na fonte. Fonte ruim = PC queimado.

---

## 🔨 Módulo 2: Processo de Montagem

### Passo 1: Preparação
- [ ] Descarregue eletricidade estática (toque em metal aterrado)
- [ ] Organize componentes na mesa
- [ ] Tenha chaves phillips à mão

### Passo 2: Instalação na Placa-Mãe (fora do gabinete)
1. Instale o processador no socket (cuidado com os pinos!)
2. Aplique pasta térmica
3. Instale o cooler
4. Instale a RAM nos slots corretos (A2/B2)
5. Instale o SSD M.2 (se houver)

### Passo 3: Montagem no Gabinete
1. Instale os espaçadores (standoffs) no gabinete
2. Instale o shield de I/O da placa-mãe
3. Fixe a placa-mãe com parafusos
4. Instale a fonte de alimentação
5. Instale HDD/SSD SATA (se houver)
6. Instale placa de vídeo no slot PCIe x16

### Passo 4: Cabeamento
**Conexões da placa-mãe:**
- ATX 24 pinos (principal)
- EPS 8 pinos (CPU)
- Conectores do painel frontal (power, reset, LEDs)
- USB frontal
- Áudio frontal

**Conexões da placa de vídeo:**
- PCIe 6+2 pinos (se necessário)

**Gerenciamento de cabos:**
- Passe cabos por trás da bandeja da placa-mãe
- Use velcro ou abraçadeiras
- Melhora fluxo de ar e estética

---

## 🔧 Módulo 3: Primeiro Boot e Configuração

### BIOS/UEFI - Primeira Inicialização
**Acesso:** Pressione DEL ou F2 ao ligar

**Configurações essenciais:**
1. **Boot Order:** Coloque o pen-drive/SSD com sistema em primeiro
2. **XMP/DOCP:** Ative para RAM rodar na frequência correta
3. **Secure Boot:** Pode deixar ativado (Windows 11 exige)
4. **Virtualization (VT-x/AMD-V):** Ative se for usar VMs

### Instalação do Sistema Operacional
1. Insira pen-drive com Windows/Linux
2. Boot pelo pen-drive
3. Siga o instalador
4. **Particione o disco:**
   - Windows: Deixe o instalador criar automaticamente
   - Linux: 50GB para / (raiz), resto para /home

### Pós-Instalação
1. Instale drivers do chipset (site da placa-mãe)
2. Instale driver da GPU (NVIDIA/AMD)
3. Atualize o Windows/Linux
4. Instale programas essenciais

---

## 🛠️ Módulo 4: Manutenção Preventiva

### Limpeza Física (a cada 6 meses)
**Equipamentos:**
- Ar comprimido
- Pincel antiestático
- Álcool isopropílico
- Pano de microfibra

**Procedimento:**
1. Desligue o PC da tomada
2. Abra o gabinete
3. Use ar comprimado em:
   - Cooler da CPU
   - Placa de vídeo
   - Fonte
   - Filtros de ar
4. Limpe poeira acumulada com pincel
5. Reaplique pasta térmica se temperatura estiver alta

### Monitoramento de Temperatura
**Valores saudáveis:**
- CPU em idle: 30-45°C
- CPU em carga: 60-80°C
- GPU em idle: 30-50°C
- GPU em carga: 65-85°C

**⚠️ Alerta:** Acima de 90°C = PROBLEMA! Verifique cooler e pasta térmica.

### Atualização de BIOS
**Quando atualizar:**
- Problemas de estabilidade
- Suporte para nova CPU
- Correções de segurança

**Como fazer:**
1. Baixe a BIOS mais recente do site do fabricante
2. Coloque em pen-drive formatado em FAT32
3. Acesse a BIOS e use a função Q-Flash/EZ Flash
4. **NUNCA desligue o PC durante a atualização!**

---

## 🚨 Módulo 5: Troubleshooting

### PC não liga (LED da placa não acende)
1. Verifique cabo de força
2. Teste a fonte em outra tomada
3. Verifique botão físico da fonte (I/O)

### PC não liga (LED da placa acende, mas não dá vídeo)
1. **Beeps:** Ouça os bips (consulte manual)
2. Remova RAM e recoloque (teste stick por stick)
3. Remova placa de vídeo e teste vídeo integrado
4. Resete a BIOS (jumper CMOS ou retire bateria)

### PC liga mas reinicia sozinho
- Problema de superaquecimento (verifique cooler)
- Fonte subdimensionada
- RAM com defeito (teste com MemTest)

### Tela azul (BSOD - Blue Screen of Death)
**Códigos comuns:**
- `MEMORY_MANAGEMENT` → Problema de RAM
- `SYSTEM_SERVICE_EXCEPTION` → Driver corrompido
- `KERNEL_DATA_INPAGE_ERROR` → HD/SSD com problema

**Solução:**
1. Anote o código de erro
2. Pesquise no Google "Windows [código] solução"
3. Use o Event Viewer do Windows para logs detalhados

### PC lento após montagem
1. Verifique Task Manager → Veja se há processo consumindo tudo
2. Confirme que RAM está em Dual Channel (CPU-Z > Memory > Channels)
3. Ative XMP na BIOS para RAM rodar na velocidade correta
4. Instale sistema no SSD (não no HDD)

---

## 📋 Checklist do Técnico Professional

### Antes de Montar
- [ ] Confirmei compatibilidade de TODOS os componentes
- [ ] Calculei a potência necessária da fonte
- [ ] Tenho pasta térmica de qualidade

### Durante a Montagem
- [ ] Descarreguei eletricidade estática
- [ ] Instalei RAM nos slots corretos (Dual Channel)
- [ ] Apliquei pasta térmica corretamente
- [ ] Gerenciei os cabos de forma organizada
- [ ] Conectei TODOS os cabos da placa-mãe

### Após Montagem
- [ ] Testei primeiro boot na BIOS
- [ ] Ativei XMP para a RAM
- [ ] Instalei drivers do chipset e GPU
- [ ] Verifiquei temperaturas com HWiNFO64
- [ ] Rodei stress test (Prime95 ou AIDA64)

---

**Veja também:**
- [Curso de Ferramentas do Pen-drive](/guias/Curso_Ferramentas_Pendrive)
- [Galeria: Troubleshooting Windows](/referencias/Galeria_Imagens)
