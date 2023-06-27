
''' Função usando palavra em portuques

função do pacote:

tuti.vogal_consoante(palavra)

return vogais, total_vogais, consoantes, total_consoantes

'''
def vogal_consoante(palavra):
    '''Quantidade de vogal e consoante'''
    vogais=[]
    consoantes=[]
    for letra in palavra:
        if letra in 'aeiouáâãàéêíóôõúü':
            vogais.append(letra)
        else:
            consoantes.append(letra)
        
    total_vogais = len(vogais)
    total_consoantes = len(consoantes)

    print("Vogais:", vogais)
    print("Total de vogais:", total_vogais)

    print("Consoantes:", consoantes)
    print("Total de consoantes:", total_consoantes)

    return vogais, total_vogais, consoantes, total_consoantes
