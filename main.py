import os
import tkinter as tk
from dotenv import load_dotenv

# Carga las variables del archivo .env
load_dotenv()


# Función 1: captura lo que el usuario escribió en los campos
def capturar_credenciales():
    usuario = entrada_usuario.get()
    clave = entrada_clave.get()
    return usuario, clave


# Función 2: compara con las variables de entorno
def validar_credenciales(usuario, clave):
    user_env = os.getenv("APP_USER")
    pass_env = os.getenv("APP_PASSWORD")
    return usuario == user_env and clave == pass_env


# Función 3: muestra el mensaje con su color
def mostrar_mensaje():
    usuario, clave = capturar_credenciales()
    if validar_credenciales(usuario, clave):
        etiqueta_resultado.config(text="Ha ingresado correctamente", fg="green")
    else:
        etiqueta_resultado.config(text="El usuario o la contraseña están incorrectos", fg="red")


# Ventana principal
ventana = tk.Tk()
ventana.title("Validar acceso")
ventana.geometry("900x600")

tk.Label(ventana, text="Usuario", font=("Arial", 16)).pack(pady=(60, 5))
entrada_usuario = tk.Entry(ventana, font=("Arial", 16))
entrada_usuario.pack()

tk.Label(ventana, text="Contraseña", font=("Arial", 16)).pack(pady=(20, 5))
entrada_clave = tk.Entry(ventana, font=("Arial", 16), show="*")
entrada_clave.pack()

tk.Button(ventana, text="Ingresar", font=("Arial", 16), command=mostrar_mensaje).pack(pady=25)

etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 18, "bold"))
etiqueta_resultado.pack(pady=10)

ventana.mainloop()