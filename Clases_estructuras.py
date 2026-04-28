# Archivo de las clases nodo y lista enlazada
#* En este archivo se definen las clases necesarias para la implementacion
#* de ellas en los ejercicios propuestos del taller numero 2 de estructuras de datos,
#* se incluyen las clases nodo y lista enlazada simple, doble, circular simple y circular doble
#! Clase nodo y lista enlazada simple
class node_simple:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

class lista_enlazada_simple:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def agregar(self, data):
        nuevo_nodo = node_simple(data)
        if self.head is None:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            self.tail.next = nuevo_nodo
            self.tail = nuevo_nodo
        
    def buscar(self, data):
        nodo = self.head
        while nodo is not None:
            if nodo.data == data:
                return nodo
            nodo = nodo.next
        return None
    
    def eliminar(self, data):
        nodo = self.buscar(data)
        if nodo is None:
            return "no se encontro la informacion a eliminar"
        
        if nodo == self.head:
            if nodo == self.tail:
                self.head = None
                self.tail = None
            else:
                aux = self.head.next
                self.head.next = None
                self.head = aux
        elif nodo == self.tail:
            aux = self.head
            while aux.next != self.tail:
                aux = aux.next
            
            aux.next = None
            self.tail = aux
        else:
            aux = self.head
            while aux.next != nodo:
                aux = aux.next
            
            aux.next = nodo.next
            nodo.next = None
        
        return "eliminado"
    
    def mostrar(self):
        nodo_lista = self.head
        while nodo_lista is not None:
            print(f"{nodo_lista} -> ", end="")
            nodo_lista = nodo_lista.next
        print("None")
    
    def modificar(self, dato_actual, nuevo_dato):
        x = self.buscar(dato_actual)
        if x is None:
            return "no se encontro la informacion a modificar"
        x.data = nuevo_dato
        return "modificado"

