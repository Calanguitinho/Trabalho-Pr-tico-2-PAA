!apt-get install graphviz
!pip install graphviz
from graphviz import Digraph

# ============================================================
# FLUXOGRAMA 1: Força Bruta
# ============================================================

dot1 = Digraph("fluxograma_bruteforce", format="png")
dot1.attr(rankdir="TB", size="8,10")

dot1.node("start", "Início", shape="oval")
dot1.node("call", "Backtrack(i, peso, valor, S)", shape="rectangle")
dot1.node("check_iter", "iteracoes >= max_iterations?", shape="diamond")
dot1.node("stop_iter", "Interrompe\n(intratável)", shape="oval")
dot1.node("check_peso", "peso > L?", shape="diamond")
dot1.node("return_peso", "Retorna", shape="oval")
dot1.node("check_final", "i == n?", shape="diamond")
dot1.node("update_best", "Atualiza melhor solução", shape="rectangle")
dot1.node("return_final", "Retorna", shape="oval")
dot1.node("include", "Incluir item i", shape="rectangle")
dot1.node("exclude", "Não incluir item i", shape="rectangle")

# Arestas SEM label (Graphviz exige isso)
dot1.edge("start", "call")
dot1.edge("call", "check_iter")

dot1.edge("check_iter", "stop_iter", label="sim")
dot1.edge("check_iter", "check_peso", label="não")

dot1.edge("check_peso", "return_peso", label="sim")
dot1.edge("check_peso", "check_final", label="não")

dot1.edge("check_final", "update_best", label="sim")
dot1.edge("update_best", "return_final")

dot1.edge("check_final", "include", label="não")
dot1.edge("include", "call")

dot1.edge("call", "exclude")   # volta após chamada recursiva
dot1.edge("exclude", "call")

dot1.render()
print("fluxograma_bruteforce.png gerado!")


# ============================================================
# FLUXOGRAMA 2: Programação Dinâmica
# ============================================================

dot2 = Digraph("fluxograma_dp", format="png")
dot2.attr(rankdir="TB", size="8,10")

dot2.node("start", "Início", shape="oval")
dot2.node("create_dp", "Criar tabela DP[n+1][L+1]", shape="rectangle")
dot2.node("fill_dp", "Preencher tabela DP\ndpela recorrência", shape="rectangle")
dot2.node("reconstruct", "Reconstrução da solução ótima", shape="rectangle")
dot2.node("end", "Fim", shape="oval")

dot2.edge("start", "create_dp")
dot2.edge("create_dp", "fill_dp")
dot2.edge("fill_dp", "reconstruct")
dot2.edge("reconstruct", "end")

dot2.render()
print("fluxograma_dp.png gerado!")


# ============================================================
# FLUXOGRAMA 3: Heurística Gulosa
# ============================================================

dot3 = Digraph("fluxograma_heuristica", format="png")
dot3.attr(rankdir="TB", size="8,10")

dot3.node("start", "Início", shape="oval")
dot3.node("sort", "Ordenar itens por valor\n(decrescente)", shape="rectangle")
dot3.node("loop", "Para cada item i", shape="diamond")
dot3.node("check_cap", "peso + p_i <= L?", shape="diamond")
dot3.node("include", "Incluir item i", shape="rectangle")
dot3.node("skip", "Ignorar item", shape="rectangle")
dot3.node("end", "Fim", shape="oval")

dot3.edge("start", "sort")
dot3.edge("sort", "loop")

dot3.edge("loop", "check_cap", label="próximo i")

dot3.edge("check_cap", "include", label="sim")
dot3.edge("include", "loop")

dot3.edge("check_cap", "skip", label="não")
dot3.edge("skip", "loop")

dot3.edge("loop", "end", label="i terminado")

dot3.render()
print("fluxograma_heuristica.png gerado!")
