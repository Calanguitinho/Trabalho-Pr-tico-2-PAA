# 🧮 Projeto – Problema da Mochila 0/1  
### Disciplina: Projeto e Análise de Algoritmos (PAA)  
### Curso: Engenharia de Computação – PUC Minas  
### Autor: **Fábio Wnuk Hollerbach Klier**  
### Professor: **Walisson Ferreira de Carvalho**

---

## 📘 Descrição Geral

Este repositório contém o código-fonte, imagens, fluxogramas e o relatório completo utilizados na resolução da **Questão 7** do Trabalho Prático de PAA.  

O trabalho analisa o **Problema da Mochila 0/1 (Knapsack 0/1)** sob três perspectivas principais:

- **(A) Prova formal de NP-completude**
- **(B) Implementação exata exponencial (força bruta, espaço O(n))**
- **(C) Programação Dinâmica (tempo O(nL), solução ótima)**
- **(D) Heurística Gulosa (~80% de aproximação)**
- **(E) Análise de complexidade teórica**
- **(F) Testes estatísticos com dados aleatórios “absurdos”**
- **(G) Conclusão comparativa entre métodos**

O repositório inclui fluxogramas, gráficos, e todo material complementar necessário para reprodutibilidade completa.

---

## 🗂️ Estrutura do Repositório
Trabalho-Mochila-PAA/
│
├── codigo/
│ ├── knapsack_full_experiments.py # Código completo dos algoritmos + testes + gráficos
│ ├── fluxogramas_generator.py # Script para gerar fluxogramas com Graphviz
│ ├── requirements.txt # Bibliotecas necessárias
│
├── imagens/
│ ├── fluxograma_bruteforce.gv.png
│ ├── fluxograma_dp.gv.png
│ ├── fluxograma_heuristica.gv.png
│ ├── tempo_bruteforce.png
│ ├── aproximacao_greedy.png
│ ├── comparacao_algoritmos.png
│ └── PUClogo.png
│
├── relatorio/
│ ├── main.tex # Relatório completo final em LaTeX
│ └── pdf_final/ # (opcional) PDF exportado do Overleaf
│
└── README.md


---

## 🚀 Como Executar o Projeto

### 🔧 1. Instalar dependências

Se estiver usando Python localmente:

```bash
pip install -r codigo/requirements.txt
No Google Colab:

!apt-get install graphviz
!pip install graphviz matplotlib numpy
▶️ 2. Executar todos os experimentos

Rodar força bruta, DP, heurística, gráficos e estatísticas:

python codigo/knapsack_full_experiments.py


Isso irá:

realizar 15 testes automáticos com dados aleatórios,

gerar todos os gráficos na pasta imagens/,

imprimir tabela de resultados no terminal.

🔁 3. Gerar fluxogramas
python codigo/fluxogramas_generator.py


Os fluxogramas serão criados na pasta imagens/ como:

fluxograma_bruteforce.gv.png

fluxograma_dp.gv.png

fluxograma_heuristica.gv.png

📊 Gráficos Disponíveis

Todos são gerados automaticamente:

Gráfico	Arquivo	Descrição
Tempo da força bruta	tempo_bruteforce.png	Mostra explosão exponencial conforme n cresce
Aproximação da heurística	aproximacao_greedy.png	Mostra desempenho médio ≈ 82%
Comparação de tempos médios	comparacao_algoritmos.png	Compara força bruta, DP e heurística
🔁 Fluxogramas

Gerados em Graphviz:

fluxograma_bruteforce.gv.png

fluxograma_dp.gv.png

fluxograma_heuristica.gv.png

Esses diagramas aparecem no relatório LaTeX para ilustrar cada algoritmo.

📄 Relatório Completo em LaTeX

O relatório final está na pasta:

relatorio/main.tex


Contém:

Prova formal de NP-completude

Pseudocódigos em estilo acadêmico

Fluxogramas

Tabela dos 15 testes

Gráficos experimentais

Discussão crítica dos resultados

Conclusão técnica

Referências bibliográficas

Garey & Johnson

Cormen

Ziviani

O PDF pode ser gerado abrindo o main.tex no Overleaf e enviando as imagens da pasta imagens/.

📌 Destaques Importantes

A força bruta possui limite explícito de 10^9 iterações, evidenciando a fronteira tratável/intratável.

A DP é ótima, mas pseudo-polinomial: depende de L, não apenas de n.

A heurística foi escolhida propositalmente para performar ~80% em média.

O gerador absurdo de dados causa queda intencional da heurística.

Todos os resultados foram obtidos com 15 rodadas aleatórias para robustez estatística.

📚 Bibliografia Utilizada

Cormen, Leiserson, Rivest, Stein – Algoritmos: Teoria e Prática

Garey & Johnson – Computers and Intractability

Ziviani – Projeto de Algoritmos

📬 Contato

Autor: Fábio Wnuk Hollerbach Klier
PUC Minas – Engenharia de Computação

🎉 Agradecimentos

Agradecimento especial ao professor Walisson Ferreira de Carvalho, cujas exigências metodológicas motivaram a elaboração de uma análise completa unindo teoria, prática e documentação profissional.
