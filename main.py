from lista import ListaSE
from time import sleep
import os

lista = ListaSE()

def clear(print_header=True):
    os.system('cls' if os.name == 'nt' else 'clear')
    if print_header:
        print("=========== SISTEMA DE ORDENAÇÃO DE LISTA ===========")
        print("Lista atual: ", end="")
        if len(lista) == 0:
            print("vazia")
            print()
        else:
            lista.display()
            print()
            
def bubble_sort(lista, order):
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if order == "1":
                if lista.at(j) > lista.at(j+1):
                    temp = lista.at(j)
                    lista.change(j, lista.at(j+1))
                    lista.change(j+1, temp)
            elif order == "2":
                if lista.at(j) < lista.at(j+1):
                    temp = lista.at(j)
                    lista.change(j, lista.at(j+1))
                    lista.change(j+1, temp)
    
    clear()
    print("Lista ordenada:")
    lista.display()
    sleep(2)
    
def insertion_sort(lista, order):
    n = len(lista)
    
    for i in range(1, n):
        key = lista.at(i)
        j = i - 1
        
        if order == "1":
            while j >= 0 and lista.at(j) > key:
                lista.change(j + 1, lista.at(j))
                j -= 1
        elif order == "2":
            while j >= 0 and lista.at(j) < key:
                lista.change(j + 1, lista.at(j))
                j -= 1
        
        lista.change(j + 1, key)
    
    clear()
    print("Lista ordenada:")
    lista.display()
    sleep(2)
    
def quick_sort(lista, order):
    def partition(low, high):
        pivot = lista.at(high)
        i = low - 1
        
        for j in range(low, high):
            if order == "1":
                if lista.at(j) <= pivot:
                    i += 1
                    lista.change(i, lista.at(j))
            elif order == "2":
                if lista.at(j) >= pivot:
                    i += 1
                    lista.change(i, lista.at(j))
        
        lista.change(i + 1, lista.at(high))
        return i + 1
    
    def _quick_sort(low, high):
        if low < high:
            pi = partition(low, high)
            _quick_sort(low, pi - 1)
            _quick_sort(pi + 1, high)
    
    n = len(lista)
    _quick_sort(0, n - 1)
    
    clear()
    print("Lista ordenada:")
    lista.display()
    sleep(2)

while True:
    clear()
    
    if len(lista) == 0:
        n = input("Digite um número para iniciar a lista: ")
    else:
        choice = input("Deseja continuar a lista? [S/N] ")
        
        clear()
        
        if choice.upper() == "N":
            if len(lista) == 1:
                print("Você precisa de mais de um elemento para ordenar a lista!")
                sleep(1)
                continue
            else:
                clear(print_header=False)
                break
        elif choice.upper() == "S":
            n = input("Digite um número para continuar a lista: ")
        else:
            print("Opção inválida!")
            sleep(1)
            continue
        
    lista.insert(n)
    
while True:
    clear()
    
    print("Escolha um algoritmo de ordenação:")
    print("1 - Bubble Sort")
    print("2 - Insertion Sort")
    print("3 - Quick Sort")
    print("0 - Sair")

    alg_choice = input("-> ")
    
    clear()
    
    print("Deseja ordenar a lista de forma crescente ou decrescente?")
    print("1 - Crescente")
    print("2 - Decrescente")
    print("0 - Voltar")

    order_choice = input("-> ")
    
    clear()
    
    if order_choice == "0":
        continue
    
    if alg_choice == "1":
        bubble_sort(lista, order_choice)
    elif alg_choice == "2":
        insertion_sort(lista, order_choice)
    elif alg_choice == "3":
        quick_sort(lista, order_choice)
    
    choice = input("Deseja ordenar novamente? [S/N] ")
    
    if choice.upper() == "N":
        break
    elif choice.upper() == "S":
        continue
    else:
        clear()
        print("Opção inválida!")
        sleep(1)
        continue
        
    


        