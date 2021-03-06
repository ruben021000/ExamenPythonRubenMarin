import random

def choose_secret(filename):
    """Dado un nombre de fichero, esta función devuelve una palabra aleatoria de este fichero transformada a mayúsculas.
    Args:
      filename: El nombre del fichero. Ej. "palabras_reduced.txt"
    Returns:
      secret: Palabra elegida aleatoriamente del fichero transformada a mayúsculas. Ej. "CREMA"
    """
    words = []
    f = open(filename, mode="rt", encoding="utf-8")

    for line in f:
        line=line.split()
        words.extend(line)

    f.close()
    word = random.choice(words)
    return word
    
def compare_words(word,secret):
    """Dadas dos palabras en mayúsculas (word y secret), esta función calcula las posiciones de las letras de word que aparecen en la misma posición en secret, y las posiciones de las letras de word que aparecen en secret pero en una posición distinta.
    Args:
      word: Una palabra. Ej. "CAMPO"
      secret: Una palabra. Ej. "CREMA"
    Returns:
      same_position: Lista de posiciones de word cuyas letras coinciden en la misma posición en secret. En el caso anterior: [0]
      same_letter: Lista de posiciones de word cuyas letras están en secret pero en posiciones distintas. En el caso anterior: [1,2]
    """
    same_position = []
    same_letter = []
    for i in range(0,len(word)):
      if word[i] == secret[i]:
        same_position.append(i)
      if word[i] in secret and i not in same_position:
        same_letter.append(i)
    return same_position,same_letter




def print_word(word,same_position,same_letter):
    """Dada una palabra, una lista same_position y otra lista same_letter, esta función creará un string donde aparezcan en mayúsculas las letras de la palabra que ocupen las posiciones de same_position, en minúsculas las letras de la palabra que ocupen las posiciones de same_letter y un guión (-) en el resto de posiciones
    Args:
      word: Una palabra. Ej. "CAMPO"
      same_letter_position: Lista de posiciones. Ej. [0]
      same_letter: Lista de posiciones. Ej. [1,2]
    Returns:
      transformed: La palabra aplicando las transformaciones. En el caso anterior: "Cam--"
    """
    transformed = []
    for i in range(0,len(word)):
        transformed.append("-")
    for letter in same_position:
      transformed[letter] = word[letter].upper()
    for letter in same_letter:
      transformed[letter] = word[letter].lower()

    return transformed
    
    
def choose_secret_advanced(filename):
    """Dado un nombre de fichero, esta función filtra solo las palabras de 5 letras que no tienen acentos (á,é,í,ó,ú). De estas palabras, la función devuelve una lista de 15 aleatorias no repetidas y una de estas 15, se selecciona aleatoriamente como palabra secret.
    Args:
      filename: El nombre del fichero. Ej. "palabras_extended.txt"
    Returns:
      selected: Lista de 15 palabras aleatorias no repetidas que tienen 5 letras y no tienen acentos
      secret: Palabra elegida aleatoriamente de la lista de 15 seleccionadas transformada a mayúsculas
    """
    words = []
    f = open(filename, mode="rt", encoding="utf-8")

    for line in f:
        line=line.split()
        words.extend(line)
    f.close()

    for word in words:
      if len(word) != 5:
        words.remove(word)

    for w in words:
        if "á" in w:
          words.remove(w)
        if "é" in w:
          words.remove(w)
        if "í" in w:
          words.remove(w)
        if "ó" in w:
          words.remove(w)
        if "ú" in w:
          words.remove(w)
        
    selected = []
    for i in range(0,15):

      selected.append(random.choice(words))
    
    secret = random.choice(selected)
      
    return secret.upper()
    
   
 
def check_valid_word(selected):
    """Dada una lista de palabras, esta función pregunta al usuario que introduzca una palabra hasta que introduzca una que esté en la lista. Esta palabra es la que devolverá la función.
    Args:
      selected: Lista de palabras.
    Returns:
      word: Palabra introducida por el usuario que está en la lista.
    """
    userWord = ""
    for i in range(0,9999): 
      userWord = str(input("Enter a word: "))
      if userWord in selected:
        print("Funciona: " + userWord)
'''
if __name__ == "__main__":
    secret=choose_secret("palabras_reduced.txt")
    print("Palabra a adivinar: "+secret)#Debug: esto es para que sepas la palabra que debes adivinar
    for repeticiones in range(0,6):
        word = input("Introduce una nueva palabra: ")
        same_position, same_letter = compare_words(word,secret)
        resultado=print_word(word,same_position,same_letter)
        print(resultado)
        if word == secret:
            print("HAS GANADO!!")
            exit()
    print("LO SIENTO, NO LA HAS ADIVINIDADO. LA PALABRA ERA "+secret)   
'''
#print(choose_secret("palabras_reduced.txt"))
#a = compare_words("CAMPO","CREMA")
#print(print_word("CAMPO",a[0],a[1]))
#print(choose_secret_advanced("palabras_extended.txt"))
#print(check_valid_word("palabras_reduced.txt"))

#Si el fichero recibido por choose_secret no tiene palabras:
try:
  choose_secret("pruebaExcepciones.txt")
except:
    print("La lista de palabras esta vacia")

#Si la longitud de las palabras recibidas por compare_words no es la misma:
try:
  word = "hola"
  secret = "no"
  print(word[len(secret)])
  print(secret[len(word)])

except:
    print("La longitud de las palabras no es igual")

#Si same_position o same_letter recibidos por print_word no son listas:
try:
  same_position = ["hola"]
  same_letter = "no"
  print(same_position.append("hola"))
  print(same_letter.append("hola"))

except:
    print("same_position o same_letter no son listas")