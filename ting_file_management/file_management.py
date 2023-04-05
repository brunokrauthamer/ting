import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        sys.stderr.write('Formato inválido')
    try:
        with open(path_file) as file:
            data = []
            for line in file:
                trated_line = line.replace('\n', '')
                data.append(trated_line)
        print(data)
        return data
    except FileNotFoundError:
        sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
