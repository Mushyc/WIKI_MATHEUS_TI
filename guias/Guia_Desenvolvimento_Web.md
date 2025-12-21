# 💻 Guia: Desenvolvimento Web - Do Zero ao Profissional

Roadmap completo para se tornar desenvolvedor Full Stack.

---

## 🎨 Frontend Development

### Fundamentos (Nível Iniciante)
**HTML5**
- Estrutura semântica (`<header>`, `<main>`, `<footer>`)
- Formulários e inputs
- Acessibilidade (ARIA)

**CSS3**
- Flexbox e Grid Layout
- Responsividade (Media Queries)
- Animações e Transições

**JavaScript**
- Manipulação do DOM
- Eventos e AJAX
- ES6+ (Arrow Functions, Promises, Async/Await)

### Frameworks e Bibliotecas (Nível Intermediário)
**React** (Mais popular)
- Components e Props
- Hooks (useState, useEffect)
- React Router
- Context API

**Alternativas:**
- Vue.js (mais simples)
- Angular (enterprise)

### Ferramentas Essenciais
- **Git/GitHub:** Controle de versão
- **npm/yarn:** Gerenciador de pacotes
- **Webpack/Vite:** Bundlers
- **TypeScript:** JavaScript com tipos

---

## ⚙️ Backend Development

### Linguagens (Escolha uma para começar)

**Node.js + Express** (JavaScript no servidor)
```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000);
```

**Python + Django/Flask** (Rápido e legível)
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'
```

**PHP + Laravel** (Ainda muito usado)

### Conceitos Fundamentais

**APIs RESTful**
- GET: Buscar dados
- POST: Criar dados
- PUT/PATCH: Atualizar dados
- DELETE: Remover dados

**Autenticação**
- JWT (JSON Web Tokens)
- OAuth 2.0
- Session-based Auth

**Banco de Dados**
- **SQL:** PostgreSQL, MySQL
- **NoSQL:** MongoDB, Redis

---

## 📚 Roadmap de Estudos (6 meses)

### Mês 1-2: Fundamentos
- [ ] HTML, CSS e JavaScript puro
- [ ] Criar 5 projetos estáticos
- [ ] Git e GitHub básico

### Mês 3-4: Framework Frontend
- [ ] React (ou Vue/Angular)
- [ ] Criar 3 projetos com API pública
- [ ] TypeScript básico

### Mês 5-6: Backend e Banco de Dados
- [ ] Node.js + Express (ou Python)
- [ ] PostgreSQL/MongoDB
- [ ] Criar API completa (CRUD)
- [ ] Deploy no Heroku/Vercel

---

## 🛠️ Stack Profissional Recomendada

### Para Iniciantes em 2025
**Frontend:** React + TypeScript + Tailwind CSS
**Backend:** Node.js + Express + PostgreSQL
**Deploy:** Vercel (Front) + Railway (Back)

### Para Enterprise
**Frontend:** Next.js (React Framework)
**Backend:** NestJS (Node.js Framework)
**Database:** PostgreSQL + Redis
**Deploy:** AWS ou Google Cloud

---

## 📖 Recursos de Estudo

**Gratuitos:**
- FreeCodeCamp
- The Odin Project
- MDN Web Docs

**Pagos (vale a pena):**
- Udemy (cursos específicos)
- Frontend Masters
- Pluralsight

---

## 🎯 Projetos para Portfólio

1. **Todo List responsiva** (HTML/CSS/JS puro)
2. **Clone de Netflix** (React + API de filmes)
3. **E-commerce simples** (React + Node + Banco)
4. **Dashboard administrativo** (React + Charts)
5. **API de Blog** (Node + Express + MongoDB)

Hospede tudo no **GitHub** e crie um README.md profissional em cada projeto.

---

**Veja também:**
- [Galeria: Roadmaps Visual](/referencias/Galeria_Imagens) (Frontend/Backend)
- [Galeria: Tecnologias por Área](/referencias/Galeria_Imagens)
- [Git e GitHub - Comandos Essenciais](/referencias/Galeria_Imagens)
