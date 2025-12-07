import random
import time
import numpy as np

# Gerador "normal" (se quiser comparar depois)
def generate_items_basic(n, max_weight=20, max_value=30):
    return [(random.randint(1, max_weight),
             random.randint(1, max_value)) for _ in range(n)]

# Gerador "absurdo" (para piorar a heurística):
#  - 80% dos itens: leves, valores modestos
#  - 20% dos itens: pesados, valores grandes (mas não tão eficientes)
def generate_items_absurd(n):
    items = []
    for _ in range(n):
        if random.random() < 0.2:  # 20% dos casos
            w = random.randint(20, 40)   # bem pesado
            v = random.randint(25, 60)   # valor alto, mas não proporcional ao peso
        else:  # 80% dos casos
            w = random.randint(1, 10)    # leve
            v = random.randint(5, 20)    # valor ok
        items.append((w, v))
    return items

best_value = 0
best_subset = []
iterations = 0
max_iterations = 1000000000  # limite tratável/intratável

def knapsack_bruteforce(items, L):
    """
    Força bruta com backtracking e limite de iterações.
    Espaço: O(n) (pilha + subconjunto atual).
    Tempo: O(2^n) no pior caso, aqui limitado por max_iterations.
    """
    global best_value, best_subset, iterations
    n = len(items)
    best_value = 0
    best_subset = []
    iterations = 0

    def backtrack(i, curr_w, curr_v, subset):
        global best_value, best_subset, iterations, max_iterations

        iterations += 1
        if iterations >= max_iterations:
            # interrompe a exploração (intratable na prática)
            raise TimeoutError("Execução interrompida: limite de iterações atingido (intratável na prática).")

        # poda por peso
        if curr_w > L:
            return

        # caso base
        if i == n:
            if curr_v > best_value:
                best_value = curr_v
                best_subset[:] = subset[:]
            return

        # incluir item i
        w, v = items[i]
        subset.append(i)
        backtrack(i + 1, curr_w + w, curr_v + v, subset)
        subset.pop()

        # não incluir item i
        backtrack(i + 1, curr_w, curr_v, subset)

    start = time.time()
    try:
        backtrack(0, 0, 0, [])
        status = "Completo (tratável para este n e L)"
    except TimeoutError as e:
        status = str(e)

    elapsed = time.time() - start

    return best_value, best_subset, iterations, elapsed, status

def knapsack_dp(items, L):
    """
    Programação dinâmica clássica O(n*L).
    Ótima, mas pseudo-polinomial (depende de L).
    """
    n = len(items)
    dp = [[0] * (L + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w, v = items[i-1]
        for cap in range(L + 1):
            if w <= cap:
                dp[i][cap] = max(dp[i-1][cap], dp[i-1][cap - w] + v)
            else:
                dp[i][cap] = dp[i-1][cap]

    # reconstrução dos itens escolhidos
    chosen = []
    cap = L
    for i in range(n, 0, -1):
        if dp[i][cap] != dp[i-1][cap]:
            chosen.append(i-1)
            cap -= items[i-1][0]

    return dp[n][L], chosen[::-1]

def knapsack_greedy(items, L):
    # densidade = valor/peso
    dens = sorted(
        [(i, w, v, v/w) for i, (w, v) in enumerate(items)],
        key=lambda x: x[3], reverse=True
    )

    total_value = 0
    total_weight = 0
    chosen = []

    for i, w, v, d in dens:
        if total_weight + w <= L:
            chosen.append(i)
            total_weight += w
            total_value += v

    return total_value, chosen

def test_single_instance():
    # n na faixa crítica para a força bruta
    n = random.randint(10, 50)
    items = generate_items_absurd(n)

    # capacidade aleatória, mas não muito alta (para DP ser viável)
    # peso médio aproximado: entre 1 e 40, então L moderado:
    L = random.randint(20, 200)

    print("\n============================================")
    print(f"Teste com n={n}, L={L}")
    print("============================================")
    print("Itens (peso, valor):")
    print(items)

    # B) Força Bruta
    bf_val, bf_set, bf_iters, bf_time, bf_status = knapsack_bruteforce(items, L)

    # C) DP (ótimo)
    dp_val, dp_set = knapsack_dp(items, L)

    # D) Heurística ruim
    gr_val, gr_set = knapsack_greedy_bad(items, L)

    print("\n--- Resultados ---")
    print(f"Força Bruta: valor={bf_val}, iterações={bf_iters}, tempo={bf_time:.4f}s")
    print("Status força bruta:", bf_status)
    print(f"DP (ótimo): valor={dp_val}, itens escolhidos={dp_set}")
    print(f"Heurística ruim: valor={gr_val}, itens escolhidos={gr_set}")

    if dp_val > 0:
        ratio = gr_val / dp_val
        print(f"Aproximação da heurística: {100 * ratio:.2f}% do ótimo")
    else:
        ratio = 1.0
        print("Caso degenerado: valor ótimo zero.")

    return {
        "n": n,
        "L": L,
        "bf_val": bf_val,
        "bf_iters": bf_iters,
        "bf_time": bf_time,
        "bf_status": bf_status,
        "dp_val": dp_val,
        "gr_val": gr_val,
        "ratio": ratio
    }

def run_multiple_random_tests(trials=15):
    results = []
    for t in range(trials):
        print(f"\n########### Rodando teste {t+1}/{trials} ###########")
        res = test_single_instance()
        results.append(res)

    ratios = [r["ratio"] for r in results if r["dp_val"] > 0]
    bf_complete = [r for r in results if "Completo" in r["bf_status"]]

    print("\n================= RESUMO FINAL =================")
    print(f"Número de testes: {trials}")
    print(f"Média de aproximação da heurística ruim: {100 * np.mean(ratios):.2f}% do ótimo (DP)")
    print(f"Desvio padrão da aproximação: {100 * np.std(ratios):.2f}%")

    print(f"\nForça Bruta completou em {len(bf_complete)}/{trials} testes.")
    if bf_complete:
        tempos = [r["bf_time"] for r in bf_complete]
        print(f"Tempo médio (apenas casos completos): {np.mean(tempos):.4f}s")
    else:
        print("Nenhum caso completou com força bruta (todos intratáveis com o limite atual).")

    return results
