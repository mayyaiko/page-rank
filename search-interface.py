import tkinter as tk
from tkinter import ttk
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
        results_text.insert(tk.END, f"Title: {page['title']}\n", "title")
        results_text.insert(tk.END, f"Content: {page['content']}\n", "content")
        results_text.insert(tk.END, f"PageRank Score: {score:.4f}\n\n", "score")

# Configuração da interface com Tkinter
root = tk.Tk()
root.title("Busca com PageRank")
root.geometry("600x500")
root.configure(bg="#f0f0f0")

# Estilo dos widgets
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 10), padding=6)
style.configure("TLabel", font=("Helvetica", 12), background="#f0f0f0")
style.configure("TEntry", padding=6)

# Label de instrução
query_label = ttk.Label(root, text="Digite sua consulta:")
query_label.pack(pady=10)

# Campo de entrada para a consulta
query_entry = ttk.Entry(root, width=50, font=("Helvetica", 10))
query_entry.pack(pady=5)

# Botão de busca
search_button = ttk.Button(root, text="Buscar", command=lambda: search(query_entry.get()))
search_button.pack(pady=10)

# Campo de texto para exibir os resultados
results_frame = tk.Frame(root, bg="#f0f0f0")
results_frame.pack(pady=10, fill="both", expand=True)

results_text = tk.Text(results_frame, wrap="word", width=70, height=20, font=("Helvetica", 10))
results_text.pack(side="left", fill="both", expand=True)

# Barra de rolagem para o campo de texto
scrollbar = ttk.Scrollbar(results_frame, orient="vertical", command=results_text.yview)
scrollbar.pack(side="right", fill="y")
results_text.configure(yscrollcommand=scrollbar.set)

# Tags de estilo para os resultados
results_text.tag_config("title", font=("Helvetica", 12, "bold"), foreground="#2c3e50")
results_text.tag_config("content", font=("Helvetica", 10), foreground="#34495e")
results_text.tag_config("score", font=("Helvetica", 10, "italic"), foreground="#7f8c8d")

root.mainloop()