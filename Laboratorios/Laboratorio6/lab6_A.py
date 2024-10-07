# Lab 6 A
# Nombre:Daniel esteban castro calderin 
# Grupo: 33
# Cod Estudiante:202310422

######################################
#                                    #
#             Punto #1               #
#                                    #
######################################

# Crear una clase llamada `SistemaArchivos` utilizando la representación de Árboles como HashMap vista en clase. 
# Al instanciar `SistemaArchivos`, debe crear un nodo raíz con el valor "C:".
# La clase `SistemaArchivos` debe permitir la gestión de rutas y contener los siguientes métodos:
# 
# - `crear_directorio(ruta)`: Recibe un parámetro `ruta` que contiene la nueva ruta a crear dentro del sistema de archivos. Las rutas deben comenzar desde la raíz.
#   La ruta se almacena de la siguiente manera: Cada elemento de la ruta está separado por '\' y el primer elemento siempre es "C:". Cada elemento subsecuente representa un subdirectorio en una estructura jerárquica.
#   - Si la jerarquía ya existe, retorna `False`.
#   - Si se crea exitosamente, retorna `True`.
#   - En caso de recibir una entrada inválida, lanza un error.
# - `consultar_directorio(ruta)`: Recibe un parámetro `ruta` que contiene la ruta a consultar en el sistema de archivos. 
#   - Si la ruta existe, retorna `True`.
#   - Si la ruta no existe, retorna `False`.
# 
# Nota: Debe usar la representación de Árboles como HashMap para que el punto sea válido.
# 
# INICIO_SOLUCION 
class SistemaArchivos:
    def __init__(self):
        self.sistema = {"C:": {}}

    def crear_directorio(self, ruta):
        if not ruta.startswith("C:"):
            raise ValueError("Ruta inválida. Debe comenzar con 'C:'")

        directorios = ruta.split("\\")[1:]

        actual = self.sistema["C:"]

        for directorio in directorios:
            if directorio not in actual:
                actual[directorio] = {}
            elif actual[directorio]:
                return False
            actual = actual[directorio]

        return True

    def consultar_directorio(self, ruta):
        if not ruta.startswith("C:"):
            raise ValueError("Ruta inválida. Debe comenzar con 'C:'")

        directorios = ruta.split("\\")[1:]

        actual = self.sistema["C:"]

        for directorio in directorios:
            if directorio not in actual:
                return False
            actual = actual[directorio]

        return True

# ejemplo de uso 
sistema = SistemaArchivos()

print(sistema.crear_directorio("C:\\Users"))
print(sistema.crear_directorio("C:\\Users\\Documents"))
print(sistema.crear_directorio("C:\\Users\\Documents"))
print(sistema.consultar_directorio("C:\\Users\\Documents"))
print(sistema.consultar_directorio("C:\\Users\\Pictures"))
# FIN_SOLUCION

######################################
#                                    #
#             Punto #2               #
#                                    #
######################################

# Mejore la eficiencia de las operaciones de inserción y consulta en la clase `SistemaArchivos` del Punto #1.
# Optimice la representación del árbol para mejorar la eficiencia de log(n) a tiempo constante. Incluya todo el código de la clase SistemaArchivos.

# INICIO_SOLUCION
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = {}
        self.existe = False

class SistemaArchivos:
    def __init__(self):
        self.raiz = Nodo("C:")

    def crear_directorio(self, ruta):
        if not ruta.startswith("C:"):
            raise ValueError("Ruta inválida. Debe comenzar con 'C:'")

        directorios = ruta.split("\\")[1:]
        actual = self.raiz

        for directorio in directorios:
            if directorio not in actual.hijos:
                actual.hijos[directorio] = Nodo(directorio)
            actual = actual.hijos[directorio]
            actual.existe = True

        return True

    def consultar_directorio(self, ruta):
        if not ruta.startswith("C:"):
            raise ValueError("Ruta inválida. Debe comenzar con 'C:'")

        directorios = ruta.split("\\")[1:]
        actual = self.raiz

        for directorio in directorios:
            if directorio not in actual.hijos:
                return False
            actual = actual.hijos[directorio]

        return actual.existe

