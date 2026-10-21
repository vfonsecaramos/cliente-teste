def saudacao(nome):
    nome = (nome or "").strip()
    return f"Olá, {nome}!" if nome else "Olá!"
