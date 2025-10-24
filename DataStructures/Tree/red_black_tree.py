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
    rotar = node["right"]
    temporal = rotar["left"]
    rotar["left"] = node
    node["right"] = temporal
    node["color"] = 0 #Red
    rotar["color"]=1 #Black
    return rotar

def rotate_right(node):
    if node or node["left"] is None:
        return None
    else:
        left = node["left"]
        left["right"] = node
        left["color"] = 1
        left["right"]["color"] = 0
    return left 

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
def flip_node_color(node):
    if node is not None:
        if node ["left"] ["color"]== 0:
            node ["left"] ["color"]= 1
        if node ["right"] ["color"]== 1:
            node ["right"] ["color"]= 0
    return node