#ejemplo de uso
sistema = SistemaArchivos()

print(sistema.crear_directorio("C:\\Users")) 
print(sistema.crear_directorio("C:\\Users\\Documents")) 
print(sistema.crear_directorio("C:\\Users\\Documents")) 
print(sistema.consultar_directorio("C:\\Users\\Documents")) 
print(sistema.consultar_directorio("C:\\Users\\Pictures"))
# FIN_SOLUCION

######################################
#                                    #
#             Punto #3               #
#                                    #
######################################

# Partiendo de la clase `SistemaArchivos` del Punto #1. Cree el método `hallar_altura(ruta)` en la clase `SistemaArchivos`.
# Este método debe buscar el nodo con el valor dado y retornar la altura del nodo en la estructura. Si no existe lanza un error. Incluya todo el código de la clase SistemaArchivos.

# INICIO_SOLUCION
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = {}
        self.existe = False

class SistemaArchivos:
    def __init__(self):
        self.raiz = Nodo("C:")

    def crear_directorio(self, ruta):
        if not ruta.startswith("C:"):
            raise ValueError("Ruta inválida. Debe comenzar con 'C:'")

        directorios = ruta.split("\\")[1:]
        actual = self.raiz

        for directorio in directorios:
            if directorio not in actual.hijos:
                actual.hijos[directorio] = Nodo(directorio)
            actual = actual.hijos[directorio]
            actual.existe = True

        return True

    def consultar_directorio(self, ruta):
        if not ruta.startswith("C:"):
            raise ValueError("Ruta inválida. Debe comenzar con 'C:'")

        directorios = ruta.split("\\")[1:]
        actual = self.raiz

        for directorio in directorios:
            if directorio not in actual.hijos:
                return False
            actual = actual.hijos[directorio]

        return actual.existe

    def hallar_altura(self, ruta):
        if not ruta.startswith("C:"):
            raise ValueError("Ruta inválida. Debe comenzar con 'C:'")

        directorios = ruta.split("\\")[1:]
        actual = self.raiz
        altura = 0

        for directorio in directorios:
            if directorio not in actual.hijos:
                raise ValueError("Ruta no existe")
            actual = actual.hijos[directorio]
            altura += 1

        return altura

# ejemplo de uso
sistema = SistemaArchivos()

sistema.crear_directorio("C:\\Users")
sistema.crear_directorio("C:\\Users\\Documents")
sistema.crear_directorio("C:\\Users\\Documents\\Pictures")

print(sistema.consultar_directorio("C:\\Users\\Documents")) 
print(sistema.hallar_altura("C:\\Users\\Documents"))  
print(sistema.hallar_altura("C:\\Users\\Documents\\Pictures"))  
# FIN_SOLUCION


######################################
#                                    #
#             Punto #4               #
#                                    #
######################################

# Cree una función llamada `calcular_posfijo` que reciba una expresión matemática en notación posfija (postfija) y calcule el resultado.
# Las operaciones a considerar son:  multiplicación (*), división (/), suma (+) y resta (-).

# INICIO_SOLUCION
def calcular_posfijo(expresion):
    pila = []

    for token in expresion.split():
        if token in "+-*/":
            if len(pila) < 2:
                raise ValueError("Expresión inválida")

            operand2 = pila.pop()
            operand1 = pila.pop()

            if token == "+":
                resultado = operand1 + operand2
            elif token == "-":
                resultado = operand1 - operand2
            elif token == "*":
                resultado = operand1 * operand2
            elif token == "/":
                if operand2 == 0:
                    raise ZeroDivisionError("División por cero")
                resultado = operand1 / operand2

            pila.append(resultado)
        else:
            pila.append(float(token))

    if len(pila) != 1:
        raise ValueError("Expresión inválida")

    return pila[0]
