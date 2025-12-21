# 🐧 Curso: Domínio do Linux

Este curso ensina os fundamentos e técnicas avançadas para você dominar sistemas Linux no trabalho.

---

## 📚 Módulo 1: Comandos Essenciais

### Navegação e Arquivos
```bash
pwd               # Mostra o diretório atual
ls -lha           # Lista arquivos detalhados (incluindo ocultos)
cd /caminho       # Muda de diretório
mkdir pasta       # Cria diretório
rm -rf pasta      # Remove diretório e conteúdo
cp origem destino # Copia arquivo
mv origem destino # Move/renomeia arquivo
```

### Gerenciamento de Processos
```bash
ps aux            # Lista todos os processos
top               # Monitor em tempo real
htop              # Monitor interativo (precisa instalar)
kill -9 PID       # Força encerramento de processo
killall nome      # Mata processo por nome
```

### Permissões e Propriedade
```bash
chmod 755 arquivo # Altera permissões (rwxr-xr-x)
chown user:group arquivo # Altera dono
ls -l             # Mostra permissões atuais
```

---

## 🔧 Módulo 2: Administração de Sistema

### Gerenciamento de Pacotes (Debian/Ubuntu)
```bash
sudo apt update           # Atualiza lista de pacotes
sudo apt upgrade          # Atualiza pacotes instalados
sudo apt install pacote   # Instala novo pacote
sudo apt remove pacote    # Remove pacote
sudo apt autoremove       # Remove dependências não utilizadas
```

### Serviços e Systemd
```bash
systemctl status nome     # Verifica status do serviço
systemctl start nome      # Inicia serviço
systemctl stop nome       # Para serviço
systemctl enable nome     # Habilita no boot
systemctl restart nome    # Reinicia serviço
```

### Rede e Conectividade
```bash
ip a                      # Mostra interfaces de rede
ping 8.8.8.8             # Testa conectividade
netstat -tunlp           # Mostra portas abertas
ss -tunlp                # Versão moderna do netstat
curl ifconfig.me         # Mostra IP público
```

---

## 💻 Módulo 3: Troubleshooting Avançado

### Análise de Logs
```bash
journalctl -xe           # Logs do sistema (últimos)
tail -f /var/log/syslog  # Monitora log em tempo real
grep "erro" /var/log/*   # Busca erros nos logs
dmesg | tail             # Mensagens do kernel
```

### Uso de Recursos
```bash
df -h                    # Espaço em disco
du -sh /caminho          # Tamanho de diretório
free -m                  # Memória RAM disponível
uptime                   # Tempo ligado e carga
```

### SSH e Acesso Remoto
```bash
ssh user@servidor        # Conecta remotamente
scp arquivo user@host:/destino # Transfere arquivo
ssh-keygen               # Gera chave SSH
ssh-copy-id user@host    # Copia chave pública
```

---

## 🎯 Exercícios Práticos

### Prática 1: Criar Script de Backup
Crie um script que faz backup da pasta home para `/backup`:
```bash
#!/bin/bash
tar -czf /backup/home-$(date +%Y%m%d).tar.gz /home/usuario
```

### Prática 2: Monitorar Disco Cheio
Configure alerta quando disco atingir 80%:
```bash
df -h | grep -E '8[0-9]%|9[0-9]%|100%' && echo "Disco cheio!"
```

### Prática 3: Automatizar com Cron
Agende um script para rodar todo dia às 3h da manhã:
```bash
crontab -e
# Adicione: 0 3 * * * /caminho/script.sh
```

---

## 📖 Referências Visuais
Consulte também a [Galeria de Imagens](/referencias/Galeria_Imagens) para ver:
- Comandos Básicos Linux (Cheat Sheet Visual)
- Comandos Avançados Linux (Administração)
