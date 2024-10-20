import json

# um Exemplo do JSON
data = '''
{
    "faturamento": {
        "1": 100.0,
        "2": 200.0,
        "3": 150.0,
        "4": 0.0,
        "5": 250.0,
        "6": 0.0,
        "7": 300.0,
        "8": 100.0
    }
}
'''

faturamento = json.loads(data)['faturamento']

valores = [v for v in faturamento.values() if v > 0]
menor_faturamento = min(valores)
maior_faturamento = max(valores)
media_faturamento = sum(valores) / len(valores)
dias_acima_da_media = len([v for v in valores if v > media_faturamento])

print(f'Menor faturamento: R${menor_faturamento:.2f}')
print(f'Maior faturamento: R${maior_faturamento:.2f}')
print(f'Dias acima da média: {dias_acima_da_media}')
