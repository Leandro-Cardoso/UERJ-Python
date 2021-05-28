import matplotlib.pyplot as plt

# Functions:
def open_data(data_file, separator = ','):
    ''' Retorna listas de dados separados pelo parâmetro "separator". '''
    lines = open(data_file).readlines()
    return [line.strip().lower().split(separator) for line in lines]

def create_list(data, item):
    ''' Retorna uma lista a partir dos dados do parâmetro "data", de um item em especifico informado no parâmetro "item". '''
    item = item.strip().lower()
    if item in data[0]:
        new_list = []
        position = data[0].index(item)
        for i in data:
            new_list.append(i[position])
        return new_list[1:]
    else:
        return 'Não existe dados sobre este item.'

def plot_histogram(title, data_list, color, bins = 10):
    ''' Cria um histograma com titulo, dados, cor e número de intervalos. '''
    plt.title(title)
    plt.hist(data_list, bins = bins, color = color)
    plt.grid(True)
    plt.show()

# Parameters:
data = open_data('dados_alunos.txt')
idade = create_list(data, 'idade')
altura = create_list(data, 'altura')
peso = create_list(data, 'peso')

# Results:
print('\nDados:', data, '\n')
print('Idades: ', idade, '\n')
print('Alturas: ', altura, '\n')
print('Pesos: ', peso, '\n')

# Plot:
plot_histogram('Frequência x Idade', idade, 'red')
plot_histogram('Frequência x Altura', altura, 'green')
plot_histogram('Frequência x Peso', peso, 'blue')