# FIN_SOLUCION

######################################
#                                    #
#             Punto #5               #
#                                    #
######################################

# Cree una clase llamada `ArbolExpresion` que permita construir un árbol de expresiones a partir de una expresión matemática en notación inorden.
# Las operaciones a considerar son: multiplicación (*), división (/), suma (+) y resta (-), 
# y deben manejarse también los paréntesis para definir la precedencia de las operaciones.
# 
# La clase `ArbolExpresion` debe incluir los siguientes métodos:
# - `leer_inorden(expresion)`: Recibe una cadena `expresion` que contiene la expresión matemática en notación inorden y construye el árbol de expresiones.
# - `imprimir()`: Imprime la expresión en notación inorden.
# 
# Incluya todo el código de la clase 'ArbolExpresion'.

# INICIO_SOLUCION
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolExpresion:
    def __init__(self):
        self.raiz = None

    def leer_inorden(self, expresion):
        self.raiz = self.construir_arbol(expresion)

    def construir_arbol(self, expresion):
        tokens = expresion.split()
        pila = []

        for token in tokens:
            if token in "+-*/":
                operand2 = pila.pop()
                operand1 = pila.pop()
                nodo = Nodo(token)
                nodo.izquierda = operand1
                nodo.derecha = operand2
                pila.append(nodo)
            elif token == "(":
                continue
            elif token == ")":
                continue
            else:
                nodo = Nodo(token)
                pila.append(nodo)

        return pila[0]

    def imprimir(self, nodo=None):
        if nodo is None:
            nodo = self.raiz

        if nodo:
            self.imprimir(nodo.izquierda)
            print(nodo.valor, end=" ")
            self.imprimir(nodo.derecha)

    def __str__(self):
        self.imprimir()
        return ""
# FIN_SOLUCION

######################################
#                                    #
#             Punto #6               #
#                                    #
######################################

# Extienda la clase `ArbolExpresion` para permitir la construcción de un árbol de expresiones a partir de una expresión matemática en notación posorden.
# La clase `ArbolExpresion` debe incluir el siguiente método adicional:
# - `leer_posorden(expresion_posorden)`: Recibe una cadena `expresion_posorden` que contiene la expresión matemática en notación posorden y construye el árbol de expresiones.
# - `imprimir_posorden()`: Imprime la expresión en notación posorden.
# 
# Incluya todo el código de la clase 'ArbolExpresion'.

# INICIO_SOLUCION
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolExpresion:
    def __init__(self):
        self.raiz = None

    def leer_inorden(self, expresion):
        self.raiz = self.construir_arbol_inorden(expresion)

    def leer_posorden(self, expresion_posorden):
        self.raiz = self.construir_arbol_posorden(expresion_posorden)

    def construir_arbol_inorden(self, expresion):
        tokens = expresion.split()
        pila = []

        for token in tokens:
            if token in "+-*/":
                operand2 = pila.pop()
                operand1 = pila.pop()
                nodo = Nodo(token)
                nodo.izquierda = operand1
                nodo.derecha = operand2
                pila.append(nodo)
            elif token == "(":
                continue
            elif token == ")":
                continue
            else:
                nodo = Nodo(token)
                pila.append(nodo)

        return pila[0]

    def construir_arbol_posorden(self, expresion_posorden):
        tokens = expresion_posorden.split()
        pila = []

        for token in tokens:
            if token in "+-*/":
                operand2 = pila.pop()
                operand1 = pila.pop()
                nodo = Nodo(token)
                nodo.izquierda = operand1
                nodo.derecha = operand2
                pila.append(nodo)
            else:
                nodo = Nodo(token)
                pila.append(nodo)

        return pila[0]

    def imprimir(self):
        self.imprimir_inorden(self.raiz)
        print()

    def imprimir_inorden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz

        if nodo:
            self.imprimir_inorden(nodo.izquierda)
            print(nodo.valor, end=" ")
            self.imprimir_inorden(nodo.derecha)

    def imprimir_posorden(self):
        self.imprimir_posorden_rec(self.raiz)
        print()

    def imprimir_posorden_rec(self, nodo=None):
        if nodo is None:
            nodo = self.raiz

        if nodo:
            self.imprimir_posorden_rec(nodo.izquierda)
            self.imprimir_posorden_rec(nodo.derecha)
            print(nodo.valor, end=" ")

    def __str__(self):
        self.imprimir()
        return ""
