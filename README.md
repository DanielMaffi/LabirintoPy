
# Visualização de Labirinto com Pyamaze

Este projeto utiliza a biblioteca `pyamaze` para criar, visualizar e interagir com labirintos de forma simples e gráfica em Python.

## 📦 Requisitos

- Python 3 instalado
- Biblioteca `pyamaze`

Instale com o comando:

```bash
pip install pyamaze
```

---

## 🧪 Como usar

### Código principal

```python
from pyamaze import maze, agent, textLabel

# Cria um labirinto 100x100
labirinto = maze(100, 100)

# Cria o labirinto padrão
labirinto.CreateMaze()

# Mostra as células e caminhos possíveis
celulas = labirinto.grid
print(celulas)

mapa = labirinto.maze_map
print(mapa)

# Mostra o caminho perfeito do labirinto
caminhoGabarito = labirinto.path
print(caminhoGabarito)

# Cria um agente que mostra o caminho percorrido
agente = agent(labirinto, filled=True, footprints=True)

# Faz o agente seguir o caminho ideal
labirinto.tracePath({agente: caminhoGabarito}, delay=100)

# Mostra o número de passos em um rótulo
texto = textLabel(labirinto, title="N passos", value=len(caminhoGabarito))

# Executa a visualização
labirinto.run()
```

---

## ⚙️ Funcionalidades extras comentadas no código

- Criar labirintos com porcentagem de caminhos alternativos usando `loopPercent`
- Salvar e carregar labirintos com `SaveMaze=True` ou `loadMaze="Labirinto.csv"`
- Controlar manualmente a posição do agente
- Criar caminhos personalizados com dicionários ou sequências ("NWSE")
- Adicionar múltiplos agentes com características diferentes

---
