charactersList = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def encrypt():
    code = input("Code: ")
    code = code.upper()
    result = []
    for i in range(len(charactersList) - 1):
        current = list(map( lambda y: y if (y not in charactersList) else charactersList[(charactersList.index(y) + i+1) % len(charactersList) ]
        , code ))
        result.append("".join(current))

    print(" ;\n\n".join(result))
    encrypt()

encrypt()