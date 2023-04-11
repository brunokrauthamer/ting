def exists_word(word, instance):
    queue_len = instance.__len__()
    occurances_info = []
    word_lower = word.lower()
    for i in range(queue_len):
        info = instance.search(i)
        lines = info["linhas_do_arquivo"]
        ocorrencias = []
        for index, line in enumerate(lines):
            line_lower = line.lower()
            if word_lower in line_lower:
                ocorrencias.append({"linha": index + 1})
        if bool(ocorrencias):
            dict_info = {
                "palavra": word,
                "arquivo": info["nome_do_arquivo"],
                "ocorrencias": ocorrencias
            }
            occurances_info.append(dict_info)
    return occurances_info


def search_by_word(word, instance):
    queue_len = instance.__len__()
    occurances_info = []
    word_lower = word.lower()
    for i in range(queue_len):
        info = instance.search(i)
        lines = info["linhas_do_arquivo"]
        ocorrencias = []
        for index, line in enumerate(lines):
            line_lower = line.lower()
            if word_lower in line_lower:
                ocorrencias.append({"linha": index + 1, "conteudo": line})
        if bool(ocorrencias):
            dict_info = {
                "palavra": word,
                "arquivo": info["nome_do_arquivo"],
                "ocorrencias": ocorrencias
            }
            occurances_info.append(dict_info)
    return occurances_info   
