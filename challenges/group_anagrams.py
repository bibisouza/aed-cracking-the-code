def group_anagrams(words: list[str]) -> list[list[str]]:
    grupos = {}
    for palavra in words:
        chave = "".join(sorted(palavra))
        if chave not in grupos:
            grupos[chave] = []
        grupos[chave].append(palavra)
    return list(grupos.values())
