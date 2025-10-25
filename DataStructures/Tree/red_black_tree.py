from DataStructures.Tree import rbt_node as n

def new_map():
    return {"root":None}
def default_compare(key, element):
    if key < element:
        return -1
    elif key > element:
        return 1
    else:
        return 0
    
def size_tree(root):
    if root is not None:
        return 1 + size_tree(root["left"]) + size_tree(root["right"])
    else:
        return 0
    
def is_red(node):
    if node is not None and node["color"] == 0:
        return True
    else:
        return False
    
def rotate_left(node): #Cuando hay un enlace rojo en la derecha
    rotar = node["right"]
    temporal = rotar["left"]
    rotar["left"] = node
    node["right"] = temporal
    node["color"] = 0 #Red
    rotar["color"]=1 #Black
    return rotar

def rotate_right(node): #Cuando hay dos enlaces rojos seguidos
    if node or node["left"] is None:
        return None
    else:
        left = node["left"]
        left["right"] = node
        left["color"] = 1
        left["right"]["color"] = 0
    return left 

def flip_node_color(node): #Cambia el color de un solo nodo
    if node is not None:
        color = node["color"]
        if color == 0:
            node["color"] = 1
        else:
            node["color"] = 0
    return node

def flip_colors(node): #Cambia el color del nodo y de sus dos hijos
    if node is not None:
        flip_node_color(node)
        izq = node["left"]["color"]
        der = node["right"]["color"]
        if node["left"] is not None:
            if izq == 0:
                node["left"]["color"] = 1
            else:
                node["left"]["color"] = 0
        if node["right"] is not None:
            if der == 0:
                node["right"]["color"] = 1
            else:
                node["right"]["color"] = 0
    return node

def put(rbt, key, value): #Ingresa una pareja llave,valor. Si la llave ya existe, se reemplaza el valor.
    insert_node(rbt["root"], key, value)
    return rbt

def insert_node(root, key, value): #Ingresa una pareja llave,valor. Si la llave ya existe, se reemplaza el valor.
    if root is None:
        return n.new_node(key, value)
    cmp = default_compare(key, root["key"])
    if cmp == -1:
        insert_node(root["left"], key, value)
    elif cmp == 1:
        insert_node(root["right"], key, value)
    elif cmp == 0:
        root["value"] = value
        
    if is_red(root["right"]) and not is_red(root["left"]): #Si hay un enlace rojo en la derecha
        rotate_left(root)
    if is_red(root["right"]) and is_red(root["left"]): #Si los hijos tienen enlace rojo
        flip_colors(root)
    if is_red(root["left"]) and is_red(root["left"]["left"]): #Si hay dos enlaces rojos a la izq seguidos
        rotate_right(root)
    return root 

def get(rbt, key): #Devuelve el valor de la llave
    return get_node(rbt["root"], key)

def get_node(root, key):
    if root == None:
        return None
    cmp = default_compare(key, root["key"])
    if cmp == 0:
        return root["value"]
    else:
        if cmp == -1:
            return get_node(root["left"], key)
        if cmp == 0:
            return get_node(root["right"], key)