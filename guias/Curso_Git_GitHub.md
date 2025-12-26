# 📂 Git e GitHub Profissional: Master Class Edition
![Banner Git](/banner_git.png)
> **Nível:** Iniciante ao Colaborador | **Foco:** Controle de Versão e Trabalho em Equipe
---

## 📖 Introdução: A Máquina do Tempo do Código

Sabe quando você salva um trabalho como `trabalho_final`, depois `trabalho_final_v2`, depois `trabalho_final_agora_vai`? O **Git** resolve isso. Ele é uma "máquina do tempo" para o seu código. Você pode voltar para qualquer ponto do passado se fizer algo errado, e pode trabalhar com outras 100 pessoas no mesmo arquivo sem que um apague o que o outro fez.

---

## 🏗️ Módulo 1: O Fluxo de Trabalho (Workflow)

O Git trabalha em 3 "estados" principais. Entender isso é a chave para não se perder.

### 📝 No seu Caderno (Os 3 Áreas):
1.  **Working Directory:** Onde você está escrevendo o código agora (arquivos modificados).
2.  **Staging Area (Index):** Onde você coloca os arquivos que "estão prontos para serem salvos" (`git add`).
3.  **Local Repository:** Onde o Git salva a versão permanentemente no seu PC (`git commit`).

O **GitHub** é apenas a "casa nas nuvens" onde você sobe esse repositório para o mundo ver (`git push`).

---

## ⚙️ Módulo 2: Comandos de Sobrevivência

Dominar o Git é dominar estes comandos:

*   `git init`: Começa o rastreio na pasta.
*   `git status`: O comando mais importante! Ele te diz o que está acontecendo agora.
*   `git add .`: Prepara todos os arquivos para o salvamento.
*   `git commit -m "mensagem"`: Tira uma "foto" do código com um comentário do que você mudou.
*   `git log`: Vê o histórico de todas as fotos (commits) já tiradas.

---

## 🌳 Módulo 3: Branchs (Caminhos Paralelos)

A **Branch** (Ramo) permite que você crie uma "cópia segura" do seu código para testar uma ideia nova sem estragar a versão principal (`main`). 

### 📝 Estratégia de Mestre:
Nunca faça mudanças diretas na `main`. Crie uma branch chamada `feature-nome-da-ideia`, teste tudo, e depois faça o **Merge** (fusão) com a principal.

---

## 📝 Exercícios de Fixação (Para responder no caderno!)

1.  O que é o Git e qual a principal diferença entre ele e o GitHub?
2.  Explique com uma analogia o que é a **Staging Area**.
3.  Para que serve o comando `git commit -m "..."` e por que a mensagem deve ser clara?
4.  O que acontece se você rodar o comando `git push` sem antes ter feito um `git commit`?
5.  Como você faria para voltar o seu código para uma versão de 3 dias atrás?
6.  O que é um **Conflito de Merge** e como ele acontece?
7.  Para que serve o arquivo `.gitignore`? Dê dois exemplos de arquivos que devem estar nele.
8.  Qual o comando para criar uma nova **Branch** chamada \"teste\"?
9.  O que é um **Pull Request (PR)** no GitHub?
10. **Desafio:** No seu caderno, descreva a sequência exata de comandos (do íncio ao fim) para criar uma pasta, iniciar o git, criar um arquivo e subir para o GitHub pela primeira vez.

---

### 🚀 Próximos Passos
- [🐍 Python para Automação](/guias/Curso_Python_Automacao) - Salve seus scripts no GitHub.
- [🌐 Desenvolvimento Web](/guias/Guia_Desenvolvimento_Web) - Publique seu portfólio usando GitHub Pages.
- [🏢 Windows Server](/guias/Curso_Windows_Server_AD) - O Azure DevOps usa Git por baixo dos panos.
