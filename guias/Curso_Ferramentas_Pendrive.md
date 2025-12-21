# 🛠️ Curso: Kit de Ferramentas do Técnico (Pen-drive)

Aprenda a usar profissionalmente cada ferramenta do seu pen-drive organizado.

---

## 📂 Categoria 01: Sistemas e ISOs

### Ventoy (Gerenciador de Boot)
**O que é:** Transforma seu pen-drive em multi-boot (várias ISOs).

**Como usar:**
1. Execute `Ventoy2Disk.exe`
2. Selecione seu pen-drive
3. Clique em "Install"
4. Copie as ISOs para a raiz do pen-drive

**Casos de uso:**
- Instalar Windows/Linux sem gravar ISO toda vez
- Testar múltiplos sistemas do mesmo pen-drive

---

## 🖥️ Categoria 02: Ferramentas de Boot

### Rufus
**O que é:** Cria pen-drives bootáveis com uma ISO.

**Passo a passo:**
1. Abra o Rufus
2. Selecione a ISO do Windows/Linux
3. Escolha o esquema de partição (GPT para UEFI, MBR para BIOS)
4. Clique em "Iniciar"

### WinToHDD
**O que é:** Instala Windows direto do HD sem pen-drive.

**Quando usar:**
- Reinstalar Windows sem mídia bootável
- Migrar sistema para outro disco

---

## 🔍 Categoria 03: Diagnóstico de Hardware

### CrystalDiskInfo
**O que é:** Monitora a saúde do HD/SSD.

**Como interpretar:**
- **Bom (Azul):** Disco está saudável
- **Atenção (Amarelo):** Problemas detectados
- **Ruim (Vermelho):** Substitua imediatamente

**Valores críticos:**
- Reallocated Sectors > 0 = Disk com setores ruins
- Temperature > 50°C = Superaquecimento

### HWiNFO64
**O que é:** Diagnóstico completo de hardware.

**Principais usos:**
- Ver temperatura de CPU/GPU em tempo real
- Identificar modelo exato de componentes
- Detectar throttling (superaquecimento)

### CPU-Z e GPU-Z
**O que fazem:** Mostram informações detalhadas de CPU e placa de vídeo.

**Cenário prático:**
Cliente pergunta se o PC aguenta um jogo → use o CPU-Z/GPU-Z para identificar o hardware e pesquisar os requisitos.

### MemTest64
**O que é:** Testa memória RAM por erros.

**Como usar:**
1. Execute o MemTest64.exe
2. Deixe rodando por no mínimo 1 hora
3. Se aparecer erro vermelho = RAM com defeito

---

## 🔧 Categoria 04: Manutenção de Sistema

### Dism++ 
**O que é:** Ferramenta avançada de limpeza e otimização do Windows.

**Funções principais:**
- Limpar arquivos temporários
- Remover atualizações antigas do Windows
- Reparar imagem do sistema (`DISM /Online /Cleanup-Image`)

### SDI (Snappy Driver Installer)
**O que é:** Instala drivers offline.

**Quando usar:**
- PC sem internet após formatação
- Drivers de chipset/rede não reconhecidos

**Como usar:**
1. Execute SDI.exe
2. Deixe ele detectar hardware
3. Marque os drivers necessários
4. Clique em "Install"

### Revo Uninstaller
**O que é:** Desinstala programas completamente (remove resíduos).

**Diferença do padrão:**
- Remove entradas do registro
- Apaga arquivos residuais
- Detecta sobras de instalações antigas

---

## 💾 Categoria 05: Recuperação de Dados

### MiniTool Power Data Recovery
**O que é:** Recupera arquivos deletados ou de discos formatados.

**Casos de uso:**
- Cliente deletou arquivo importante acidentalmente
- HD formatado por engano
- Partição corrompida

**Como usar:**
1. Selecione o tipo de recuperação (Deleted, Formatted, etc)
2. Escolha o disco
3. Faça um scan completo
4. Salve os arquivos recuperados em OUTRO DISCO

**⚠️ Importante:** NUNCA salve arquivos recuperados no mesmo disco que está recuperando!

---

## 🎯 Workflow de Atendimento

### Cenário 1: PC Lento
1. Rode o **CrystalDiskInfo** → Veja se o HD está com problemas
2. Abra **HWiNFO64** → Verifique temperatura e throttling
3. Use **Dism++** → Limpe arquivos temporários

### Cenário 2: Formatação Completa
1. Use **Ventoy/Rufus** → Crie mídia de instalação
2. Instale o sistema
3. Execute **SDI** → Instale todos os drivers

### Cenário 3: Dados Perdidos
1. **NÃO ESCREVA NADA NO DISCO**
2. Use **MiniTool Power Data Recovery**
3. Salve em pen-drive ou HD externo

---

## 📋 Checklist do Técnico Profissional

Sempre no seu atendimento:
- [ ] Faça backup dos dados do cliente ANTES de mexer
- [ ] Anote o problema original
- [ ] Use CrystalDiskInfo para verificar saúde do disco
- [ ] Documente o que foi feito
- [ ] Teste tudo antes de devolver

---

Veja também: [Curso de Manutenção de Computadores](/guias/Curso_Montagem_Manutencao_PC) para complementar seu conhecimento.
