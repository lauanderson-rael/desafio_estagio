def inverter_string(s):
    resultado = ''
    for char in s:
        resultado = char + resultado
    return resultado

string = input("Informe uma string: ")
print("String invertida:", inverter_string(string))
