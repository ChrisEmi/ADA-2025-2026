import heapq
import sys

opcion = None
texto = None
while opcion != "4":
    print("Opciones de entrada de texto para codificacion Huffman:")
    print("1. Ingresar texto manualmente")
    print("2. Usar texto de ejemplo predefinido")
    print("3. Leer texto desde el archivo 'PRACTICA 6/texto.txt'")
    print("4. Salir")
    opcion = input("Seleccione una opcion (1-4): ")
    if opcion == "1":
        texto = input("Ingrese el texto a codificar: ")
        break
    elif opcion == "2":
        texto = "ejemplo de texto para codificacion huffman"
        print("Usando texto de ejemplo para codificacion huffman.")
        break
    elif opcion == "3":
        try:
            with open("PRACTICA 6/texto.txt", "r") as archivo:
                texto = archivo.read()
            print("Usando texto del archivo 'texto.txt' para codificacion huffman.")
            break
        except FileNotFoundError:
            print("El archivo 'PRACTICA 6/texto.txt' no existe.")
            continue
    elif opcion == "4":
        print("Saliendo del programa.")
        sys.exit()
    else:
        print("Opcion no valida. Por favor, elija una opcion del 1 al 4.")

if texto is None:
    sys.exit()

frecuencias = {}

for letra in texto:
    if letra in frecuencias:
        frecuencias[letra] += 1
    else:
        frecuencias[letra] = 1
    print(f"Frecuencia de '{letra}': {frecuencias[letra]}")


class Nodo:
    def __init__(self, letra, freq):
        self.letra = letra
        self.freq = freq
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.freq < otro.freq
    
heap = [Nodo(letra, freq) for letra, freq in frecuencias.items()]
heapq.heapify(heap)
    
while len(heap) > 1:
    nodo1 = heapq.heappop(heap)
    nodo2 = heapq.heappop(heap)
    nuevo_nodo = Nodo(None, nodo1.freq + nodo2.freq)
    nuevo_nodo.izquierda = nodo1
    nuevo_nodo.derecha = nodo2
    heapq.heappush(heap, nuevo_nodo)

codigos_huffman = {}

def generar_codigos(nodo, codigo=""):
    if nodo is None:
        return
    
    if nodo.letra is not None:
        codigos_huffman[nodo.letra] = codigo
        return
    
    generar_codigos(nodo.izquierda, codigo + "0")
    generar_codigos(nodo.derecha, codigo + "1")

def mostrar_arbol(nodo, prefijo="", es_izquierdo=True):
    """Muestra el árbol de Huffman de forma visual en la consola."""
    if nodo is None:
        return
    
    # Mostrar el nodo actual
    conector = "├── " if es_izquierdo else "└── "
    if prefijo == "":
        conector = ""
    
    if nodo.letra is not None:
        etiqueta = f"'{nodo.letra}' ({nodo.freq})"
    else:
        etiqueta = f"[{nodo.freq}]"
    
    print(prefijo + conector + etiqueta)
    
    # Preparar el prefijo para los hijos
    if prefijo == "":
        nuevo_prefijo = ""
    else:
        nuevo_prefijo = prefijo + ("│   " if es_izquierdo else "    ")
    
    # Mostrar los hijos
    hijos = []
    if nodo.izquierda is not None:
        hijos.append((nodo.izquierda, "0"))
    if nodo.derecha is not None:
        hijos.append((nodo.derecha, "1"))
    
    for i, (hijo, direccion) in enumerate(hijos):
        es_ultimo = (i == len(hijos) - 1)
        conector_hijo = "├── " if not es_ultimo else "└── "
        
        if hijo.letra is not None:
            etiqueta_hijo = f"({direccion}) '{hijo.letra}' ({hijo.freq})"
        else:
            etiqueta_hijo = f"({direccion}) [{hijo.freq}]"
        
        print(nuevo_prefijo + conector_hijo + etiqueta_hijo)
        
        # Recursión para los subárboles
        sub_prefijo = nuevo_prefijo + ("│   " if not es_ultimo else "    ")
        if hijo.izquierda is not None or hijo.derecha is not None:
            mostrar_subarbol(hijo, sub_prefijo)

def mostrar_subarbol(nodo, prefijo):
    """Función auxiliar para mostrar subárboles."""
    hijos = []
    if nodo.izquierda is not None:
        hijos.append((nodo.izquierda, "0"))
    if nodo.derecha is not None:
        hijos.append((nodo.derecha, "1"))
    
    for i, (hijo, direccion) in enumerate(hijos):
        es_ultimo = (i == len(hijos) - 1)
        conector = "├── " if not es_ultimo else "└── "
        
        if hijo.letra is not None:
            etiqueta = f"({direccion}) '{hijo.letra}' ({hijo.freq})"
        else:
            etiqueta = f"({direccion}) [{hijo.freq}]"
        
        print(prefijo + conector + etiqueta)
        
        if hijo.izquierda is not None or hijo.derecha is not None:
            nuevo_prefijo = prefijo + ("│   " if not es_ultimo else "    ")
            mostrar_subarbol(hijo, nuevo_prefijo)

raiz = heap[0]
generar_codigos(raiz)

print("\n" + "="*50)
print("ÁRBOL DE HUFFMAN")
print("="*50)
mostrar_arbol(raiz)
print("="*50 + "\n")

print("CÓDIGOS DE HUFFMAN:")
for letra, codigo in codigos_huffman.items():
    print(f"  Letra: {letra!r}, Codigo: {codigo}")

bits_originales = len(texto) * 8
bits_codificados = sum(frecuencias[letra] * len(codigo) for letra, codigo in codigos_huffman.items())
print(f"Bits en texto original: {bits_originales}")
print(f"Bits en texto codificado: {bits_codificados}")

texto_codificado = "".join(codigos_huffman[letra] for letra in texto)
print("Texto codificado:", texto_codificado)

