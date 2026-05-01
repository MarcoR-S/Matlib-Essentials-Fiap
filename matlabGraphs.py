import matplotlib.pyplot as plt
import numpy as np

def line():
    temp = [22, 25, 28, 32, 35, 34, 33, 31, 29, 27]
    horas = [1,2,3,4,5,6,7,8,9,10]

    plt.plot(horas,temp, label = "temperatura da máquina", marker = 'x')
    plt.xlabel("Horas")
    plt.ylabel("Temperatura")
    plt.title("Gráfico")
    plt.grid(True)
    plt.xticks(horas)
    plt.show()


def scatter():
    estudo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    notas = [2, 3, 5, 4, 7, 6, 8, 7, 9, 10]

    plt.scatter(estudo,notas, color = 'green', s=100)
    plt.xlabel("Estudo")
    plt.ylabel("Notas")
    plt.legend()
    plt.title("Notas e Estudos")
    plt.show()

def hist():
    idades = np.random.normal(30, 5, 500)
    plt.hist(idades, bins=30, color = 'cyan', edgecolor = 'black')
    plt.xlabel("Idades")
    plt.show()

def bar():
    vendedores = ['Ana', 'Beto', 'Caio', 'Duda']
    vendas = [15000, 18000, 12000, 22000]
    cores = ['red', 'green', 'cyan', 'yellow']
    plt.bar(vendedores, vendas, color = cores)
    plt.title("Vendas 2026")
    plt.xlabel("Vendedores")
    plt.ylabel("Vendas")
    plt.show()

def pizza():
    marcas = ['Marca A', 'Marca B', 'Outras']
    participacao = [45, 35, 20]
    cores = ['red', 'pink', 'blue']
    plt.pie(participacao, labels=marcas,colors=cores,autopct='%1.1f%%',explode=(0.1, 0, 0))
    plt.title("MARKETSHARE")
    plt.show()

if __name__ == "__main__":
    print("Escolha o gráfico: \n1-Linha\n2-Scatter\n3-Hist\n4-Bar\n5-Pizza")
    op = input("Digite o número: ")
    
    mapa = {"1": line, "2": scatter, "3": hist, "4": bar, "5": pizza}
    if op in mapa:
        mapa[op]()
    else:
        print("Opção inválida.")
























