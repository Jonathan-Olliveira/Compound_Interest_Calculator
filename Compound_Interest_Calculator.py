print("Bem vindo a calculadora de Juros compostos!")


initial_investment = float(input("Digite o valor do seu investimento inicial: "))
monthly_investment = float(input("Digite o valor do investimento que desejar fazer todos os meses: "))
annual_fee = float(input("Digite a taxa anual a.a: ")) / 1200
investment_time = int(input("Digite o periodo de tempo em anos que ficará esse investimento: ")) * 12
accumulated_amount = (monthly_investment * investment_time) + initial_investment

def calcular_juros_compostos():
    armazenar = float(0)
    for i in range(1, 2):
        armazenar += initial_investment
        print(f"o valor é do {i}ºmes é {armazenar:.2f}")
        for j in range(2, investment_time + 1):
            armazenar += monthly_investment
            armazenar = (armazenar * annual_fee) + armazenar
            print("o valor é do {}ºmes é {:.2f}".format(j, armazenar))
        accumulated_interest = armazenar - accumulated_amount
        print("")
        print("valor total investido R${}, total em juros de R${:.2f}".format(accumulated_amount, accumulated_interest))


calcular_juros_compostos()

# todo: adicionar exceção e tratamento de erros
# todo: implementar uma mini GUI
# todo: implementar novas funcionalidades