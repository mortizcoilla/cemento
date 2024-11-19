import os

# Lista de carpetas a ignorar
CARPETAS_IGNORADAS = {'.git', '.github', '.ipynb_checkpoints', 'node_modules', 'venv'}

def obtener_estructura_directorio(ruta_directorio, nivel=0):
    estructura = ""
    archivos_y_directorios = sorted(os.listdir(ruta_directorio))
    
    for elemento in archivos_y_directorios:
        if elemento in CARPETAS_IGNORADAS:
            continue
        
        ruta_elemento = os.path.join(ruta_directorio, elemento)
        estructura += "    " * nivel + "|-- " + elemento + "\n"
        
        if os.path.isdir(ruta_elemento):
            estructura += obtener_estructura_directorio(ruta_elemento, nivel + 1)
    
    return estructura

def imprimir_estructura_proyecto(ruta_proyecto):
    estructura = obtener_estructura_directorio(ruta_proyecto)
    print(estructura)
    return estructura

if __name__ == "__main__":
    ruta_proyecto = "/home/makabrus/Workspace/RegresionKeras"
    estructura = imprimir_estructura_proyecto(ruta_proyecto)
    
    with open(os.path.join(ruta_proyecto, "estructura.txt"), "w") as archivo:
        archivo.write(estructura)
