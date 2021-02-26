import string

WESTALPHABET = "abcdefghijklmnopqrstuvwxyz"
ACCENTS = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u', 'ã':'a', 'à':'a', 'õ':'o', 'â':'a', 'ê':'e', 'ô':'o' ,'ç':'c'}

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

# Algoritmo MonoAlphabetic 
class MonoAlphabetic(CryptAlgorithm):
    def __init__(self, key, alphabet = WESTALPHABET):
        self.key = completeKey(key, alphabet)
        self.alphabet = alphabet

    # Encriptar texto
    def encrypt(self, text):
        # O maketrans retorna a tabela de tradução, que vai mapear cada caracter e transforma-lo em outro na mesma posição
        translationTable = string.maketrans(self.alphabet, self.key)

        return string.translate(string2Crypt(text), translationTable)

    # Decriptar texto
    def decrypt(self, text):
        newKey = self.invertMonoAlphabetic(self.key)
        # O maketrans retorna a tabela de tradução, que vai mapear cada caracter e transforma-lo em outro na mesma posição
        translationTable = string.maketrans(self.alphabet, newKey)

        return string.translate(text, translationTable)

# Completa uma key usando o resto do alfabeto na ordem natural
def completeKey(key, alphabet):
    key = notRepeated(string.lower(key))

    if len(key) == len(alphabet):
        return key

    for character in alphabet:
        if character not in key:
            key += character

    return key

# Elimina caracteres repetidos numa string
def notRepeated(key):
    seenCharacters = []
    newKey = ""

    for character in key:
        if character not in seenCharacters:
            newKey += character
            seenCharacters.append(character)

    return newKey

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

# Conta o numero de cada caracter e mostra as suas percentagens
def countCharacters(text):
    # Criar uma lista com 26 'None' ja dentro da lista -> [None, None, ..., None ]
    characters = [None] * len(WESTALPHABET)
    i = 0

    while i < len(WESTALPHABET):
        countChars = 0

        for character in text:
            if character == text[i]:
                countChars += 1

        i += 1

        # ord('x') dá o codigo ASCII do caracter 'x'
        index = ord(text[i]) - 97

        characters.insert(index, countChars)

    print('-- Percentage of the Characters --')

    for i in range(0, len(WESTALPHABET)):
        print(char(i + 97), ' = ', ((characters[i] * 1.0)/(len(text) * 1.0) * 100), '%')

# Conta o numero de cada digrafo e mostra as suas percentagens
def countDoubles(text):
    i = 1
    character1 = text[i-1]
    character2 = text[i]
    digraph = character1 + character2
    i += 1
    totalDigraphs = 0
    # Criação de um dicionario e adicionar o primeiro digrafo (key) com um um valor=1, por ser o primeiro
    dictionary = dict([(digraph, 1)])

    while i < len(text):
        character1 = text[i-1]
        character2 = text[i]
        digraph = character1 + character2
        i += 1
        totalDigraphs += 1

        if digraph in dictionary:
            digraphCount = dictionary[digraph]
            dictionary[digraph] = digraphCount + 1
        else:
            dictionary[digraph] = 1

    print("-- Percentage of Digraphs --")

    for key in sorted(dictionary.keys()):
        print(key, ' = ', ((dictionary[key] * 1.0)/(totalDigraphs * 1.0) * 100), '%')

print('***** MONOALPHABETIC CIPHER *****')
text = input()
option = input('Do you want to encrypt or decrypt the text? (E/D) -> ')

# ord('x') dá o codigo ASCII do caracter 'x'
if ord(option) == 69:
    alphabet_key = input('Key for the cipher: ')
    print('')

    key = MonoAlphabetic(alphabet_key)

    print(key.encrypt(text))
elif ord(option) == 68:
    countCharacters(text)
    print('')
    countDoubles(text)

    alphabet_key = input('Key for the cipher: ')
    print('')

    key = MonoAlphabetic(alphabet_key)

    print(key.decrypt(text))
else:
    print('You did not chose any of the option sorry!! :(')

