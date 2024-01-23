import contact_book

option = 0

while option != 7:
    print("-----------------------------------------")
    print("1. Adicionar Contato")
    print("2. Listar Contato")
    print("3. editar Contatos")
    print("4. Marcar/desmarcar Contato como favorito")
    print("5. Listar Contatos favoritos")
    print("6. Apagar Contatos")
    print("7. Sair")
    print("-----------------------------------------")

    
    option = int(input("\nDigite a opção desejada: "))
    if option == 1:
        print("\n-------------------")
        print("|Adicionar contato|")
        print("-------------------")
        contact_book.add_contact()
    elif option == 2:
        print("\n------------------")
        print("|Listar Contatos|")
        print("------------------")
        contact_book.show_contacts()
    elif option == 3:
        print("\n------------------")
        print("Editar Contato")
        print("------------------")
        contact_book.edit_contact()
    elif option == 4:
        print("\n--------------------------------")
        print("|Marcar/desmarcar como favorito|")
        print("--------------------------------")
        contact_book.mark_favorite()
    elif option == 5:
        print("\n---------------------------")
        print("|Listar contatos Favoritos|")
        print("---------------------------")
        contact_book.show_favorites()
    elif option == 6:
        print("\n----------------")
        print("|Apagar contato|")
        print("----------------")
        contact_book.delete_contacts()
    elif option == 7:
        print("\n---------------------")
        print("|Encerrando programa|")
        print("---------------------")
    else:
        print("\n----------------------------")
        print("|Opção inválida, tente novamente|")
        print("----------------------------")
    
    