# 📶 Capítulo 4: Guerra Wireless (Wi-Fi Cracking)

O ar está cheio de dados, e a maioria deles está mal protegida. Neste capítulo, aprenderemos como auditar redes sem fio, quebrar senhas WPA2 e entender por que "senha forte" não é a única coisa que importa em uma rede Wi-Fi.

---

## 📡 4.1 Colocando a Placa em Modo Monitor

Por padrão, sua placa Wi-Fi só "ouve" o que é para ela. Para hackear, precisamos que ela ouça **tudo**.

```bash
sudo airmon-ng start wlan0
```
*Dica: Use `iwconfig` para confirmar se o nome da interface mudou para `wlan0mon`.*

---

## 🕸️ 4.2 O Ataque de Handshake (WPA2)

Para quebrar a senha de uma rede WPA2, precisamos capturar o momento em que um dispositivo se conecta ao roteador. Esse momento é o **Handshake**.

### 4.2.1 Passo a Passo Profissional:
1. **Localizar o alvo:** `sudo airodump-ng wlan0mon` (Anote o BSSID e o Canal).
2. **Focar no alvo:** `sudo airodump-ng -c [canal] --bssid [BSSID] -w captura wlan0mon`.
3. **Forçar o Handshake (Deauth):** Em outro terminal, chute um usuário da rede:
   ```bash
   sudo aireplay-ng -0 5 -a [BSSID] wlan0mon
   ```
4. **Captura completa:** Quando aparecer `WPA Handshake` no topo da tela, você tem a senha criptografada no seu arquivo `captura-01.cap`.

---

## 🔨 4.3 Brute-force: Quebrando a Criptografia

Agora que temos o "cadeado trancado", precisamos encontrar a chave. Usaremos o **Aircrack-ng** com uma wordlist (lista de senhas).

```bash
aircrack-ng -w /usr/share/wordlists/rockyou.txt captura-01.cap
```
*Nota: Se a senha for "12345678" ou "data de nascimento", o Rockyou vai achar em segundos.*

---

## 😈 4.4 Evil Twin: O Gêmeo Malvado

E se você criasse uma rede Wi-Fi idêntica à do shopping ou da empresa, mas sem senha? O dispositivo do usuário se conecta a você automaticamente, e você captura **todo o tráfego** dele.

::: danger ⚠️ O Perigo Perto de Você
Ataques de "Evil Twin" são os mais perigosos porque não dependem de falha técnica no roteador, mas sim da confiança do usuário. Nunca se conecte a redes Wi-Fi abertas desconhecidas.
:::

---

## 🧪 Desafio do Mestre: Auditoria do seu Próprio Wi-Fi
1. Coloque sua placa em modo monitor.
2. Capture o Handshake da sua própria rede residencial.
3. Tente quebrar a senha usando a wordlist `rockyou.txt`.
4. **Resultado:** Se a senha foi encontrada rápido, você precisa mudar sua senha para algo mais complexo IMEDIATAMENTE.

---

> [!TIP]
> **O Próximo Salto:** Agora que você domina as redes locais, vamos para o alvo mais lucrativo e comum: **Web Hacking** (Capítulo 5). Aprenda a quebrar sites e aplicações.
