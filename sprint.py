import json
import os
import csv
from datetime import datetime

ARQUIVO_BENEFICIARIOS = "beneficiarios.json"
ARQUIVO_DENTISTAS = "dentistas.json"
ARQUIVO_PEDIDOS = "pedidos_ajuda.json"
ARQUIVO_ATENDIMENTOS = "atendimentos.json"


# ===================== PERSISTÊNCIA =====================

def carregar_dados(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_dados(arquivo, lista):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)


# ===================== EXPORTAR / IMPORTAR JSON =====================

def exportar_json(lista, nome_sugerido):
    if len(lista) == 0:
        print("Nenhum dado cadastrado para exportar!")
        return
    nome_arq = input(f"Digite o nome do arquivo JSON (padrão: {nome_sugerido}): ").strip()
    if not nome_arq:
        nome_arq = nome_sugerido
    if not nome_arq.endswith(".json"):
        nome_arq += ".json"
    try:
        with open(nome_arq, "w", encoding="utf-8") as f:
            json.dump(lista, f, ensure_ascii=False, indent=4)
        print(f"Dados exportados com sucesso para '{nome_arq}'!")
    except Exception as e:
        print(f"Erro ao exportar: {e}")


def importar_json(lista, arquivo_padrao):
    nome_arq = input(f"Digite o nome do arquivo JSON (padrão: {arquivo_padrao}): ").strip()
    if not nome_arq:
        nome_arq = arquivo_padrao
    if not nome_arq.endswith(".json"):
        nome_arq += ".json"
    try:
        with open(nome_arq, "r", encoding="utf-8") as f:
            dados = json.load(f)
        lista.clear()
        lista.extend(dados)
        print(f"Dados importados com sucesso de '{nome_arq}'!")
    except FileNotFoundError:
        print(f"Arquivo '{nome_arq}' não encontrado.")
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON. Verifique se ele é válido.")
    except Exception as e:
        print(f"Erro ao importar: {e}")


# ===================== EXPORTAR CSV =====================

