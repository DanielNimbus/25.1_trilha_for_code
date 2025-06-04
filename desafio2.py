id = 100
tupla_completa = [] #primeiro declarei como lista para poder fazer as modificações
tupla_computadores_funcionando = [] #idem


while 1:

    rodar = str(input("Quer adicionar um computador? (s ou n) - >"))
    if rodar == "n":
        break

    estado = int(input("O computador está funcionando? (1 = sim \ 0 = não)-> "))
    

    if estado == "": # caso o usuário não digite nada, pare
        break


    lista_pecas = []
    defeito = ""

    #só vai rodar a pergunta dos defeitos caso esteja com problema (usuario indicou 0)
    if estado == False:
        while 1:
            defeito = str(input("Peça com defeito -> "))
            # caso o usuário disse que não tem mais defeito, pula o append do "n"
            if defeito == "n":
                break
            lista_pecas.append(defeito)

    # transforma a lista de peças ruins em uma tupla 
    lista_pecas = tuple(lista_pecas)
    
    #dá append lá
    tupla_completa.append((id, estado, lista_pecas))

    # caso o computador esteja bom ele vai colocar também na lista dos bons
    if estado == 1:
        tupla_computadores_funcionando.append((id, estado, lista_pecas))

    id += 1

#transforma em tupla
tupla_completa = tuple(tupla_completa)
tupla_computadores_funcionando = tuple(tupla_computadores_funcionando)

# EOF
print("a tupla completa é ", tupla_completa)
print("a tupla só com os bons é ", tupla_computadores_funcionando)




