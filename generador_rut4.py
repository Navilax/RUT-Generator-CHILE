import tkinter as tk
from PIL import Image, ImageTk
import random

# Lista de RUTs a excluir (ejemplo)
exclusiones = []

def calcular_digito_verificador(numero):
  """Calcula el dígito verificador de un RUT chileno utilizando el algoritmo del módulo 11.

  Args:
    numero: El número base del RUT (sin el dígito verificador).

  Returns:
    El dígito verificador como una cadena (un dígito o 'K').
  """

  reverse_numero = str(numero)[::-1]
  factors = [2, 3, 4, 5, 6, 7]
  suma = 0

  for i, digit in enumerate(reverse_numero):
    suma += int(digit) * factors[i % 6]

  resto = 11 - (suma % 11)

  if resto == 11:
    return '0'
  elif resto == 10:
    return 'K'
  else:
    return str(resto)

def generar_ruts(prefijo, cantidad):
  """Genera una lista de RUTs válidos con un prefijo específico.

  Args:
    prefijo: Los primeros dígitos del RUT.
    cantidad: La cantidad de RUTs a generar.

  Returns:
    Una lista de RUTs generados.
  """

  ruts = []
  for _ in range(cantidad):
    numero_correlativo = int(prefijo + str(random.randint(100000, 999999)))
    digito_verificador = calcular_digito_verificador(numero_correlativo)
    rut = f"{numero_correlativo}-{digito_verificador}"
    ruts.append(rut)
  return ruts

def generar_y_mostrar_ruts():
  """Obtiene el prefijo y la cantidad de RUTs, genera los RUTs y los muestra en la interfaz."""
  prefijo = entry_prefijo.get()
  cantidad = int(entry_cantidad.get())
  ruts = generar_ruts(prefijo, cantidad)
  text_resultados.delete(1.0, tk.END)
  text_resultados.insert(tk.END, "\n".join(ruts))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de RUTs con fondo")

# Cargar la imagen de fondo y ajustar el tamaño
ruta_imagen = "images/wallp2.jpg"
try:
  imagen_original = Image.open(ruta_imagen)
except FileNotFoundError:
  print("No se encontró la imagen. Verifica la ruta.")
  exit()

ancho_imagen = 300 # Ajusta el ancho de la imagen según tus preferencias
alto_imagen = 200 # Ajusta el alto de la imagen según tus preferencias
imagen_ajustada = imagen_original.resize((ancho_imagen, alto_imagen), resample=Image.LANCZOS)
foto_imagen = ImageTk.PhotoImage(imagen_ajustada)

# Crear un label para la imagen de fondo y colocarlo debajo del cuadro de resultados
label_imagen = tk.Label(ventana, image=foto_imagen)
label_imagen.pack(side=tk.TOP)

# Crear los elementos de la interfaz
label_prefijo = tk.Label(ventana, text="Ingrese el prefijo:")
entry_prefijo = tk.Entry(ventana)
label_cantidad = tk.Label(ventana, text="Cantidad de RUTs:")
entry_cantidad = tk.Entry(ventana)
button_generar = tk.Button(ventana, text="Generar RUT", command=generar_y_mostrar_ruts, height=4)
text_resultados = tk.Text(ventana, height=10)

# Empaquetar los elementos
label_prefijo.pack()
entry_prefijo.pack()
label_cantidad.pack()
entry_cantidad.pack()
button_generar.pack()
text_resultados.pack()

# Forzar una actualización de la ventana
ventana.update()

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
