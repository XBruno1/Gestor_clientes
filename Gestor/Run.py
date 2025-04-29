import sys

try:
    from . import ui as gradio_ui
    from . import Data_base as db
    from .Menu import menu
except ImportError:
    from Gestor import ui as gradio_ui
    import sys
    import Data_base as db
    from Menu import menu

def terminal_check():
    """Realiza una verificación básica de la base de datos desde la terminal."""
    print("Running terminal check...")
    try:
        # Ejemplo de verificación: contar clientes en la base de datos
        count = len(db.Clientes.lista_clientes)
        print(f"Database connection successful. Number of clients: {count}")
    except Exception as e:
        print(f"Error during terminal check: {e}")

def main():
    """Punto de entrada principal del programa."""
    if len(sys.argv) > 1:
        option = sys.argv[1]
        if option == "-t":
            terminal_check()
        elif option == "-m":
            menu.iniciar()
        else:
            print(f"Opción desconocida: {option}")
            print("Opciones disponibles:")
            print("  -t : Ejecutar verificación en terminal")
            print("  -m : Iniciar el menú")
    else:
        # Lanzar la interfaz de usuario de Gradio si no se pasan argumentos
        gradio_ui.launch_ui()

if __name__ == "__main__":
    main()