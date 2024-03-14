import csv
import json
import matplotlib.pyplot as plt

# Lendo o arquivo CSV
with open('ang.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Pula o cabeçalho
    data = {}
    for row in reader:
        # Converte a string em um dicionário
        angles = json.loads(row[1].replace("'", '"'))
        for key, value in angles.items():
            # Adiciona o valor ao dicionário de dados
            if key not in data:
                data[key] = []
            data[key].append(value)

for key, values in data.items():
    plt.figure()
    plt.plot(values)
    plt.title(key)
    
    # Encontra os índices do maior e do menor valor
    max_index = values.index(max(values))
    min_index = values.index(min(values))
    print(max(values), min(values), " " + key)
    # Marca o maior valor com um ponto vermelho
    plt.scatter(max_index, max(values), color='red')
    
    # Marca o menor valor com um ponto azul
    plt.scatter(min_index, min(values), color='blue')

    plt.savefig(f'graficos/{key}.png')

