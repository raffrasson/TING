from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    queue = txt_importer(path_file)
    formatted_output = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(queue),
        "linhas_do_arquivo": queue,
    }
    for item in instance._data:
        if path_file == item["nome_do_arquivo"]:
            return None
    instance.enqueue(formatted_output)
    print(formatted_output)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
