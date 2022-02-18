nome = input("Informe o usuário: ")
senha = input("Informe a senha: ")
while nome == senha:
    print("Nome de usuário e senha devem ser diferentes.")
    nome = input("Informe o usuário: ")
    senha = input("Informe a senha: ")