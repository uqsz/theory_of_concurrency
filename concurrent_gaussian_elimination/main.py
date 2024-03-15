
import random
import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
import threading


def generate_random_matrix(n):
    return [[random.randint(1.0, 10.0) for _ in range(n + 1)] for _ in range(n)]


def f(k, n):  # stworz alfabet oraz D w zaleznosci od rozmiaru macierzy
    global D, sigma
    if k == n-1:
        return
    for i in range(k+1, n):
        A = "A"+str(k)+str(i)
        for x in sigma:
            D.append((A, x))
            D.append((x, A))
    for i in range(k+1, n):
        A = "A"+str(k)+str(i)
        sigma.append(A)
        for j in range(k, n+1):
            B = "B"+str(k)+str(j)+str(i)
            C = "C"+str(k)+str(j)+str(i)
            sigma.append(B)
            D.append((A, B))
            D.append((B, A))
            sigma.append(C)
            D.append((B, C))
            D.append((C, B))
    f(k+1, n)


def bfs(G, s):  # zmodyfikowany bfs
    global dis, vis
    Q = deque()
    Q.append(s)
    vis[s] = True
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if dis[v] < dis[u]+1:  # jezeli odwiedzony wierzcholek ma mniejszą wartosc eykiety od tej ktora chcemy mu nadac, to ja zmieniamy
                dis[v] = dis[u]+1
                Q.append(v)
            vis[v] = True


def test(n):  # glowna funkcja rozwiazujaca zadanie
    global sigma, D
    sigma = []
    D = []
    f(0, n)
    labels = {}
    for i, x in enumerate(sigma):
        labels[i] = x
    graph = {}  # graf reprezentujący zbior D
    for edge in D:
        start, end = edge
        if start not in graph:
            graph[start] = [end]
        else:
            graph[start].append(end)

    fnf = []  # graf zaleznosci

    for i in range(len(sigma)):  # wstepne uzupelnienie grafu zaleznosci
        fnf.append([])
        for j in range(i+1, len(sigma)):
            if sigma[j] in graph[sigma[i]]:
                fnf[i].append(j)

    for i in range(len(sigma)):  # usuniecie nadmiarowych krawedzi w grafie
        for j in range(i+1, len(sigma)):
            for k in range(j+1, len(sigma)):
                if k in fnf[i] and j in fnf[i] and k in fnf[j]:
                    fnf[i].remove(k)

    global dis, vis
    vis = [False]*len(fnf)
    dis = [0]*len(fnf)

    # etykietowanie wierzcholkow grafu za pomocą BFS dla kazdego nieodwiedzonego wierzcholka
    for v in range(len(fnf)):
        if not vis[v]:
            bfs(fnf, v)

    m = max(dis)+1  # obliczenie FNF
    res = [[] for i in range(m)]
    for i in range(m):
        for j in range(len(dis)):
            if dis[j] == i:
                res[i].append(sigma[j])

    # ZAPISYWANIE WYNIKÓW

    with open("output"+str(n)+".txt", 'w') as file:
        print("INPUT", file=file)
        print("A:", A, file=file)
        print("RESULTS", file=file)
        process_classes(res)
        print("A:", A, file=file)
        print("w/sigma:", sigma, file=file, end="\n")
        print("D =", D, file=file)
        print("FNF(|w|) =", res, "\n", file=file)
        file.write("digraph g {\n")
        for i, x in enumerate(sigma):
            file.write(f"{i+1} [label = {x}]\n")
        for i in range(len(fnf)):
            for j in fnf[i]:
                file.write(f"{i+1} -> {j+1}\n")
        file.write("}\n")

    G = nx.DiGraph()
    for i in range(len(fnf)):
        for j in fnf[i]:
            G.add_edge(i, j)
    fig, ax = plt.subplots(figsize=(8, 8))
    plt.title("Graf Diekerta dla n = " + str(n))
    pos = nx.shell_layout(G, scale=2000)
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=10,
            node_color='skyblue', edge_color='gray', linewidths=0.5)
    plt.savefig("graph" + str(n) + ".png")


def process_classes(class_set):
    global coefficients
    coefficients = {}
    for class_group in class_set:
        threads = []
        for class_name in class_group:
            thread = threading.Thread(target=worker, args=(class_name,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()


def worker(class_name):
    global A, coefficients
    operation = class_name[0]

    if operation == "A":
        i, k = map(int, class_name[1:])
        coefficients[class_name] = A[k][i] / A[i][i]

    elif operation == "B":
        i, j, k = map(int, class_name[1:])
        coefficients[class_name] = A[i][j] * coefficients[f"A{i}{k}"]

    elif operation == "C":
        i, j, k = map(int, class_name[1:])
        A[k][j] -= coefficients[f"B{i}{j}{k}"]


if __name__ == "__main__":
    global A
    for n in range(2, 5):
        if n == 3:
            A = [[2.0, 1.0, 3.0, 6.0],
                 [4.0, 3.0, 8.0, 15.0],
                 [6.0, 5.0, 16.0, 27.0]]
        else:
            A = generate_random_matrix(n)
        test(n)
