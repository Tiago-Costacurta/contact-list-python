contacts = [ 
# {"name": "Tiago", 
#  "phone": "19845648", 
#  "email": "user@gmail.com", 
#  "favorite": "Não"},
# {"name": "José", 
#  "phone": "985956472848", 
#  "email": "user2@gmail.com", 
#  "favorite": "Sim"},
# {"name": "João", 
#  "phone": "298465798456", 
#  "email": "user3@gmail.com", 
#  "favorite": "Sim"}
]

def add_contact():
    name = input("\nDigite o nome do contato: ")
    phone = int(input("\nDigite o número do contato: "))
    email = input("\nDigite o e-mail do contato: ")
    favorite = input("\nDeseja marcar este contato como favorito? Digite S ou N: ")
    if favorite == "s" or favorite == "S":
        favorite = "Sim"
    else:
        favorite = "Não"
    contact = {"name": name, 
                "phone": phone, 
                "email": email, 
                "favorite": favorite}
    contacts.append(contact)
    if favorite == "Sim":
        print(f"O contato {name} foi adicionado a sua lista de contatos e está como favorito")
    else:
        print(f"O contato {name} foi adicionado a sua lista de contatos e não está como favorito")     
    return

def show_contacts():
    print("\n///////////////////////////////////////////////////////////////////////////////////////////")
    for index, contact in enumerate(contacts):
        name_contact = contact["name"]
        phone_contact = contact["phone"]
        email_contact = contact["email"]
        favorite_contact = contact["favorite"]
        index += 1
        print(f"{index}. {name_contact} - {phone_contact} - {email_contact} - Favorito: {favorite_contact}")
    print("///////////////////////////////////////////////////////////////////////////////////////////")
    
    return
def edit_contact():
    show_contacts()
    edit = int(input("Digite o número do contato que deseja editar: "))
    edit -= 1
    for index, contact in enumerate(contacts):
        if index == edit:
            change = 0
            while change != 4:    
                print("--------------------------------------")
                print("Editando contato")
                print("Digite 1 para editar nome")
                print("Digite 2 para editar telefone")
                print("Digite 3 para editar email")
                print("Digite 4 para finalizar")
                print("--------------------------------------")
                change = int(input("\nDigite a opção que deseja alterar: "))
                
                if change == 1:
                    contact["name"] = input("Digite o nome que deseja atribuir: ")
                elif change == 2:
                    contact["phone"] = int(input("Digite o número que deseja alterar: "))
                elif change == 3:
                    contact["email"] = input("Digite o e-mail que deseja alterar: ")
                elif change == 4:
                    return
                else:
                    print("Opção inválida")
            return
    return
def mark_favorite():
    show_contacts()
    edit = int(input("Digite o número do contato que deseja editar: "))
    edit -= 1
    for index, contact in enumerate(contacts):
        contact_name = contact["name"]
        if index == edit:
            if contact["favorite"] == "Não":
                contact["favorite"] = "Sim"
                print(f"\nO contato {contact_name} foi adicionado aos favoritos.")
                break
            else:
                contact["favorite"] = "Não"
                print(f"\nO contato {contact_name} foi removido dos favoritos.")
                break
    return

def show_favorites():
    for index, contact in enumerate(contacts):
        name_contact = contact["name"]
        phone_contact = contact["phone"]
        email_contact = contact["email"]
        favorite_contact = contact["favorite"]
        index += 1
        if contact["favorite"] == "Sim":
            print(f"{index}. {name_contact} - {phone_contact} - {email_contact} - Favorito: {favorite_contact}")
    return

def delete_contacts():
    show_contacts()
    edit = int(input("Digite o número do contato que deseja editar: "))
    edit -= 1
    for index, contact in enumerate(contacts):
        contact_name = contact["name"]
        if index == edit:
            print(f"\nO contato {contact_name} foi removido da lista de contatos.")
            contacts.remove(contact)
            return
    return