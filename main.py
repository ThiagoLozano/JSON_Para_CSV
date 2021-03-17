import csv
import json

class Conexao:
    # Método construtor.
    def __init__(self):
        # Abre o arquivo JSON.
        try:
            with open("./loja.json") as f:
                self.orders = json.load(f)
            self.Retorna_CSV()
        except Exception as erro:
            print("Erro: {}".format(erro))
            
    # Metodo que retorna o CSV.
    def Retorna_CSV(self):
        # Cria o CSV.
        with open("json_to_csv.csv", "w") as f:
            columns = ['ID', 'Name', 'Description', 'Quantity', 'Value', 'Total']
            escrever = csv.DictWriter(f, fieldnames=columns, lineterminator='\n')
            escrever.writeheader()

            # Pega cada objeto do pedido e insere no CSV.
            for order in self.orders['order']:
                id_order = order['id']
                name = order['name']
                description = order['description']
                quantity = order['quantity']
                value = order['value']
                
                # Escreve em cada linha.
                escrever.writerow({'ID': id_order, 'Name': name, 'Description': description, 'Quantity': quantity, 'Value': value})

usuario = Conexao()
