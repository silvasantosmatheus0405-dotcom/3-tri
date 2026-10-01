def calcula_hash(senha):
    valor = 0
    for letra in senha:
        valor = valor + ord(letra)
    return valor

senha_cadastrada = "j03102003p"
hash_cadastrado = calcula_hash(senha_cadastrada)

print(hash_cadastrado)

senha_digitada = input("digite sua senha")
hash_digitado = calcula_hash(senha_digitada)

if hash_cadastrado == hash_digitado:
    print("acesso concedido")
else:
    print("senha incorreta")
