from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


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


def test(eq, A, w, num=0):  # glowna funkcja rozwiazujaca zadanie
    D = []  # zbior D
    I = []  # zbior I
    for i in range(len(eq)):  # petla uzupelniająca zbiory D i I
        for j in range(i, len(eq)):
            if i == j:
                D.append((A[i], A[j]))
            elif eq[i][0] in eq[j][1:3] or eq[j][0] in eq[i][1:3]:  # sprawdzanie zaleznosci rownan
                D.append((A[j], A[i]))
                D.append((A[i], A[j]))
            else:
                I.append((A[i], A[j]))
                I.append((A[j], A[i]))

    graph = {}  # graf reprezentujący zbior D
    for edge in D:
        start, end = edge
        if start not in graph:
            graph[start] = [end]
        else:
            graph[start].append(end)

    fnf = []  # graf zaleznosci

    for i in range(len(w)):  # wstepne uzupelnienie grafu zaleznosci
        fnf.append([])
        for j in range(i+1, len(w)):
            if w[j] in graph[w[i]]:
                fnf[i].append(j)

    for i in range(len(w)):  # usuniecie nadmiarowych krawedzi w grafie
        for j in range(i+1, len(w)):
            for k in range(j+1, len(w)):
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
                res[i].append(w[j])

    save(fnf, w, D, I, res, num)  # zapis wyników


def save(fnf, w, D, I, g, num):  # funkcja zapisująca wyniki do plikow
    plt.clf()
    labels = {}
    for i, x in enumerate(w):
        labels[i] = x
    with open("output"+str(num)+".txt", 'w') as file:
        print("INPUT", file=file)
        print("Equations:", eq, file=file)
        print("A:", A, file=file)
        print("w:", w, file=file)
        print("RESULTS", file=file)
        print("D =", D, file=file)
        print("I =", I, file=file)
        print("FNF(|w|) =", g, "\n", file=file)
        file.write("digraph g {\n")
        for i, x in enumerate(w):
            file.write(f"{i+1} [label = {x}]\n")
        for i in range(len(fnf)):
            for j in fnf[i]:
                file.write(f"{i+1} -> {j+1}\n")
        file.write("}\n")

    G = nx.DiGraph()
    for i in range(len(fnf)):
        for j in fnf[i]:
            G.add_edge(i, j)
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=700, node_color="skyblue",
            font_size=10, font_color="black", font_weight="bold", arrowsize=20)
    plt.savefig("graph" + str(num) + ".png")


if __name__ == "__main__":
    eq = ["xxy", "yyz", "xxz", "zyz"]
    A = "abcd"
    w = "baadcb"
    test(eq, A, w, num=0)  # test pierwszy

    eq = ["xx1", "yyz", "xxz", "wwv", "zyz", "vxv"]
    A = "abcdef"
    w = "acdcfbbe"
    test(eq, A, w, num=1)  # test drugi
