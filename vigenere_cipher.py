import matplotlib.pyplot as plt

WESTALPHABET = "abcdefghijklmnopqrstuvwxyz"

# Classe base para algoritmos criptgraficos
class CryptAlgorithm(object):
    def __init__(self, alphabet = WESTALPHABET):
        self.alphabet = alphabet

    # Inverte a tabela monoalfabetica (tabela de tradução)
    def invertMonoAlphabetic(self, key):
        asciiCode = ord('a')
        n = 0
        keyList = list(self.alphabet)

        for character in key:
            keyList[ord(character) - asciiCode] = chr(asciiCode + n)
            n += 1

        # Junta todos os itens da lista em uma string usando '' como separador
        return string.join(keyList, '')

# Vigenere algoritmo de incriptar e decriptar
class Vigenere(CryptAlgorithm):
    def __init__(self, key, alphabet = WESTALPHABET):
        self.alphabet = alphabet
        self.sizeAlphabet = len(alphabet)
        self.key = key
        self.sizeKey = len(key)
        self.asciiCode = ord("a")

    # Encriptar texto
    def encrypt(self, text):
        message = ""
        i = 0

        for character in string2Crypt(text):
            message += self.alphabet[((ord(character) - self.asciiCode) + (ord(self.key[i%self.sizeKey]) - self.asciiCode)) % self.sizeAlphabet]
            i += 1

        return message

    # Decriptar texto
    def decrypt(self, text):
        message = ""
        i = 0
        newKey = self.invertMonoAlphabetic(self.alphabet)

        for character in text:
            message += chr((((ord(newKey[ord(character)-self.asciiCode]) - self.asciiCode) - (ord(self.key[i%self.sizeKey]) - self.asciiCode)) % self.sizeAlphabet) + self.asciiCode)
            i +=1

        return message

# Converte uma string para um Criptograma
def string2Crypt(text):
    cryptogram = ""

    for character in text:
        cryptogram += characterFilter(character)

    return cryptogram

# Filtra caracteres para uma contagem adicional
def characterFilter(character):
    if character in ACCENTS:
        return ACCENTS[character]
    # string.uppercase é uma string que contem todos os caracteres maiusculos
    elif character in string.uppercase:
        return characterFilter(string.lower(character))
    # string.lowercase é uma string que contem todos os caracteres minusculas
    elif character in string.lowercase:
        return character
    else:
        return ""

# Numero total de cada caracter no texto 
def numberCharacters(text):
    letterCount = []
    index = 0

    while index < len(WESTALPHABET):
        count = 0

        for letter in text:
            if letter == WESTALPHABET[index]:
                count += 1

        index += 1
        letterCount.append(count)

    for i in range(0, len(letterCount)):
        print(WESTALPHABET[i], '=', ((letterCount[i] * 1.0) / (len(text) * 1.0) * 100), '%')

# Função para ver a periodicidade
def textPeriodicity(text):
    periodicity = []

    for i in range(2,50):
        tempResult = []
        sumResults = 0
        division  = textDivision(text, i)

        for j in range(0, i):
            coincidence = coincidenceIndex(division[j])
            tempResult.append(coincidence)

        for k in range(0, len(tempResult)):
            sumResults += tempResult[k]

        periodicity.append(sumResults/i)
        sumResults = 0

    xAxis = range(2,50)

    # Criação de gradico de pontos
    # scatter(x = xAxiz, y = periodicity, LABEL, color = cor, marker = estilo do marcador, s = area do marker)
    plt.scatter(xAxis, periodicity, label = "stars", color = "green", marker = "*", s = 50)
    # Eixo do X
    plt.xlabel('Index of Division')
    # Eixo do Y
    plt.ylabel('Periodicity')  
    # Função que mostra o grafico
    plt.show()

# Divide o texto em um numero de periodicidade
def textDivision(text, number):
    textDivision = []
    i = 0

    for character in text:
        i = i % number
        textDivision[i] += character
        i += 1

    return textDivision

# Indice de Coincidencia
def coincidenceIndex(text):
    letters = ' -ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letterCount = []
    aux1 = 0
    aux2 = 0
    index = 0

    while aux1 < len(letters):
        count = 0

        for character in text:
            if character == letters[aux1]:
                count += 1

        aux1 += 1
        letterCount.append(count)

    while aux2 < len(letters):
        index += letterCount[aux2] * (letterCount[aux2] - 1)
        aux2 += 1

    index = float(index)
    denominator = float(len(text) * (len(text) - 1))
    coincidence = index / denominator

    return coincidence

print('***** VIGENERE CIPHER *****')
text = input()
option = input('Do you want to encrypt or decrypt the text? (E/D) -> ')

# ord('x') dá o codigo ASCII do caracter 'x'
if ord(option) == 69:
    alphabetKey = input('Key: ')
    key = Vigenere(alphabetKey)

    print(key.encrypt(text))
elif ord(option) == 68:
    textPeriodicity(text)
    indexDivision = input('You want to divide the text to which value? ')
    division = textDivision(text, indexDivision)

    for i in range (0, indexDivision):
        numberCharacters(division[i])

    alphabetKey = input('Key: ')
    key = Vigenere(alphabetKey)

    print(key.decrypt(text))
else:
    print('You did not chose any of the option sorry!! :(')