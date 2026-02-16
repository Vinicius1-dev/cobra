# 🐍 Jogo da Cobrinha

Implementação clássica do jogo da cobrinha (Snake Game) desenvolvido em Python utilizando Pygame.

## 🎮 Sobre o Jogo

Jogo clássico onde você controla uma cobrinha que deve comer a comida (quadrado vermelho) para crescer. O objetivo é conseguir a maior pontuação possível sem colidir com as paredes ou com o próprio corpo!

## ✨ Funcionalidades

- 🐍 Movimentação suave da cobrinha
- 🍎 Comida com posicionamento aleatório
- 📊 Sistema de pontuação
- 💥 Detecção de colisões (paredes e corpo)
- 🎨 Interface colorida e simples
- ⚡ Velocidade ajustável

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Pygame** (biblioteca para desenvolvimento de jogos)

## 📦 Instalação

### 1. Instalar Python

Certifique-se de ter Python 3.x instalado. Baixe em: [python.org](https://www.python.org/)

### 2. Instalar Pygame
```bash
pip install pygame
```

### 3. Baixar o Jogo
```bash
git clone https://github.com/seu-usuario/jogo-cobrinha.git
cd jogo-cobrinha
```

## 🚀 Como Jogar

### Executar o jogo:
```bash
python jogo_cobrinha.py
```

### Controles:

- ⬆️ **Seta para CIMA** - Move para cima
- ⬇️ **Seta para BAIXO** - Move para baixo
- ⬅️ **Seta para ESQUERDA** - Move para esquerda
- ➡️ **Seta para DIREITA** - Move para direita

### Regras:

1. 🐍 Use as setas do teclado para mover a cobrinha
2. 🍎 Coma a comida vermelha para crescer e ganhar pontos
3. 💥 Evite colidir com as paredes
4. 💥 Evite colidir com seu próprio corpo
5. 🏆 Tente fazer a maior pontuação!

## 🎯 Mecânica do Jogo

**Pontuação:**
- Cada comida = +10 pontos
- Cobra cresce 1 segmento por comida

**Game Over:**
- Colidir com parede
- Colidir com o próprio corpo

**Velocidade:**
- Configurada em 10 FPS (frames por segundo)
- Pode ser ajustada na linha: `relogio.tick(10)`

## 🔧 Personalização

Você pode personalizar o jogo editando estas variáveis:
```python
# Tamanho da janela
LARGURA = 600  # Mudar largura
ALTURA = 400   # Mudar altura

# Cores (RGB)
VERDE = (0, 255, 0)    # Cor da cobra
VERMELHO = (255, 0, 0) # Cor da comida

# Velocidade
relogio.tick(10)  # Aumentar = mais rápido
```

## 🎓 Aprendizados

Este projeto me ajudou a praticar:

- ✅ Manipulação de eventos em Pygame
- ✅ Lógica de colisão
- ✅ Estruturas de dados (listas)
- ✅ Game loop e FPS
- ✅ Desenho de gráficos 2D
- ✅ Lógica de jogo

## 🚀 Melhorias Futuras

- [ ] Adicionar tela inicial
- [ ] Adicionar tela de game over
- [ ] Sistema de high score
- [ ] Níveis de dificuldade
- [ ] Sons e efeitos sonoros
- [ ] Power-ups especiais

## 👨‍💻 Desenvolvedor

**Vinicius Alves Silva**
- 🎓 Estudante de Ciência de Dados
- 🏆 Certificações: Google & IBM - Python
- 🐍 Foco: Python, Análise de Dados, Desenvolvimento de Jogos
- 💼 [LinkedIn](https://linkedin.com/in/vinicius-alves-silva-b666b6364)
- 💻 [GitHub](https://github.com/seu-usuario)

## 📝 Licença

Projeto desenvolvido para fins educacionais.

---

⭐ **Desenvolvido com Python e Pygame** 🐍🎮
