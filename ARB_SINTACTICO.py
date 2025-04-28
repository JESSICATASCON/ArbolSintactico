import ast

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_syntax_tree(expr):
    try:
        tree = ast.parse(expr, mode='eval')
        return parse_ast(tree.body)
    except SyntaxError as e:
        print(f"Error de sintaxis: {e}")
        return None
    except Exception as e:
        print(f"Error inesperado: {e}")
        return None

def parse_ast(node):
    if isinstance(node, ast.Num):
        return Node(str(node.n))
    elif isinstance(node, ast.Name):
        return Node(node.id)
    elif isinstance(node, ast.BinOp):
        left = parse_ast(node.left)
        right = parse_ast(node.right)
        op = parse_operator(node.op)
        return Node(op, left, right)
    elif isinstance(node, ast.UnaryOp):
        operand = parse_ast(node.operand)
        op = parse_operator(node.op)
        return Node(op, operand)
    elif isinstance(node, ast.Expression):
        return parse_ast(node.body)
    else:
        raise ValueError(f"Nodo AST no soportado: {type(node).__name__}")

def parse_operator(op_node):
    if isinstance(op_node, ast.Add):
        return '+'
    elif isinstance(op_node, ast.Sub):
        return '-'
    elif isinstance(op_node, ast.Mult):
        return '*'
    elif isinstance(op_node, ast.Div):
        return '/'
    else:
        raise ValueError(f"Operador no soportado: {type(op_node).__name__}")

def print_tree(node, level=0, prefix="Raíz: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.value))
        if node.left or node.right:
            print_tree(node.left, level + 1, "Izq: ")
            print_tree(node.right, level + 1, "Der: ")

def main():
    print("Constructor de Árboles Sintácticos")
    print("Ingrese expresiones matemáticas para generar sus árboles sintácticos")
    print("Operadores soportados: +, -, *, /")
    print("Puede usar variables (a, b, c, etc.) y números")
    print("Escriba 'salir' para terminar el programa\n")
    
    while True:
        expression = input("\nIngrese una expresión matemática (o 'salir'): ").strip()
        
        if expression.lower() == 'salir':
            print("\nPrograma terminado.")
            break
        
        if not expression:
            print("Por favor ingrese una expresión válida.")
            continue
        
        syntax_tree = build_syntax_tree(expression)
        
        if syntax_tree:
            print(f"\nÁrbol Sintáctico para la expresión: {expression}")
            print_tree(syntax_tree)
        else:
            print("No se pudo generar el árbol sintáctico. Verifique la expresión.")

if __name__ == "__main__":
    main()