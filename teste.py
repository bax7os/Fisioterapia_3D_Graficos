import csv
import matplotlib.pyplot as plt
import os

# Cria uma pasta para salvar os gráficos
os.makedirs('graficos', exist_ok=True)

# Lendo o arquivo TSV
with open('ang.tsv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')  # Use '\t' como delimitador
    data = {}
    for row in reader:
        for i in range(1, len(row), 2):  # Começa em 1 e pula de dois em dois
            # Extrai a chave e o valor
            key = row[i].strip(': ')
            value = float(row[i+1])
            
            # Adiciona o valor ao dicionário de dados
            if key not in data:
                data[key] = []
            data[key].append(value)

# Cria um gráfico para cada conjunto de dados
for key, values in data.items():
    plt.figure()
    plt.plot(values)
    plt.title(key)
    
    # Encontra os índices do maior e do menor valor
    max_index = values.index(max(values))
    min_index = values.index(min(values))
    
    # Marca o maior valor com um ponto vermelho
    plt.scatter(max_index, max(values), color='red')
    
    # Marca o menor valor com um ponto azul
    plt.scatter(min_index, min(values), color='blue')
    print(max(values), min(values), " " + key)
    # Salva o gráfico na pasta 'graficos'
    plt.savefig(f'graficos/{key}.png')
    
    plt.close()  # Fecha a figura atual
