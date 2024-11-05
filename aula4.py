
'''nivel - 1 ou 2
base = clientes 
etapa = ingestao ou extracao'''


def alerta(nivel, base, etapa):
        nivel = '1'
        base = 'clientes'
        etapa = 'ingestao'
        if nivel == 1 and etapa = ingestao:
        print(f"Alerta! Falha de carregamento na base clientes na etapa de ingestao!")
       return = alerta(1, clientes, ingestao)

def alerta(nivel, base, etapa):
    nivel = 1  # Mudei para um inteiro, se você quiser comparar como inteiro
    base = 'clientes'  # Usando uma string
    etapa = 'ingestao'  # Usando uma string
    
    # Verificando a condição
    if nivel == 1 and etapa == 'ingestao':
        print(f"Alerta! Falha de carregamento na base {base} na etapa de {etapa}!")
        
# Exemplo de uso
alerta(1, 'clientes', 'ingestao')