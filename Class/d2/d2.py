def manage_collaborators(NumCollaborators):
    if NumCollaborators == 0:
        try:
            with open('colaboradores.txt', 'r') as file:
                lines = file.readlines()
                for i in range(min(5, len(lines))):
                    print(lines[i].strip())
        except FileNotFoundError:
            print("El archivo 'colaboradores.txt' no existe.")
    else:
        if NumCollaborators <= 14:
            print("No puedes agregar tantos colaboradores.")
        else:
            with open('colaboradores.txt', 'a') as file:
                for i in range(NumCollaborators):
                    collaborator = input("Collaborator's name: ")
                    file.write(collaborator + '\n')
                    print(f"Collaborator '{collaborator}' added.")

                    if i == 14:
                        break

NumCollaborators = int(input("Ingresa el Numero de Colaboradores:🤵 "))
manage_collaborators(NumCollaborators)
