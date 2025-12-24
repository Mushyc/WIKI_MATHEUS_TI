# 🖥️ Montagem e Manutenção de PCs: Master Class Edition

![Banner Hardware](/banner_infra_hardware.png)

Domine o hardware. Da escolha cirúrgica dos componentes ao diagnóstico de falhas físicas complexas, este guia transforma você em um mestre da infraestrutura física. No mundo da TI, o software roda sobre o hardware; se a base falha, tudo cai.

---

## 📂 Módulo 1: Anatomia Avançada do PC

### 1.1 O Cérebro: CPU (Processador)
- **Cores vs Threads:** Mais cores = multitarefa. Mais clock = velocidade em jogos/apps únicos.
- **TDP (Thermal Design Power):** Indica quanto calor o processador gera. Essencial para escolher o cooler correto.
- **Bottleneck (Gargalo):** Quando sua placa de vídeo é muito potente para o seu processador (ou vice-versa), gerando travamentos.

### 1.2 A Espinha Dorsal: Placa-Mãe (Motherboard)
- **Chipsets:** 
    - **Série H/A:** Básicos (Escritório).
    - **Série B:** Custo-benefício (Suporta XMP/Overclock moderado).
    - **Série Z/X:** Alta performance (Entusiastas).
- **VRM:** Os componentes que alimentam o processador. VRMs ruins fazem o PC desligar sob carga pesada.

---

## ⚙️ Módulo 2: Memória e Armazenamento (Velocidade Pura)

### 2.1 RAM: O Poder do Canal Duplo
Sempre use pentes de memória em pares (ex: 2x 8GB em vez de 1x 16GB). Isso dobra a largura de banda de comunicação com o processador, aumentando a performance em até 20%.
- **XMP / DOCP:** Perfil de alta velocidade que deve ser ativado na BIOS, caso contrário sua RAM de 3200MHz rodará a 2133MHz.

### 2.2 SSD: A Revolução da Velocidade
| Tipo | Tecnologia | Velocidade Máxima | Uso Ideal |
| :--- | :--- | :--- | :--- |
| **HD SATA** | Disco Mecânico | 150 MB/s | Backup e Arquivos Mortos |
| **SSD SATA** | Flash 2.5" | 550 MB/s | PC de Escritório / Upgrade de PC Velho |
| **NVMe Gen 3**| M.2 PCIe 3.0 | 3.500 MB/s | Gaming e Uso Geral Profissional |
| **NVMe Gen 4**| M.2 PCIe 4.0 | 7.500 MB/s | Edição de Vídeo 4K e Workstations |

---

## 🔬 Módulo 3: Diagnóstico de Elite (POST & Beep Codes)

Quando o PC não liga, ele tenta te dizer o porquê através de sinais sonoros ou luzes (Debug LEDs).

### 3.1 Tabela de Beeps (Padrão AMI BIOS)
| Sinal | Diagnóstico Provável | O que fazer? |
| :--- | :--- | :--- |
| **1 Bip Curto** | Sistema OK | Nada, o PC vai ligar. |
| **3 Bips Curtos**| Falha na Memória RAM | Limpar contatos com borracha branca. |
| **1 Longo, 2 Curtos**| Falha na Placa de Vídeo | Reencaixar a GPU ou limpar contatos. |
| **Bips Contínuos**| Falha na Fonte/Energia | Testar tensões ou trocar a fonte. |

---

## 🌡️ Módulo 4: Refrigeração e Gestão Térmica

### 4.1 Pressão de Ar no Gabinete
- **Pressão Positiva:** Mais ar entrando do que saindo. (Evita poeira, mas pode acumular calor).
- **Pressão Negativa:** Mais ar saindo do que entrando. (Esfria rápido, mas suja o PC muito mais).
- **Ideal:** Equilíbrio. Ar frio entra pela frente/baixo, ar quente sai por trás/cima.

::: tip 💡 Dica de Mestre: Pasta Térmica
Não faça um "X" exagerado. Uma gota do tamanho de uma ervilha no centro é suficiente. O excesso de pasta térmica pode vazar e, em pastas condutivas, causar curto-circuito.
:::

---

## 🛡️ Módulo 5: Troubleshooting Professional

::: info 🛡️ Na Trincheira: Caso Real
Um PC de R$ 10.000 desligava em jogos pesados. O dono trocou a placa de vídeo e continuou o erro. Usei um multímetro e vi que a linha de 12V da fonte caía para 11.2V sob carga. **Diagnóstico:** Fonte de carga nominal alta, mas de má qualidade técnica. **Solução:** Troca por uma fonte com selo 80 Plus Gold. Problema resolvido.
:::

---

### Links de Referência Master
- [🏢 Windows Server & AD](/guias/Curso_Windows_Server_AD) - Servidores físicos.
- [🐧 Domínio do Linux](/guias/Curso_Dominio_Linux) - Drivers de hardware no Linux.
- [🔍 Troubleshooting Profissional](/guias/Guia_Troubleshooting_Profissional) - Metodologia de diagnóstico.
- [🛠️ Ferramentas Pen-drive](/guias/Curso_Ferramentas_Pendrive) - Softwares de teste de hardware.