def exportar_beneficiarios_csv(beneficiarios):
    if len(beneficiarios) == 0:
        print("Nenhum beneficiário cadastrado para exportar!")
        return

    cabecalho = ['ID', 'CPF', 'Nome', 'Data Nascimento', 'Sexo', 'Programa Social',
                 'CEP', 'Logradouro', 'Cidade', 'Estado', 'Email', 'Telefone']

    with open('beneficiarios.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(cabecalho)
        for b in beneficiarios:
            writer.writerow([
                b['id'], b['cpf'], b['nome'], b['data_nasc'], b['sexo'],
                b['programa_social'], b['endereco']['cep'], b['endereco']['logradouro'],
                b['endereco']['cidade'], b['endereco']['estado'], b['email'], b['telefone']
            ])
    print("Beneficiários exportados com sucesso para 'beneficiarios.csv'!")


def exportar_dentistas_csv(dentistas):
    if len(dentistas) == 0:
        print("Nenhum dentista cadastrado para exportar!")
        return

    cabecalho = ['ID', 'CPF', 'Nome', 'Data Nascimento', 'Sexo', 'CRO',
                 'Especialidades', 'Disponibilidade', 'CEP', 'Logradouro',
                 'Cidade', 'Estado', 'Email', 'Telefone']

    with open('dentistas.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(cabecalho)
        for d in dentistas:
            writer.writerow([
                d['id'], d['cpf'], d['nome'], d['data_nasc'], d['sexo'],
                d['cro'], d['especialidades'], d['disponibilidade'],
                d['endereco']['cep'], d['endereco']['logradouro'],
                d['endereco']['cidade'], d['endereco']['estado'],
                d['email'], d['telefone']
            ])
    print("Dentistas exportados com sucesso para 'dentistas.csv'!")


def exportar_pedidos_csv(pedidos_ajuda):
    if len(pedidos_ajuda) == 0:
        print("Nenhum pedido de ajuda cadastrado para exportar!")
        return

    cabecalho = ['ID Pedido', 'ID Beneficiário', 'Nome', 'Sexo',
                 'Descrição', 'Email', 'Telefone', 'Data Criação']

    with open('pedidos_ajuda.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(cabecalho)
        for p in pedidos_ajuda:
            writer.writerow([
                p['id'],
                p['id_beneficiario'] if p['id_beneficiario'] else 'Não vinculado',
                p['nome'], p['sexo'], p['descricao'],
                p['email'], p['telefone'], p['data_criacao']
            ])
    print("Pedidos de ajuda exportados com sucesso para 'pedidos_ajuda.csv'!")


def exportar_atendimentos_csv(atendimentos):
    if len(atendimentos) == 0:
        print("Nenhum atendimento cadastrado para exportar!")
        return

    cabecalho = ['ID Dentista', 'Nome Dentista', 'ID Beneficiário',
                 'Nome Beneficiário', 'Descrição', 'Data Atendimento', 'Data Registro']

    with open('atendimentos.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(cabecalho)
        for a in atendimentos:
            writer.writerow([
                a['id_dentista'], a['dentista'], a['id_beneficiario'],
                a['beneficiario'], a['descricao'], a['data'], a['data_registro']
            ])
    print("Atendimentos exportados com sucesso para 'atendimentos.csv'!")


# ===================== MAIN =====================

def main():
    beneficiarios = carregar_dados(ARQUIVO_BENEFICIARIOS)
    dentistas = carregar_dados(ARQUIVO_DENTISTAS)
    pedidos_ajuda = carregar_dados(ARQUIVO_PEDIDOS)
    atendimentos = carregar_dados(ARQUIVO_ATENDIMENTOS)

    while True:
        print("\n=== Menu Principal ===")
        print("1 - Beneficiário")
        print("2 - Dentista")
        print("3 - Pedido de Ajuda")
        print("4 - Registrar Atendimento")
        print("5 - Importar / Exportar dados")
        print("6 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            while True:
                print("\n--- Beneficiário ---")
                print("1 - Inserir beneficiário")
                print("2 - Alterar beneficiário")
                print("3 - Excluir beneficiário")
                print("4 - Exibir beneficiário")
                print("5 - Voltar")

                opcao = input("Escolha: ")

                if opcao == "1":
                    inserir_beneficiario(beneficiarios)
                    salvar_dados(ARQUIVO_BENEFICIARIOS, beneficiarios)

                elif opcao == "2":
                    cpf_alterar = input("Digite o CPF do beneficiário que deseja alterar: ")
                    indice = buscar_beneficiario_cpf(beneficiarios, cpf_alterar)
                    if indice != -1:
                        alterar_beneficiario(beneficiarios, indice)
                        salvar_dados(ARQUIVO_BENEFICIARIOS, beneficiarios)
                    else:
                        print("Beneficiário não encontrado!")

                elif opcao == "3":
                    cpf_excluir = input("Digite o CPF do beneficiário que deseja excluir: ")
                    indice = buscar_beneficiario_cpf(beneficiarios, cpf_excluir)
                    if indice != -1:
                        excluir_beneficiario(beneficiarios, indice)
                        salvar_dados(ARQUIVO_BENEFICIARIOS, beneficiarios)
                    else:
                        print("Beneficiário não encontrado!")

                elif opcao == "4":
                    cpf_exibir = input("Digite o CPF do beneficiário que deseja exibir: ")
                    indice = buscar_beneficiario_cpf(beneficiarios, cpf_exibir)
                    if indice != -1:
                        exibir_beneficiario(beneficiarios, indice)
                    else:
                        print("Beneficiário não encontrado!")

                elif opcao == "5":
                    break

                else:
                    print("Opção inválida.")

        elif escolha == "2":
            while True:
                print("\n--- Dentista ---")
                print("1 - Inserir dentista")
                print("2 - Alterar dentista")
                print("3 - Excluir dentista")
                print("4 - Exibir dentista")
                print("5 - Voltar")

                opcao = input("Escolha: ")

                if opcao == "1":
                    inserir_dentista(dentistas)
                    salvar_dados(ARQUIVO_DENTISTAS, dentistas)

                elif opcao == "2":
                    cpf_alterar = input("Digite o CPF do dentista que deseja alterar: ")
                    indice = buscar_dentista_cpf(dentistas, cpf_alterar)
                    if indice != -1:
                        alterar_dentista(dentistas, indice)
                        salvar_dados(ARQUIVO_DENTISTAS, dentistas)
                    else:
                        print("Dentista não encontrado!")

                elif opcao == "3":
                    cpf_excluir = input("Digite o CPF do dentista que deseja excluir: ")
                    indice = buscar_dentista_cpf(dentistas, cpf_excluir)
                    if indice != -1:
                        excluir_dentista(dentistas, indice)
                        salvar_dados(ARQUIVO_DENTISTAS, dentistas)
                    else:
                        print("Dentista não encontrado!")

                elif opcao == "4":
                    cpf_exibir = input("Digite o CPF do dentista que deseja exibir: ")
                    indice = buscar_dentista_cpf(dentistas, cpf_exibir)
                    if indice != -1:
                        exibir_dentista(dentistas, indice)
                    else:
                        print("Dentista não encontrado!")

                elif opcao == "5":
                    break

                else:
                    print("Opção inválida.")

        elif escolha == "3":
            while True:
                print("\n--- Pedido de Ajuda ---")
                print("1 - Registrar pedido de ajuda")
                print("2 - Exibir pedido de ajuda")
                print("3 - Voltar")

                opcao = input("Escolha: ")

                if opcao == "1":
                    registrar_pedido_ajuda(pedidos_ajuda)
                    salvar_dados(ARQUIVO_PEDIDOS, pedidos_ajuda)

                elif opcao == "2":
                    id_exibir = input("Digite o ID do pedido que deseja exibir: ")
                    indice = buscar_pedido_id(pedidos_ajuda, id_exibir)
                    if indice != -1:
                        exibir_pedido(pedidos_ajuda, indice)
                    else:
                        print("Pedido não encontrado!")

                elif opcao == "3":
                    break

                else:
                    print("Opção inválida.")

        elif escolha == "4":
            registrar_atendimento(dentistas, beneficiarios, atendimentos)
            salvar_dados(ARQUIVO_ATENDIMENTOS, atendimentos)

        elif escolha == "5":
            while True:
                print("\n--- Importar / Exportar Dados ---")
                print("1 - Exportar dados para JSON")
                print("2 - Importar dados de JSON")
                print("3 - Exportar dados para CSV")
                print("4 - Voltar")

                opcao = input("Escolha: ")

                if opcao == "1":
                    while True:
                        print("\n  Exportar JSON:")
                        print("  1 - Beneficiários")
                        print("  2 - Dentistas")
                        print("  3 - Pedidos de Ajuda")
                        print("  4 - Atendimentos")
                        print("  5 - Voltar")

                        sub = input("  Escolha: ")

                        if sub == "1":
                            exportar_json(beneficiarios, ARQUIVO_BENEFICIARIOS)
                        elif sub == "2":
                            exportar_json(dentistas, ARQUIVO_DENTISTAS)
                        elif sub == "3":
                            exportar_json(pedidos_ajuda, ARQUIVO_PEDIDOS)
                        elif sub == "4":
                            exportar_json(atendimentos, ARQUIVO_ATENDIMENTOS)
                        elif sub == "5":
                            break
                        else:
                            print("Opção inválida.")

                elif opcao == "2":
                    while True:
                        print("\n  Importar JSON:")
                        print("  1 - Beneficiários")
                        print("  2 - Dentistas")
                        print("  3 - Pedidos de Ajuda")
                        print("  4 - Atendimentos")
                        print("  5 - Voltar")

                        sub = input("  Escolha: ")

                        if sub == "1":
                            importar_json(beneficiarios, ARQUIVO_BENEFICIARIOS)
                            salvar_dados(ARQUIVO_BENEFICIARIOS, beneficiarios)
                        elif sub == "2":
                            importar_json(dentistas, ARQUIVO_DENTISTAS)
                            salvar_dados(ARQUIVO_DENTISTAS, dentistas)
                        elif sub == "3":
                            importar_json(pedidos_ajuda, ARQUIVO_PEDIDOS)
                            salvar_dados(ARQUIVO_PEDIDOS, pedidos_ajuda)
                        elif sub == "4":
                            importar_json(atendimentos, ARQUIVO_ATENDIMENTOS)
                            salvar_dados(ARQUIVO_ATENDIMENTOS, atendimentos)
                        elif sub == "5":
                            break
                        else:
                            print("Opção inválida.")

                elif opcao == "3":
                    while True:
                        print("\n  Exportar CSV:")
                        print("  1 - Beneficiários")
                        print("  2 - Dentistas")
                        print("  3 - Pedidos de Ajuda")
                        print("  4 - Atendimentos")
                        print("  5 - Voltar")

                        sub = input("  Escolha: ")

                        if sub == "1":
                            exportar_beneficiarios_csv(beneficiarios)
                        elif sub == "2":
                            exportar_dentistas_csv(dentistas)
                        elif sub == "3":
                            exportar_pedidos_csv(pedidos_ajuda)
                        elif sub == "4":
                            exportar_atendimentos_csv(atendimentos)
                        elif sub == "5":
                            break
                        else:
                            print("Opção inválida.")

                elif opcao == "4":
                    break

                else:
                    print("Opção inválida.")

        elif escolha == "6":
            print("Sistema encerrado. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")


# ===================== BENEFICIÁRIO =====================

def buscar_beneficiario_cpf(beneficiarios, cpf):
    indice = -1
    for i in range(len(beneficiarios)):
        if beneficiarios[i]['cpf'] == cpf:
            indice = i
    return indice


def gerar_id_beneficiario(beneficiarios):
    if len(beneficiarios) == 0:
        return 1
    return max(b['id'] for b in beneficiarios) + 1


def inserir_beneficiario(beneficiarios):
    try:
        cpf = input("CPF: ")
        indice = buscar_beneficiario_cpf(beneficiarios, cpf)
        while indice != -1:
            cpf = input("CPF já cadastrado. Digite outro CPF: ")
            indice = buscar_beneficiario_cpf(beneficiarios, cpf)
        nome = input("Nome completo: ")
        data_nasc = input("Data de nascimento (DD/MM/AAAA): ")
        sexo = input("Sexo: ")
        programa_social = input("Programa social: ")
        cep = input("CEP: ")
        logradouro = input("Logradouro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
    except ValueError:
        print("Erro: verifique os dados informados.")
    else:
        id_novo = gerar_id_beneficiario(beneficiarios)
        beneficiario = {
            'id': id_novo,
            'cpf': cpf,
            'nome': nome,
            'data_nasc': data_nasc,
            'sexo': sexo,
            'programa_social': programa_social,
            'endereco': {
                'cep': cep,
                'logradouro': logradouro,
                'cidade': cidade,
                'estado': estado
            },
            'email': email,
            'telefone': telefone
        }
        beneficiarios.append(beneficiario)
        print(f"Beneficiário cadastrado com sucesso! ID: {id_novo}")


def alterar_beneficiario(beneficiarios, indice):
    try:
        print(f"Nome: {beneficiarios[indice]['nome']}")
        nome = input("Novo nome completo: ")
        print(f"Data de nascimento: {beneficiarios[indice]['data_nasc']}")
        data_nasc = input("Nova data de nascimento (DD/MM/AAAA): ")
        print(f"Sexo: {beneficiarios[indice]['sexo']}")
        sexo = input("Novo sexo: ")
        print(f"Programa social: {beneficiarios[indice]['programa_social']}")
        programa_social = input("Novo programa social: ")
        print(f"CEP: {beneficiarios[indice]['endereco']['cep']}")
        cep = input("Novo CEP: ")
        print(f"Logradouro: {beneficiarios[indice]['endereco']['logradouro']}")
        logradouro = input("Novo logradouro: ")
        print(f"Cidade: {beneficiarios[indice]['endereco']['cidade']}")
        cidade = input("Nova cidade: ")
        print(f"Estado: {beneficiarios[indice]['endereco']['estado']}")
        estado = input("Novo estado: ")
        print(f"Email: {beneficiarios[indice]['email']}")
        email = input("Novo email: ")
        print(f"Telefone: {beneficiarios[indice]['telefone']}")
        telefone = input("Novo telefone: ")
    except ValueError:
        print("Erro: verifique os dados informados.")
    else:
        beneficiarios[indice]['nome'] = nome
        beneficiarios[indice]['data_nasc'] = data_nasc
        beneficiarios[indice]['sexo'] = sexo
        beneficiarios[indice]['programa_social'] = programa_social
        beneficiarios[indice]['endereco']['cep'] = cep
        beneficiarios[indice]['endereco']['logradouro'] = logradouro
        beneficiarios[indice]['endereco']['cidade'] = cidade
        beneficiarios[indice]['endereco']['estado'] = estado
        beneficiarios[indice]['email'] = email
        beneficiarios[indice]['telefone'] = telefone
        print("Beneficiário alterado com sucesso!")


def excluir_beneficiario(beneficiarios, indice):
    beneficiarios.pop(indice)
    print("Beneficiário excluído com sucesso!")


def exibir_beneficiario(beneficiarios, indice):
    b = beneficiarios[indice]
    print(f"ID: {b['id']}")
    print(f"CPF: {b['cpf']}")
    print(f"Nome: {b['nome']}")
    print(f"Data de nascimento: {b['data_nasc']}")
    print(f"Sexo: {b['sexo']}")
    print(f"Programa social: {b['programa_social']}")
    print(f"Endereço:")
    print(f"  CEP: {b['endereco']['cep']}")
    print(f"  Logradouro: {b['endereco']['logradouro']}")
    print(f"  Cidade: {b['endereco']['cidade']}")
    print(f"  Estado: {b['endereco']['estado']}")
    print(f"Email: {b['email']}")
    print(f"Telefone: {b['telefone']}")


# ===================== DENTISTA =====================

def buscar_dentista_cpf(dentistas, cpf):
    indice = -1
    for i in range(len(dentistas)):
        if dentistas[i]['cpf'] == cpf:
            indice = i
    return indice


def gerar_id_dentista(dentistas):
    if len(dentistas) == 0:
        return 1
    return max(d['id'] for d in dentistas) + 1


def inserir_dentista(dentistas):
    try:
        cpf = input("CPF: ")
        indice = buscar_dentista_cpf(dentistas, cpf)
        while indice != -1:
            cpf = input("CPF já cadastrado. Digite outro CPF: ")
            indice = buscar_dentista_cpf(dentistas, cpf)
        nome = input("Nome completo: ")
        data_nasc = input("Data de nascimento (DD/MM/AAAA): ")
        sexo = input("Sexo: ")
        cro = input("CRO: ")
        especialidades = input("Especialidades: ")
        disponibilidade = input("Disponibilidade: ")
        cep = input("CEP: ")
        logradouro = input("Logradouro: ")
        cidade = input("Cidade: ")
        estado = input("Estado: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
    except ValueError:
        print("Erro: verifique os dados informados.")
    else:
        id_novo = gerar_id_dentista(dentistas)
        dentista = {
            'id': id_novo,
            'cpf': cpf,
            'nome': nome,
            'data_nasc': data_nasc,
            'sexo': sexo,
            'cro': cro,
            'especialidades': especialidades,
            'disponibilidade': disponibilidade,
            'endereco': {
                'cep': cep,
                'logradouro': logradouro,
                'cidade': cidade,
                'estado': estado
            },
            'email': email,
            'telefone': telefone
        }
        dentistas.append(dentista)
        print(f"Dentista cadastrado com sucesso! ID: {id_novo}")


def alterar_dentista(dentistas, indice):
    try:
        print(f"Nome: {dentistas[indice]['nome']}")
        nome = input("Novo nome completo: ")
        print(f"Data de nascimento: {dentistas[indice]['data_nasc']}")
        data_nasc = input("Nova data de nascimento (DD/MM/AAAA): ")
        print(f"Sexo: {dentistas[indice]['sexo']}")
        sexo = input("Novo sexo: ")
        print(f"CRO: {dentistas[indice]['cro']}")
        cro = input("Novo CRO: ")
        print(f"Especialidades: {dentistas[indice]['especialidades']}")
        especialidades = input("Novas especialidades: ")
        print(f"Disponibilidade: {dentistas[indice]['disponibilidade']}")
        disponibilidade = input("Nova disponibilidade: ")
        print(f"CEP: {dentistas[indice]['endereco']['cep']}")
        cep = input("Novo CEP: ")
        print(f"Logradouro: {dentistas[indice]['endereco']['logradouro']}")
        logradouro = input("Novo logradouro: ")
        print(f"Cidade: {dentistas[indice]['endereco']['cidade']}")
        cidade = input("Nova cidade: ")
        print(f"Estado: {dentistas[indice]['endereco']['estado']}")
        estado = input("Novo estado: ")
        print(f"Email: {dentistas[indice]['email']}")
        email = input("Novo email: ")
        print(f"Telefone: {dentistas[indice]['telefone']}")
        telefone = input("Novo telefone: ")
    except ValueError:
        print("Erro: verifique os dados informados.")
    else:
        dentistas[indice]['nome'] = nome
        dentistas[indice]['data_nasc'] = data_nasc
        dentistas[indice]['sexo'] = sexo
        dentistas[indice]['cro'] = cro
        dentistas[indice]['especialidades'] = especialidades
        dentistas[indice]['disponibilidade'] = disponibilidade
        dentistas[indice]['endereco']['cep'] = cep
        dentistas[indice]['endereco']['logradouro'] = logradouro
        dentistas[indice]['endereco']['cidade'] = cidade
        dentistas[indice]['endereco']['estado'] = estado
        dentistas[indice]['email'] = email
        dentistas[indice]['telefone'] = telefone
        print("Dentista alterado com sucesso!")


def excluir_dentista(dentistas, indice):
    dentistas.pop(indice)
    print("Dentista excluído com sucesso!")


def exibir_dentista(dentistas, indice):
    d = dentistas[indice]
    print(f"ID: {d['id']}")
    print(f"CPF: {d['cpf']}")
    print(f"Nome: {d['nome']}")
    print(f"Data de nascimento: {d['data_nasc']}")
    print(f"Sexo: {d['sexo']}")
    print(f"CRO: {d['cro']}")
    print(f"Especialidades: {d['especialidades']}")
    print(f"Disponibilidade: {d['disponibilidade']}")
    print(f"Endereço:")
    print(f"  CEP: {d['endereco']['cep']}")
    print(f"  Logradouro: {d['endereco']['logradouro']}")
    print(f"  Cidade: {d['endereco']['cidade']}")
    print(f"  Estado: {d['endereco']['estado']}")
    print(f"Email: {d['email']}")
    print(f"Telefone: {d['telefone']}")


# ===================== PEDIDO DE AJUDA =====================

def buscar_pedido_id(pedidos_ajuda, id_pedido):
    indice = -1
    for i in range(len(pedidos_ajuda)):
        if str(pedidos_ajuda[i]['id']) == str(id_pedido):
            indice = i
    return indice


def gerar_id_pedido(pedidos_ajuda):
    if len(pedidos_ajuda) == 0:
        return 1
    return max(p['id'] for p in pedidos_ajuda) + 1


def registrar_pedido_ajuda(pedidos_ajuda):
    try:
        id_beneficiario = input("ID do beneficiário (deixe em branco se ainda não cadastrado): ")
        nome = input("Nome completo: ")
        sexo = input("Sexo: ")
        descricao = input("Descrição do problema: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
    except ValueError:
        print("Erro: verifique os dados informados.")
    else:
        id_novo = gerar_id_pedido(pedidos_ajuda)
        pedido = {
            'id': id_novo,
            'id_beneficiario': id_beneficiario if id_beneficiario else None,
            'nome': nome,
            'sexo': sexo,
            'descricao': descricao,
            'email': email,
            'telefone': telefone,
            'data_criacao': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        pedidos_ajuda.append(pedido)
        print(f"Pedido de ajuda registrado com sucesso! ID do pedido: {id_novo}")


def exibir_pedido(pedidos_ajuda, indice):
    p = pedidos_ajuda[indice]
    print(f"ID do pedido: {p['id']}")
    print(f"ID do beneficiário: {p['id_beneficiario'] if p['id_beneficiario'] else 'Não vinculado'}")
    print(f"Nome: {p['nome']}")
    print(f"Sexo: {p['sexo']}")
    print(f"Descrição: {p['descricao']}")
    print(f"Email: {p['email']}")
    print(f"Telefone: {p['telefone']}")
    print(f"Data de criação: {p['data_criacao']}")


# ===================== ATENDIMENTO =====================

def registrar_atendimento(dentistas, beneficiarios, atendimentos):
    try:
        cpf_dentista = input("CPF do dentista: ")
        cpf_beneficiario = input("CPF do beneficiário: ")

        dentista_encontrado = None
        beneficiario_encontrado = None

        for d in dentistas:
            if d['cpf'] == cpf_dentista:
                dentista_encontrado = d
        for b in beneficiarios:
            if b['cpf'] == cpf_beneficiario:
                beneficiario_encontrado = b

        if not dentista_encontrado or not beneficiario_encontrado:
            print("Dentista ou beneficiário não encontrados.")
            return

        descricao = input("Descrição do atendimento: ")
        data = input("Data do atendimento (DD/MM/AAAA): ")
    except ValueError:
        print("Erro: verifique os dados informados.")
    else:
        atendimento = {
            'id_dentista': dentista_encontrado['id'],
            'dentista': dentista_encontrado['nome'],
            'id_beneficiario': beneficiario_encontrado['id'],
            'beneficiario': beneficiario_encontrado['nome'],
            'descricao': descricao,
            'data': data,
            'data_registro': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        atendimentos.append(atendimento)
        print("Atendimento registrado com sucesso!")


if __name__ == "__main__":
    main()