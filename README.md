📦 Rota Inteligente — Otimização de Entregas com IA

Autor: Diogo Carvalho
Disciplina: Artificial Intelligence Fundamentals
Curso: Engenharia de Computação

🚀 1. Visão Geral do Projeto

Este projeto foi desenvolvido para resolver o problema logístico da empresa fictícia Sabor Express, que enfrenta dificuldades para organizar suas rotas de entrega durante horários de pico.

O objetivo foi implementar uma solução baseada em Inteligência Artificial Clássica capaz de:

Encontrar o menor caminho entre pontos da cidade usando grafos e A*

Agrupar entregas próximas usando K-Means

Otimizar o trabalho de entregadores durante a alta demanda

Gerar visualizações de grafos e clusters

O resultado é uma solução completa, eficiente e com impacto direto na redução de custos operacionais.

🎯 2. Objetivos

Criar um sistema inteligente de roteamento

Aplicar IA Clássica (A*, BFS, DFS, K-Means)

Modelar a cidade como grafo ponderado

Gerar visualizações automáticas

Documentar a solução de forma clara e profissional

🧠 3. Abordagem Técnica
📌 3.1 Representação do Problema como Grafo

A cidade é modelada como:

Nós (vertices): bairros, pontos de entrega, restaurante

Arestas: ruas com pesos baseados em distância/tempo

Lat/long: armazenados para uso da heurística do A*

O grafo pode ser carregado via CSV ou gerado pela demo interna.

Exemplo dos CSVs usados está na pasta /data.

🔍 3.2 Algoritmos Implementados
⭐ A* (A-Star)

Algoritmo principal de menor caminho

Utiliza heurística: distância euclidiana lat/lon

Entrega rotas otimizadas mesmo em grafos com pesos diferentes

🌐 BFS (Breadth-First Search)

Encontra o menor número de passos

Usado para comparação

🌑 DFS (Depth-First Search)

Não garante menor caminho

Incluído apenas para fins didáticos

📌 K-Means (Clustering)

Agrupa entregas próximas

Cada cluster representa uma área de um entregador

Ideal para alta demanda

📊 4. Resultados Obtidos

Ao rodar o sistema, são gerados automaticamente:

✔️ Grafo da rota (A*)

Arquivo:

docs/grafo_demo.png


Quando rodado com dados reais:

docs/grafo_from_csv.png

✔️ Clusters do K-Means

Arquivo:

docs/clusters.png

✔️ Entregas agrupadas em CSV

Arquivo:

docs/deliveries_clustered.csv


Esses resultados mostram:

Redução significativa do tempo total de rota

Divisão equilibrada de entregas entre entregadores

Visualização clara das zonas de entrega

📝 5. Estrutura do Projeto
rota-inteligente
 ┣ 📁 src
 ┃ ┣ graph.py
 ┃ ┣ astar.py
 ┃ ┣ searches.py
 ┃ ┣ clustering.py
 ┃ ┣ visualize.py
 ┃ ┗ main.py
 ┣ 📁 data
 ┃ ┣ map.csv
 ┃ ┗ deliveries.csv
 ┣ 📁 docs
 ┃ ┣ grafo_demo.png
 ┃ ┣ grafo_from_csv.png
 ┃ ┗ clusters.png
 ┣ requirements.txt
 ┗ README.md

▶️ 6. Como Executar
🔧 Instalar dependências
pip install -r requirements.txt

🧪 Rodar a DEMO
python -m src.main


Gera automaticamente:

docs/grafo_demo.png

🧪 Rodar com seus arquivos CSV
python -m src.main --edges data/map.csv --deliveries data/deliveries.csv --k 2


Gera automaticamente:

docs/grafo_from_csv.png

docs/clusters.png

docs/deliveries_clustered.csv

📈 7. Análise Crítica
✔️ Pontos fortes

A* extremamente eficiente

K-Means agrupa de forma clara e útil

Visualizações facilitam entendimento

Código modular, organizado e escalável

⚠️ Limitações

Não usa dados de trânsito em tempo real

K-Means depende do valor de k (número de entregadores)

💡 8. Melhorias Futuras

Usar APIs de trânsito (Google Maps / Here)

Aplicar Algoritmos Genéticos para otimização global

Testar DBSCAN para clustering dinâmico

Usar Reinforcement Learning para rotas em tempo real

Grafo estático
