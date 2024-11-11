import numpy as np

def build_adjacency_matrix(pages):
    """Cria uma matriz de adjacência para as páginas."""
    N = len(pages)
    M = np.zeros((N, N))
    for i, page in pages.items():
        for link in page["links"]:
            M[link][i] = 1
    # Normaliza as colunas para que cada uma delas some 1 (evita divisão por zero)
    M = M / M.sum(axis=0, where=(M.sum(axis=0) != 0))  
    return M

def pagerank_with_query(M, query, pages, num_iterations=100, d=0.85):
    """Calcula o PageRank ajustado para relevância de uma consulta."""
    N = M.shape[1]
    ranks = np.ones(N) / N  # Inicializa PageRank
    relevance_boost = np.array([1.5 if query.lower() in page["content"].lower() else 1.0 for page in pages.values()])
    
    for _ in range(num_iterations):
        # Atualiza ranks usando o cálculo iterativo do PageRank
        ranks = (1 - d) / N + d * M.dot(ranks)
        # Aplica o boost de relevância e normaliza
        ranks = ranks * relevance_boost
        ranks /= ranks.sum()  # Normaliza para que a soma seja 1
    
    return (ranks*10) # Ajustando para que a normalização não fique tão baixa.
