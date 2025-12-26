# 🏢 Windows Server & Active Directory: Master Class Edition
> **Nível:** Intermediário ao Administrador | **Foco:** Governança e Infraestrutura
---

## 📖 Introdução: O Cérebro da Empresa

Em uma casa, cada um cuida da sua senha. Em uma empresa com 500 funcionários, isso seria impossível. O **Windows Server** com o **Active Directory (AD)** serve para centralizar tudo. Você cria o usuário uma única vez, e ele pode logar em qualquer computador da empresa com as mesmas permissões.

---

## 🏗️ Módulo 1: O Diretório Ativo (Active Directory)

O AD é um banco de dados que guarda "Objetos" (Usuários, Computadores, Impressoras).

### 📝 No seu Caderno (A Hierarquia):
- **Floresta:** O nível mais alto (A empresa toda).
- **Domínio:** Uma unidade lógica (Ex: `empresa.local`).
- **Árvore:** Um conjunto de domínios.
- **Unidade Organizacional (OU):** Pastas para organizar por departamento (Ex: RH, TI, Vendas).

---

## ⚙️ Módulo 2: GPO (Group Policy Object)

É aqui que o administrador "manda" nos computadores. Através de uma GPO, você pode:
*   Mudar o papel de parede de todos os PCs ao mesmo tempo.
*   Bloquear o acesso ao Painel de Controle.
*   Instalar um software automaticamente em 200 máquinas.

### 📝 Regra de Ouro (Herança):
As políticas aplicadas no nível de **Domínio** descem para todas as **OUs** abaixo dele. Se você bloquear o USB na raiz, ninguém na empresa usa USB.

---

## 🌍 Módulo 3: Serviços de Infraestrutura (DNS e DHCP)

O Windows Server geralmente é o "mestre" desses serviços que vimos em Redes.
*   **DNS no AD:** Sem ele, o herói do AD não funciona. Os computadores usam o DNS para achar o "Controlador de Domínio".
*   **Escopo DHCP:** É onde você define a faixa de IPs que o servidor vai entregar.

---

## 🛡️ Módulo 4: Permissões NTFS e Compartilhamento

Como garantir que o estagiário não apague a planilha da diretoria?
1.  **Compartilhamento:** Permissão para entrar na pasta pela rede.
2.  **NTFS:** Permissão para o que ele pode fazer COM os arquivos (Ler, Gravar, Modificar).
*   *Dica:* A permissão mais restritiva sempre vence!

---

## 📝 Exercícios de Fixação (Para responder no caderno!)

1.  O que é o **Active Directory** e qual sua principal vantagem para uma empresa?
2.  Explique a diferença entre uma **Unidade Organizacional (OU)** e um **Grupo** no Windows Server.
3.  O que é uma **GPO** e dê um exemplo real de como um técnico de TI a usaria.
4.  Por que o serviço de **DNS** é vital para o funcionamento de um domínio Windows?
5.  O que acontece se um usuário for movido de uma OU para outra com uma GPO diferente?
6.  Qual a diferença entre a permissão de **Leitura** e a permissão de **Modificação** no NTFS?
7.  Para que serve o comando `gpupdate /force` no prompt do Windows?
8.  O que é um **Controlador de Domínio (DC)**?
9.  Como o Windows Server ajuda na segurança cibernética de uma empresa?
10. **Desafio:** Se um funcionário esqueceu a senha, em qual ferramenta do Windows Server você iria para resetá-la?

---

### 🚀 Próximos Passos
- [☁️ Cloud Computing](/guias/Curso_Cloud_Computing) - Aprenda a levar esse servidor para a nuvem.
- [🛠️ Troubleshooting](/guias/Guia_Troubleshooting_Profissional) - Resolva erros de login e permissão.
- [🛂 Roadmap Certificações](/guias/Guia_Roadmap_Certificacoes) - Prepare-se para a prova MS-900 ou AZ-800.
