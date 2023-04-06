from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    length = instance.__len__()
    for i in range(length):
        data = instance.search(i)
        if data["nome_do_arquivo"] == path_file:
            return None
    file_list = txt_importer(path_file)
    file_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_list),
        "linhas_do_arquivo": file_list
    }
    instance.enqueue(file_info)
    sys.stdout.write(str(file_info))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
