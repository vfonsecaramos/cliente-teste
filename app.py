def saudacao(nome):
    """Devolve "Olá, {nome}!" se houver nome, ou apenas "Olá!" se nome for vazio ou None."""
    nome = (nome or "").strip()
    return f"Olá, {nome}!" if nome else "Olá!"
