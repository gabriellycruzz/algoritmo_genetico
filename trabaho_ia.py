# EQUIPE: GABRIELLY XAVIER E NAJLA MARIA


import random

# 1º Passo: função para calcular o fitness (pares de rainhas que não se atacam)
def calcular_fitness(tabuleiro):
    n = len(tabuleiro)
    nao_atacantes = 0
    for i in range(n):
        for j in range(i + 1, n):
            if tabuleiro[i] != tabuleiro[j] and abs(tabuleiro[i] - tabuleiro[j]) != abs(i - j):
                nao_atacantes += 1
    return nao_atacantes

# 2º Passo: função para gerar a população inicial
def gerar_populacao(tamanho):
    return [[random.randint(1, 8) for _ in range(8)] for _ in range(tamanho)]

# 3º Passo: seleção de pais por roleta
def selecionar_pais(populacao, fitnesses):
    total_fitness = sum(fitnesses)
    escolha = random.uniform(0, total_fitness)
    acumulado = 0
    for i, fitness in enumerate(fitnesses):
        acumulado += fitness
        if acumulado >= escolha:
            return populacao[i]

# 4º Passo: função de crossover
def crossover(pai1, pai2):
    ponto_corte = random.randint(1, 7)
    filho1 = pai1[:ponto_corte] + pai2[ponto_corte:]
    filho2 = pai2[:ponto_corte] + pai1[ponto_corte:]
    return filho1, filho2

# 5º Passo: função de mutação
def mutar(individuo, txmut):
    for i in range(len(individuo)):
        if random.random() < txmut:
            individuo[i] = random.randint(1, 8)

# 6º Passo: algoritmo Genético
def algoritmo_genetico(tampop, itmax, txmut):
    populacao = gerar_populacao(tampop)
    for geracao in range(itmax):
        fitnesses = [calcular_fitness(ind) for ind in populacao]
        nova_populacao = []
        
        while len(nova_populacao) < tampop:
            pai1 = selecionar_pais(populacao, fitnesses)
            pai2 = selecionar_pais(populacao, fitnesses)
            filho1, filho2 = crossover(pai1, pai2)
            mutar(filho1, txmut)
            mutar(filho2, txmut)
            nova_populacao.extend([filho1, filho2])

        populacao = sorted(nova_populacao, key=calcular_fitness, reverse=True)[:tampop]
        melhor_individuo = populacao[0]
        melhor_fitness = calcular_fitness(melhor_individuo)
        
        #7º Passo: imprime a solução encontrada
        if melhor_fitness == 28:
            print(f"Solução encontrada na geração {geracao + 1}: {melhor_individuo}")
            return melhor_individuo
        
        # 8º Passo: imprime o progresso da geração
        print(f"Geração {geracao + 1}: Melhor Fitness = {melhor_fitness}")

    print(f"Melhor solução encontrada após {itmax} gerações: {populacao[0]}")
    return populacao[0]


# Testar o algoritmo
tampop = 150
itmax = 100
txmut = 0.2
algoritmo_genetico(tampop, itmax, txmut)