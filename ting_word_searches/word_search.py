def exists_word(word, instance):
    list = []
    for item in instance._data:
        lines_found = []
        for line in item["linhas_do_arquivo"]:
            if word.lower() in line.lower():
                lines_found.append(
                    {
                        "linha": item["linhas_do_arquivo"].index(line),
                        "conteúdo": line,
                    }
                )
                print("lines_found")
        if len(lines_found) > 0:
            formatted_data = {
                "palavra": word,
                "arquivo": item["nome_do_arquivo"],
                "ocorrencias": lines_found,
            }
            list.append(formatted_data)
    return list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