# FIN_SOLUCION

######################################
#                                    #
#             Punto #7               #
#                                    #
######################################

# Extienda la clase `ArbolExpresion` para evaluar la expresión representada por el árbol.
# La clase `ArbolExpresion` debe incluir el siguiente método adicional:
# - `evaluar()`: Evalúa la expresión representada por el árbol y retorna el resultado. Incluya todo el código de la clase 'ArbolExpresion'.

# INICIO_SOLUCION
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolExpresion:
    def __init__(self):
        self.raiz = None

    def leer_inorden(self, expresion):
        self.raiz = self.construir_arbol_inorden(expresion)

    def leer_posorden(self, expresion_posorden):
        tokens = expresion_posorden.split()
        self.raiz = self.construir_arbol_posorden(tokens)

    def construir_arbol_inorden(self, expresion):
        tokens = expresion.split()
        pila = []

        for token in tokens:
            if token in "+-*/":
                operand2 = pila.pop()
                operand1 = pila.pop()
                nodo = Nodo(token)
                nodo.izquierda = operand1
                nodo.derecha = operand2
                pila.append(nodo)
            elif token == "(":
                continue
            elif token == ")":
                continue
            else:
                nodo = Nodo(token)
                pila.append(nodo)

        return pila[0]

    def construir_arbol_posorden(self, tokens):
        if len(tokens) == 1:
            return Nodo(tokens[0])
        else:
            operador = tokens[-1]
            nodo = Nodo(operador)
            mitad = len(tokens) // 2
            nodo.izquierda = self.construir_arbol_posorden(tokens[:mitad])
            nodo.derecha = self.construir_arbol_posorden(tokens[mitad:-1])
            return nodo

    def imprimir_inorden(self):
        self.imprimir_inorden_rec(self.raiz)
        print()

    def imprimir_inorden_rec(self, nodo=None):
        if nodo is None:
            nodo = self.raiz

        if nodo:
            self.imprimir_inorden_rec(nodo.izquierda)
            print(nodo.valor, end=" ")
            self.imprimir_inorden_rec(nodo.derecha)

    def imprimir_posorden(self):
        self.imprimir_posorden_rec(self.raiz)
        print()

    def imprimir_posorden_rec(self, nodo=None):
        if nodo is None:
            nodo = self.raiz

        if nodo:
            self.imprimir_posorden_rec(nodo.izquierda)
            self.imprimir_posorden_rec(nodo.derecha)
            print(nodo.valor, end=" ")

    def evaluar(self):
        return self.evaluar_rec(self.raiz)

    def evaluar_rec(self, nodo=None):
        if nodo is None:
            nodo = self.raiz

        if nodo.valor in "+-*/":
            izquierda = self.evaluar_rec(nodo.izquierda)
            derecha = self.evaluar_rec(nodo.derecha)

            if nodo.valor == "+":
                return izquierda + derecha
            elif nodo.valor == "-":
                return izquierda - derecha
            elif nodo.valor == "*":
                return izquierda * derecha
            elif nodo.valor == "/":
                if derecha == 0:
                    raise ZeroDivisionError("División por cero")
                return izquierda / derecha
        else:
            return float(nodo.valor)
# FIN_SOLUCION
