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
    # consultei
    # https://www.section.io/engineering-education/queue-data-structure-python/
    #  para suporte
    if len(instance) == 0:
        print("Não há elementos")
    else:
        file = instance.dequeue()
        name = file["nome_do_arquivo"]
        print(f"Arquivo {name} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
