
# 🎓 Show do Milhão – Python Educacional

Este projeto é uma adaptação interativa do clássico programa de TV “Show do Milhão”, desenvolvida em Python com fins pedagógicos. O objetivo é gamificar o processo de aprendizagem de lógica de programação, estruturas de controle, algoritmos, boas práticas de software e pensamento computacional, voltado especialmente para estudantes do curso de Desenvolvimento de Software Multiplataforma da FATEC.

---

## 🚀 Objetivos do Projeto

- Reforçar o pensamento computacional de forma divertida e prática.
- Aplicar conceitos fundamentais de Python de forma modular e escalável.
- Estimular a aprendizagem ativa com uso de gamificação.
- Desenvolver habilidades reais de engenharia de software e versionamento.
- Proporcionar um ambiente educativo para revisão de conteúdos técnicos.

---

## 🧠 Funcionalidades

- Banco de 100 perguntas temáticas com alternativas e dicas.
- Perguntas com dificuldade crescente.
- Sistema de pontuação automática (+10 por acerto).
- Três ajudas disponíveis por jogo:
  - [D]ica
  - [P]ular
  - [E]liminar duas
- Feedback imediato após cada resposta.
- Reinício ou encerramento ao final do jogo.
- Modularização clara com arquivos independentes para cada etapa.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- Terminal ou IDE (VS Code, PyCharm, IDLE)
- JSON (para banco de dados de perguntas)
- Git + GitHub (controle de versão)

---

## 🗂️ Estrutura do Projeto

```
show-do-milhao-python/
├── main.py                          # Arquivo principal
├── perguntas_show_do_milhao.json   # Banco com 100 perguntas
├── scripts/
│   ├── etapa1_intro.py             # Boas-vindas e introdução
│   ├── etapa2_perguntas.py         # Leitura e sorteio de perguntas
│   ├── etapa3_jogo.py              # Lógica principal do jogo
│   └── encerrar_jogo.py            # Feedback final e decisão
```

---

## ▶️ Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/show-do-milhao-python.git
```

2. Acesse a pasta do projeto:
```bash
cd show-do-milhao-python
```

3. Execute o jogo:
```bash
python main.py
```

---

## ✨ Próximos Passos (Sugestões de Expansão)

- Interface gráfica com `tkinter`.
- Integração web com `Flask`.
- Armazenamento de ranking com `JSON` ou `SQLite`.
- Exportação automática de pontuação.
- Suporte para múltiplos jogadores.
- Sistema de categorias temáticas (Python, lógica, engenharia de software etc).

---

## 👨‍🏫 Público-Alvo

Estudantes de cursos técnicos e superiores em tecnologia, especialmente os que estão aprendendo:
- Algoritmos e lógica de programação
- Estruturas de dados
- Fundamentos de Python
- Engenharia de software

---

## 📄 Licença

Distribuído sob a Licença MIT. Consulte o arquivo LICENSE para mais informações.

---

“Programar é transformar lógica em experiência de aprendizagem.”

Desenvolvido por Graciliano Tolentino | FATEC – DSM
