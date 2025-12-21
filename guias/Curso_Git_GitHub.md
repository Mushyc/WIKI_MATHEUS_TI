# 🔀 Curso: Git e GitHub Profissional

Controle de versão que TODO desenvolvedor PRECISA dominar.

---

## 🎯 Por Que Git é Obrigatório?

- ✅ 99% das empresas usam
- ✅ Obrigatório para trabalho em equipe
- ✅ Portfólio público (GitHub)
- ✅ Salva seu código de desastres

---

## 📚 Módulo 1: Fundamentos

### Instalação
```bash
# Windows
winget install Git.Git

# Linux
sudo apt install git

# Configuração inicial
git config --global user.name "Seu Nome"
git config --global user.email "seuemail@gmail.com"
```

### Comandos Essenciais
```bash
# Iniciar repositório
git init

# Ver status
git status

# Adicionar arquivos
git add arquivo.txt        # Um arquivo
git add .                  # Todos os arquivos

# Commit (salvar)
git commit -m "Mensagem descritiva"

# Ver histórico
git log
git log --oneline  # Resumido
```

---

## 🌿 Módulo 2: Branches

### O Que São?
Linhas paralelas de desenvolvimento.

```bash
# Criar branch
git branch feature-login

# Mudar para branch
git checkout feature-login
# OU (comando novo)
git switch feature-login

# Criar E mudar
git checkout -b feature-cadastro

# Listar branches
git branch

# Deletar branch
git branch -d feature-login
```

### Workflow Padrão
```
main (produção)
  └── develop (desenvolvimento)
        ├── feature-login
        └── feature-cadastro
```

---

## 🔄 Módulo 3: Merge e Rebase

### Merge (Juntar branches)
```bash
git checkout main
git merge feature-login
```

### Resolver Conflitos
```bash
# 1. Git avisa do conflito
# 2. Abra arquivo conflitante:
<<<<<<< HEAD
código da branch atual
=======
código da outra branch
>>>>>>> feature-login

# 3. Edite manualmente
# 4. Adicione e commite
git add arquivo.txt
git commit -m "Resolvido conflito"
```

---

## ☁️ Módulo 4: GitHub

### Conectar Repositório Local ao GitHub
```bash
# Adicionar remoto
git remote add origin https://github.com/usuario/repo.git

# Enviar código
git push -u origin main

# Baixar alterações
git pull origin main
```

### Clone
```bash
git clone https://github.com/usuario/repo.git
```

---

## 🎯 Módulo 5: Workflow Profissional

### GitFlow
```bash
# Branches principais
main          # Produção
develop       # Desenvolvimento

# Branches temporárias
feature/nome  # Nova funcionalidade
hotfix/nome   # Correção urgente
release/v1.0  # Preparação de release
```

### Commits Semânticos
```bash
git commit -m "feat: adiciona login com Google"
git commit -m "fix: corrige bug no cadastro"
git commit -m "docs: atualiza README"
git commit -m "refactor: melhora estrutura do código"
git commit -m "test: adiciona testes unitários"
```

---

## 🔧 Comandos Avançados

```bash
# Desfazer último commit (mantém alterações)
git reset --soft HEAD~1

# Desfazer último commit (descarta alterações)
git reset --hard HEAD~1

# Ver diferenças
git diff

# Salvar trabalho temporariamente
git stash
git stash pop  # Restaurar

# Reescrever histórico
git rebase -i HEAD~3
```

---

## 🎓 Boas Práticas

1. **Commits pequenos e frequentes**
2. **Mensagens descritivas**
3. **Nunca commitar senhas/chaves**
4. **Use .gitignore**
5. **Pull antes de Push**

---

### Exemplo .gitignore
```
# Python
__pycache__/
*.py[cod]
venv/

# Node
node_modules/
.env

# IDEs
.vscode/
.idea/
```

---

**Veja também:**
- [Desenvolvimento Web](/guias/Guia_Desenvolvimento_Web)
- [Python para Automação](/guias/Curso_Python_Automacao)
