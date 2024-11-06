import tkinter as tk
from PageRank import build_adjacency_matrix, pagerank_with_query
from PageList import pages

# Função de busca que utiliza o PageRank com a consulta fornecida
def search(query):
    M = build_adjacency_matrix(pages)
    ranks = pagerank_with_query(M, query, pages)
    ranked_pages = sorted(enumerate(ranks), key=lambda x: x[1], reverse=True)
    
    # Exibe os resultados
    results_text.delete("1.0", tk.END)
    for idx, score in ranked_pages:
        page = pages[idx]
        results_text.insert(tk.END, f"Title: {page['title']}\n")
        results_text.insert(tk.END, f"Content: {page['content']}\n")
        results_text.insert(tk.END, f"PageRank Score: {score:.4f}\n\n")

# Configuração da interface com Tkinter
root = tk.Tk()
root.title("Simples Página de Busca com PageRank")

query_label = tk.Label(root, text="Digite sua consulta:")
query_label.pack()

query_entry = tk.Entry(root, width=50)
query_entry.pack()

search_button = tk.Button(root, text="Buscar", command=lambda: search(query_entry.get()))
search_button.pack()

results_text = tk.Text(root, wrap="word", width=60, height=20)
results_text.pack()

root.mainloop()