# Exemplo de um texto encriptado:
# "ktnvihijtsbijciihijtsvijfmsjmoielmftdevltftytlctslbetmdhiefmtjcihsktnvihijtsbijciihijtsvijfmsjmoielmftdevltftytlctymlcezeymjciszlecezmhfoezifiylthttilifnuefmmjehmtjtlizejctmtdtjbtftsfemsfmsihmjmzmdijfmleumtftzilcmhiiomdcmfimlcezndmtzthivijctsjmgegdetcizmmdhiefmbmllicchilizilmhliymltsyidmylehielmviufisfimehydihijcmtftmcnmdhtfidttlbmjeumcevtfmoielmftdevltftytlctihmhmetlemftsymlcezeymjcisomunhgmdmjtjibmcevtftivijctanitjcihzkibtnmtoehhmesftanitfizlszehtfivijfmstsifectlisdevlieltsimdomllmgescmsmnszndcmftsyidtxjfnlmjcimcmlfifitjcihzlecezmlmhtaniztjsefilmhcilseftnhzdmltfisejviscehijctfmtlbmjeumtjmanisctylthtzetjmdjtnclmsifeisvmhtshnyesisymdkmftsyidmzefmfisihmjmsmjcisfiscmviujihijclmfmkmvemnhtncfttlzthmshishmsfehijsismjciletliszleceztntmdomllmgescmbnedkilhiyejctsmjctsztjvezctfianimlifnuefmztgilcnlmhifecezmoiuzthanimoielmymssmssihmlbihfmblmjfihmetlemfmsyisstmsnhmtyejetanijtfeoilifmfiolmjzesztglectfmzdtotjtsylehieltsanmcltfemsztllilmhgihfiytesfesstoteymlmisanizilsnscijctntxtvihmdomllmgescmzlceztcmhghihlidmtzmdijfmleumtftivijctgmscmvmanimoielmsicevissiejezemftnhmsihmjmmjcisymlmanimsvijfmsotssihfeoilijcismoelhtnmdnfejftmtzthitfthsyiltftihanikhmesfesytjegedefmfioejmjzielmhmesoiscevmdftanioielmsijihctftszthtidvelmsmjctshtsmeztfiymdmvlmsiolmjzesztbmlzemliesyticlemjtcmlmhnhmaniglmsebjeoezmcevmjmsvijfmsihlidmtmtstncltsmjtsknhytjctyidthijtsihlidmtmtanmdipescinjmjehefmfiktnvihijtsbijcijiscmifetissmivefjzemotehmesjtclemjtsfemsfmsihmjmihanisivemhytnanssehmsyisstmsmytjctntlisytjsvidfmzdtotjymlmtgmdmjthijtsytsecevtztjclegnlmhcmhghmsaniscishicitltdbezmsmzknvmitvijctanisioeuilmhsijceljtsgmftdivmlmhmtijzillmhijctftsscmjfsymlmfisisyiltftsanifiytsecmvmhojtdcehtoehfisihmjmymlmzthytlmsztjcmstsliymltstlbmjeumtjtsioezmhytlmaneymlmtifectlfmzmdijfletfmsdiclmsolmjzeszthmflnbmmejcijtzmhmllemfizlemlnhblmjfioiscevmddecilletiscmomuilymssmlymlmsibnjftydmjtmvilcijcifmsvijfmsomdcmhztjcmzctsftsmnctliszthdiectlisytlanilmutnhiszlectlaniymlcezeymjnhfigmciejsileftjmyltblmhmtjtvmefisibnefmomuilnhmsisstfimncblmotsjtymvedktfmsnmifectlmaniscetjmtifectlaniijanmjctveziylisefijcifmmsstzemtytlcnbnismfiifectlisidevlieltsfelebentzilcmhiytlcnijsifnlmjcitectmjtsmdhfmzthnjezmtfioezeijcihmflnbmcizinmejfmzlcezmsmnsjzemfizlifijzemesfivijfmsanifinmutmsecnmiszmlezmcmszthtmfivilthishtdevltvijfmihfeoilijcisymvedkisimylitsfsymlisomumdbnhsijceftanitsmdomllmgescmsytssmhcilisymtsfivijfmotlmftymvedktitsliscmjcisjtztjzdnenjtltdfizlcezmsijztjclmhtsmejfmmlifnuefmmjehmtjtlizejctstglicnftfnlmjcitsfemsfmsihmjmtnmejmnbnlmtcmlfemfmipytsetymcijcijmbmdilemhnjezeymdftytlctjmgegdetcizmmdhiefmbmlliccanimztjcizinxjtsdcehtsfemsftivijctytlctftsissishtcevtsmjcjethvmdijcifmisclmcbemszlemcevmsfmtyejetanimoielmftdevltftytlctisczdmlmhijcimyilfilcillijtmjvidjmzetjmd"