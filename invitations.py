# Versión simplificada sin pandas
from PIL import Image, ImageDraw, ImageFont
import os

def leer_nombres_csv(archivo_csv):
    """Lee nombres desde un archivo CSV simple"""
    nombres = []
    try:
        with open(archivo_csv, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                nombre = linea.strip()
                if nombre and nombre.lower() != 'nombre':  # Saltar cabecera
                    nombres.append(nombre)
        return nombres
    except Exception as e:
        print(f"Error leyendo CSV: {e}")
        return []

# Leer nombres desde CSV o usar lista manual
archivo = leer_nombres_csv('invitados.csv')

def crear_invitacion(nombre, template_path="invitacion.png", output_dir="images"):
    """Crea una invitación individual"""
    
    # Crear directorio de salida
    os.makedirs(output_dir, exist_ok=True)
    
    # Abrir template
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)
    
    # Configurar fuente
    TAMANO_FUENTE = 100
    font = ImageFont.truetype("EBGaramond-Bold.ttf", TAMANO_FUENTE)
    
    # Calcular posición centrada
    bbox = draw.textbbox((0, 0), nombre, font=font)
    text_width = bbox[2] - bbox[0]
    
    # Posición del texto (ajusta estos valores según tu template)
    x = (img.width - text_width) // 2  # Centrado horizontalmente
    y = 380  # Ajusta esta posición Y según tu diseño
    
    # Dibujar texto
    draw.text((x, y), nombre, fill="white", font=font)
    
    # Guardar

    filename = f"invitacion_{nombre.replace(' ', '_')}.png"
    output_path = os.path.join(output_dir, filename)
    img.save(output_path)
    print(f"Creada: {filename}")

# Generar todas las invitaciones
print("Generando invitaciones...")
for linea in archivo:
    nombre, telegram = linea.strip().split(',')
    crear_invitacion(nombre)

print(f"¡Completado! {len(archivo)} invitaciones generadas.")