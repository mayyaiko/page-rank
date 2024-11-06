import numpy as np

def pagerank(M, num_iterations=100, d=0.85):
  
    N = M.shape[1]  # número de páginas
    ranks = np.ones(N) / N  # inicializa PageRank com valores iguais
    
    for _ in range(num_iterations):
        ranks = (1 - d) / N + d * M.dot(ranks)
    
    return ranks

# Exemplo de uso:
# Define uma matriz de adjacência para um grafo simples
M = np.array([
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
], dtype=float)

# Normaliza as colunas para que cada coluna some 1 (ajustando para o modelo de Markov)
M = M / M.sum(axis=0)

# Calcula o PageRank
pagerank_values = pagerank(M)
print("Valores de PageRank:", pagerank_values)