#! Clase nodo y lista enlazada doble
class node_doble:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
class ListaEnlazadaDoble:
    def __init__(self):
        self.head = None
        self.tail = None


    def insertar(self,data):
        new_node = node_doble(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def modificar(self,old_data,new_data):
        current = self.head
        while current is not None:
            if current.data == old_data:
                current.data = new_data
                return
            current = current.next

    def buscar(self,data):
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next
        return None
    
    def eliminar(self,data):
        current = self.buscar(data)

        if current is None:
            return f"el nodo con el dato {data} no existe"
        #! Eliminar el nodo encontrado
        #? Si el nodo a eliminar es el head o el tail, se deben actualizar los punteros correspondientes
        if current == self.head:
            #? si el nodo a eliminar es el unico nodo en la lista, se deben actualizar ambos punteros head y tail a None
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                #* si el nodo a eliminar es el head pero no es el unico nodo,
                #* se debe actualizar el puntero head al siguiente nodo 
                #* y establecer el puntero prev del nuevo head a None
                self.head = self.head.next
                self.head.prev = None
                current.next = None
        elif current == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            current.prev = None
        else:
            #* si el nodo a eliminar no es ni el head ni el tail, 
            #* se deben actualizar los punteros next y prev de los nodos adyacentes 
            #* para omitir el nodo a eliminar
            current.prev.next = current.next
            current.next.prev = current.prev
            current.next = None
            current.prev = None
    

    def imprimir(self):
        current = self.head
        while current is not None:
            print(f"{current} -> ", end=" ")
            current = current.next
        print("None")

#! Clase nodo y lista enlazada circular simple
class node_circular:
    def __init__(self, data):
        self.data = data
        self.next = None


#* Lista enlazada circular simple
class lista_circular:
    def __init__(self):
        self.head = None
        self.tail = None

    def esta_vacia(self):
        return self.head is None

    def agregar(self, data):
        nuevo_nodo = node_circular(data)

        if self.esta_vacia():
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
            self.tail.next = self.head
            return

        self.tail.next = nuevo_nodo
        self.tail = nuevo_nodo
        self.tail.next = self.head

    def buscar(self, data):
        if self.esta_vacia():
            return None

        actual = self.head
        while True:
            if actual.data == data:
                return actual
            actual = actual.next
            if actual == self.head:
                break

        return None

    def eliminar(self, data):
        if self.esta_vacia():
            return "no se encontro la informacion a eliminar"

        actual = self.head
        anterior = self.tail

        while True:
            if actual.data == data:
                # Caso: solo un nodo
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                # Caso: eliminar cabeza
                elif actual == self.head:
                    self.head = self.head.next
                    self.tail.next = self.head
                # Caso: eliminar cola
                elif actual == self.tail:
                    anterior.next = self.head
                    self.tail = anterior
                # Caso: nodo intermedio
                else:
                    anterior.next = actual.next
                return "eliminado"

            anterior = actual
            actual = actual.next

            if actual == self.head:
                break

        return "no se encontro la informacion a eliminar"

    def mostrar(self):
        if self.esta_vacia():
            print("lista vacia")
            return

        actual = self.head
        elementos = []

        while True:
            elementos.append(str(actual.data))
            actual = actual.next
            if actual == self.head:
                break

        print(" -> ".join(elementos) + " -> (vuelve al inicio)")

    def modificar(self, dato_actual, nuevo_dato):
        nodo = self.buscar(dato_actual)
        if nodo is None:
            return "no se encontro la informacion a modificar"

        nodo.data = nuevo_dato
        return "modificado"


#! Clase nodo y lista enlazada circular doble
class node_circular_doble:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class ListaEnlazadaCircularDoble:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def estaVacia(self):
        return self.head is None
    
    def insertar(self,data):
        nodo = node_circular_doble(data)
        if self.estaVacia():
            self.head = nodo
            self.tail = nodo
            nodo.next = nodo
            nodo.prev = nodo
        else:
            self.tail.next = nodo
            nodo.next = self.head
            nodo.prev = self.tail
            self.tail = nodo
            self.head.prev = nodo
    

    def buscar(self, dato):
        if self.estaVacia():
            return f"esta vacia"
        
        puntero = self.head
        while True:
            if puntero.data == dato:
                return puntero
            puntero = puntero.next
            if puntero is self.tail:
                if puntero.data == dato:
                    return puntero
                else:
                    puntero = None
                    return puntero 
        
    def modificar(self, dato_nuevo, dato_viejo):
        if self.estaVacia():
            return
        
        puntero = self.buscar(dato_viejo)

        if puntero != None:
            puntero.data = dato_nuevo
            return f"el valor {dato_viejo} fue modificado por el valor {dato_nuevo}"
        else:
            return f"El valor {dato_viejo} no fue encontrado en la lista"
    
    def eliminar(self, dato_a_eliminar):
        if self.estaVacia():
            return "lista vacia"
        
        cabeza  = self.head
        cola = self.tail
        nodo_a_eliminar = self.buscar(dato_a_eliminar)

        if nodo_a_eliminar is None:
            return "no se encontro el valor a eliminar"

        while True:
            if nodo_a_eliminar is cabeza and nodo_a_eliminar is cola:
                self.head = None
                self.tail = None
            elif nodo_a_eliminar is cabeza:
                self.head = nodo_a_eliminar.next
                self.head.prev = self.tail
                self.tail.next = self.head
            elif nodo_a_eliminar is cola:
                self.tail = nodo_a_eliminar.prev
                self.tail.next = self.head
                self.head.prev = self.tail
            else:
                nodo_a_eliminar.prev.next = nodo_a_eliminar.next
                nodo_a_eliminar.next.prev = nodo_a_eliminar.prev
            return f"el valor {dato_a_eliminar} fue eliminado"
        
    def imprimir(self):
        if self.estaVacia():
            return "lista vacia"
        
        puntero = self.head
        while True:
            print(puntero.data)
            puntero = puntero.next
            if puntero is self.head:
                break