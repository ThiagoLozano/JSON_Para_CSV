# PROJETO PYTHON: Converter JSON para CSV

> Script que pega um arquivo JSON e converte para o formato CSV.

# Tecnologias Utilizadas

* **_VScode_**;

* **_Python3;_** 

# Bibliotecas e Configurações

### Bibliotecas Utilizadas

```python
import csv
import json
```

### Configurações

> O script foi feito com base na estrutura POO.

```python
class Conversor:
    def __init__(self):

usuario = Conversor()
```

# Arquivo JSON

```json
{
	"order": [
		{
			"id": 1,
			"name": "Camisa",
			"description": "Camisa Social Preta",
			"quantity": 3,
			"value": 56.50
		},
		{
			"id": 2,
			"name": "Regata",
			"description": "Regata 100% Algodão",
			"quantity": 6,
			"value": 9.99
		},
		{
			"id": 3,
			"name": "Saia Rodada",
			"description": "Saia Rodada Rosa",
			"quantity": 2,
			"value": 29.90
		},
		{
			"id": 4,
			"name": "Meia",
			"description": "Meia branca",
			"quantity": 3,
			"value": 5.00
		},
		{
			"id": 5,
			"name": "Gorro",
			"description": "Gorro Preto",
			"quantity": 1,
			"value": 12.00
		},
		{
			"id": 6,
			"name": "Moletom",
			"description": "Moletom Adidas",
			"quantity": 1,
			"value": 119.95
		},
		{
			"id": 7,
			"name": "Bermuda",
			"description": "Bermuda Ciclone",
			"quantity": 3,
			"value": 35.00
		},
		{
			"id": 8,
			"name": "Tênis",
			"description": "Tênis Nike Shox",
			"quantity": 1,
			"value": 450.00
		}
	]
}
```



### Leitura do JSON

```python
1. try:
2.   with open("./loja.json") as f:
3.      self.orders = json.load(f)
4.      self.Retorna_CSV()
5. except Exception as erro:
6.      print("Problema ao interpretar o arquivo JSON: {}".format(erro))
```

> Linha 1: Chama o Try
>
> Linha 2: Abre o arquivo JSON e coloca na variável __f__
>
> Linha 3: Cria uma variável que recebe o arquivo carregado como JSON.
>
> Linha 4: Chama a função __Retorna_CSV()__
>
> Linha 5: Cria uma exceção
>
> Linha 6: Retorna uma mensagem de erro na tela.

# Criar CSV

```python
1. def Retorna_CSV(self):
2.        # Cria o CSV.
3.        with open("json_to_csv.csv", "w") as f:
4.        columns = ['ID', 'Name', 'Description', 'Quantity', 'Value', 'Total']
5.        escrever = csv.DictWriter(f, fieldnames=columns, lineterminator='\n')
6.        escrever.writeheader()
7.
8.        # Pega cada objeto do pedido e insere no CSV.
9.        for order in self.orders['order']:
10.         id_order = order['id']
11.         name = order['name']
12.         description = order['description']
13.         quantity = order['quantity']
14.         value = order['value']
15.                
16.         # Escreve em cada linha.
17.         escrever.writerow({'ID': id_order, 'Name': name, 'Description': description, 'Quantity': quantity, 'Value': value})
```

> Linha 1: Cria a função __Retornar_CSV()__;
>
> Linha 3: Cria um arquivo CSV e coloca na variável __f__;
>
> Linha 4: Cria a coluna com cada nome;
>
> Linha 5: Configura  o arquivo  (Variável do arquivo, colunas, o fim da linha termina com uma quebra de linha)
>
> Linha 6: Escreve o cabeçalho da tabela.
>
> Linha 9: Cria um laço que passa pelo JSON
>
> Linha 10, 11, 12, 13, 14:  Cria uma variável que recebe os objetos específicos do JSON.
>
> Linha 17: Escreve em cada linha, inserindo cem cada Coluna os valores de cada variável. 

# CSV

| ID   | Name        | Description         | Quantity | Value  |
| ---- | ----------- | ------------------- | -------- | ------ |
| 1    | Camisa      | Camisa Social Preta | 3        | 56.5   |
| 2    | Regata      | Regata 100% Algodão | 6        | 9.99   |
| 3    | Saia Rodada | Saia Rodada Rosa    | 2        | 29.9   |
| 4    | Meia        | Meia branca         | 3        | 5.0    |
| 5    | Gorro       | Gorro Preto         | 1        | 12.0   |
| 6    | Moletom     | Moletom Adidas      | 1        | 119.95 |
| 7    | Bermuda     | Bermuda Ciclone     | 3        | 35.0   |
| 8    | Tênis       | Tênis Nike Shox     | 1        | 450.0  |

