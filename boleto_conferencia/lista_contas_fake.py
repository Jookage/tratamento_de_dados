"""
Gera um arquivo TXT ficticio no layout esperado pelo script de
separacao debito/boleto (linhas com codigo de registro + agencia +
conta + nome + credito + debito + flag + tipo + sms).

Usa nomes, contas e valores 100% sinteticos. O codigo de registro usa
"999" (generico), diferente do codigo real do banco de producao -
ajuste a regex do script principal para casar com "999" ao rodar
localmente com este arquivo de teste.
"""

import random
from datetime import datetime, timedelta

ARQUIVO_SAIDA = "exemplo_fake_boleto.txt"
QTD_REGISTROS = 200
QTD_DIAS = 3

NOMES_FAKE = [
    "FULANO DA SILVA TESTE",
    "CICLANO DE SOUZA TESTE",
    "BELTRANO PEREIRA TESTE",
    "MARIA EXEMPLO SANTOS",
    "JOAO EXEMPLO OLIVEIRA",
    "ANA TESTE COSTA",
    "PEDRO TESTE ALMEIDA",
    "JULIA EXEMPLO LIMA",
]

TIPOS = ["DC", "DD"]  # DC = boleto (mantido), DD = debito (descartado pelo script)


def gerar_conta():
    return "".join(str(random.randint(0, 9)) for _ in range(16))


def gerar_agencia():
    return f"{random.randint(1, 999):03d}"


def gerar_valor():
    inteiro = random.randint(10, 9999)
    centavos = random.randint(0, 99)
    return f"{inteiro:,}".replace(",", ".") + f",{centavos:02d}"


def gerar_linha(nome):
    agencia = gerar_agencia()
    conta = gerar_conta()
    credito = gerar_valor()
    debito = "0,00"
    flag = random.choice(["S", "N"])
    tipo = random.choice(TIPOS)
    sms = random.choice(["S", "N"])

    # Codigo generico 999 no lugar do codigo real do banco
    return f"999 {agencia} {conta} {nome:<30} {credito} {debito} {flag} {tipo} {sms}\n"


def main():
    linhas = []
    data_base = datetime(2026, 1, 1)

    for d in range(QTD_DIAS):
        data_str = (data_base + timedelta(days=d)).strftime("%d/%m/%Y")
        linhas.append(f"DATA ARQ - {data_str}\n")

        for _ in range(QTD_REGISTROS // QTD_DIAS):
            nome = random.choice(NOMES_FAKE)
            linhas.append(gerar_linha(nome))

    with open(ARQUIVO_SAIDA, "w", encoding="latin1") as f:
        f.writelines(linhas)

    print(f"Arquivo gerado: {ARQUIVO_SAIDA} ({len(linhas)} linhas)")


if __name__ == "__main__":
    main()