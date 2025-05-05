import getpass
import json

def criar_utilizador():
    print("=== Criar Novo Utilizador ===")
    nome = input("Insira o nome de utilizador: ")

    # Oculta a password no terminal
    password = getpass.getpass("Insira a password: ")
    confirmar_password = getpass.getpass("Confirme a password: ")

    if password != confirmar_password:
        print("Erro: As passwords não coincidem.")
        return

    cargo = input("Insira o cargo do utilizador: ")
    acessos = input("Insira os acessos (ex: rede, VPN, etc.): ")
    permissoes = input("Insira as permissões (ex: leitura, escrita, admin): ")
    softwares = input("Insira os softwares que o utilizador irá usar (separados por vírgula): ")

    utilizador = {
        'nome': nome,
        'password': password,  # Em produção, deve-se usar hash
        'cargo': cargo,
        'acessos': acessos,
        'permissoes': permissoes,
        'softwares': [s.strip() for s in softwares.split(',')]
    }

    print("\nUtilizador criado com sucesso!")
    print(json.dumps(utilizador, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    criar_utilizador()
