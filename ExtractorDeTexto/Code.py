from PIL import Image
import pytesseract

def extract_text_from_image(image_path):
    #Open image
    img = Image.open(image_path)

    #Extraemos texto utilizado pyteseract
    text = pytesseract.image_to_string(img)

    return text

def save_text_to_file(text, output_file):
    with open(output_file, "w") as file:
        file.write(text)

if __name__=="MAIN":
    #Ruta de imagen
    image_path = r"C:\Users\samue\OneDrive\Imágenes\Capturas de pantalla\Imagen1.png"

    #Extraer texto de imagen
    extracted_text = extract_text_from_image(image_path)

    #Save the text extracted from a file .txt
    output_file = r"C:\Users\samue\OneDrive\Escritorio\ExtractorDeTexto\texto_extraido.txt"

    #Guardamos el texto extraido en el archivo de salida
    save_text_to_file(extracted_text, output_file)

    print("Text Extracted and saved on: " , output_file)

