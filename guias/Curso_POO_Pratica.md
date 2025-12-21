# 🎨 Curso: Programação Orientada a Objetos (POO)

Domine o paradigma que domina o mercado de desenvolvimento.

---

## 🎯 O Que é POO?

**Definição:** Forma de programar que organiza código em **objetos** (coisas) ao invés de só funções.

**Vantagem:** Código mais organizado, reutilizável e fácil de manter.

---

## 📚 Módulo 1: Classes e Objetos

### Conceito Base
**Classe** = Molde (planta da casa)
**Objeto** = Instância (casa construída)

### Exemplo Prático
```python
# Classe (molde)
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
    
    def acelerar(self, valor):
        self.velocidade += valor
        print(f"Acelerando... Velocidade: {self.velocidade} km/h")
    
    def frear(self):
        self.velocidade = 0
        print("Carro parado")

# Objetos (instâncias)
carro1 = Carro("Toyota", "Corolla", 2023)
carro2 = Carro("Honda", "Civic", 2024)

carro1.acelerar(50)  # Acelerando... Velocidade: 50 km/h
carro2.acelerar(80)  # Acelerando... Velocidade: 80 km/h
```

---

## 🔒 Módulo 2: Encapsulamento

### Conceito
Esconder detalhes internos e expor apenas o necessário.

### Atributos Privados
```python
class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial  # Privado (__)
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return True
        return False
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            return True
        return False
    
    def get_saldo(self):  # Getter
        return self.__saldo

conta = ContaBancaria("João", 1000)
conta.depositar(500)
print(conta.get_saldo())  # 1500
# print(conta.__saldo)  # ERRO! Atributo privado
```

**Por quê?** Previne modificação acidental/mal-intencionada.

---

## 🧬 Módulo 3: Herança

### Conceito
Criar classes baseadas em outras (reaproveitar código).

### Exemplo
```python
# Classe base (pai)
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def calcular_bonus(self):
        return self.salario * 0.1

# Classe derivada (filho)
class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)  # Chama construtor do pai
        self.departamento = departamento
    
    def calcular_bonus(self):  # Sobrescreve método do pai
        return self.salario * 0.2

class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem

# Uso
gerente = Gerente("Maria", 10000, "TI")
dev = Desenvolvedor("João", 8000, "Python")

print(gerente.calcular_bonus())  # 2000 (20%)
print(dev.calcular_bonus())      # 800 (10%)
```

---

## 🎭 Módulo 4: Polimorfismo

### Conceito
Mesma interface, comportamentos diferentes.

### Exemplo
```python
class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

class Vaca(Animal):
    def fazer_som(self):
        return "Muuu!"

# Polimorfismo em ação
animais = [Cachorro(), Gato(), Vaca()]

for animal in animais:
    print(animal.fazer_som())
# Au au!
# Miau!
# Muuu!
```

**Vantagem:** Código flexível e extensível.

---

## 📜 Módulo 5: Abstração

### Classes Abstratas
Definem interface sem implementação completa.

```python
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass
    
    @abstractmethod
    def calcular_perimetro(self):
        pass

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return 3.14 * self.raio ** 2
    
    def calcular_perimetro(self):
        return 2 * 3.14 * self.raio

# Uso
ret = Retangulo(5, 3)
circ = Circulo(4)

print(ret.calcular_area())   # 15
print(circ.calcular_area())  # 50.24
```

---

## 🏗️ Módulo 6: Design Patterns (Padrões de Projeto)

### Singleton
Garante que classe tenha apenas UMA instância.

```python
class Database:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

db1 = Database()
db2 = Database()
print(db1 is db2)  # True (mesma instância)
```

### Factory
Cria objetos sem especificar classe exata.

```python
class NotificacaoFactory:
    @staticmethod
    def criar(tipo):
        if tipo == "email":
            return NotificacaoEmail()
        elif tipo == "sms":
            return NotificacaoSMS()
        elif tipo == "push":
            return NotificacaoPush()

class NotificacaoEmail:
    def enviar(self, mensagem):
        print(f"Email: {mensagem}")

class NotificacaoSMS:
    def enviar(self, mensagem):
        print(f"SMS: {mensagem}")

# Uso
notif = NotificacaoFactory.criar("email")
notif.enviar("Olá!")
```

### Observer
Objetos observam mudanças em outros.

```python
class Subject:
    def __init__(self):
        self._observers = []
    
    def adicionar_observer(self, observer):
        self._observers.append(observer)
    
    def notificar(self, mensagem):
        for observer in self._observers:
            observer.atualizar(mensagem)

class Observer:
    def __init__(self, nome):
        self.nome = nome
    
    def atualizar(self, mensagem):
        print(f"{self.nome} recebeu: {mensagem}")

# Uso
subject = Subject()
obs1 = Observer("João")
obs2 = Observer("Maria")

subject.adicionar_observer(obs1)
subject.adicionar_observer(obs2)

subject.notificar("Novo post!")
# João recebeu: Novo post!
# Maria recebeu: Novo post!
```

---

## 🎯 Projeto Prático: Sistema de Biblioteca

```python
class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.emprestado = False
    
    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True
            return True
        return False
    
    def devolver(self):
        self.emprestado = False

class Usuario:
    def __init__(self, nome, id_usuario):
        self.nome = nome
        self.id_usuario = id_usuario
        self.livros_emprestados = []
    
    def pegar_livro(self, livro):
        if livro.emprestar():
            self.livros_emprestados.append(livro)
            return True
        return False
    
    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            livro.devolver()
            self.livros_emprestados.remove(livro)
            return True
        return False

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
    
    def adicionar_livro(self, livro):
        self.livros.append(livro)
    
    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)
    
    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None

# Uso
biblioteca = Biblioteca()

livro1 = Livro("Clean Code", "Robert Martin", "123456")
livro2 = Livro("Python Fluente", "Luciano Ramalho", "789012")

usuario1 = Usuario("João", 1)

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.cadastrar_usuario(usuario1)

livro = biblioteca.buscar_livro("Clean Code")
if usuario1.pegar_livro(livro):
    print(f"{usuario1.nome} pegou emprestado '{livro.titulo}'")
```

---

## 📖 Princípios SOLID

### S - Single Responsibility
Cada classe deve ter UMA responsabilidade.

### O - Open/Closed
Aberto para extensão, fechado para modificação.

### L - Liskov  Substitution
Subclasses devem substituir classes base.

### I - Interface Segregation
Interfaces específicas > interfaces gerais.

### D - Dependency Inversion
Dependa de abstrações, não de implementações.

---

**Veja também:**
- [Algoritmos e Estruturas de Dados](/guias/Curso_Algoritmos_Estruturas_Dados)
- [Python para Automação](/guias/Curso_Python_Automacao)
- [Desenvolvimento Web](/guias/Guia_Desenvolvimento_Web)
