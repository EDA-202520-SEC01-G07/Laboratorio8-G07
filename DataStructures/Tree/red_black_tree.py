def new_map():
    return {"root":None}
def default_compare(key, element):
    if key < element:
        return -1
    elif key > element:
        return 1
    else:
        return 0
def rotate_left(node): #Cuando hay un enlace rojo en la derecha
    arriba = node["right"]
    arriba["left"] = node
    arriba["color"] = 1 #1 es black
    arriba["left"]["color"] = 0 #0 es red
    return arriba
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
