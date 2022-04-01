"""_summary_

    Working with library PIL
    
"""

from PIL import Image

def rotate(image_path, degrees_to_rotate, output_image_path) -> None:
    try:
        image_obj: Image = Image.open(image_path)
        rotated_image = image_obj.rotate(degrees_to_rotate)
        rotated_image.save(output_image_path)
        rotated_image.show()
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    path_img: str = '/home/juan/Descargas/programacion/ejemplos_python/Python-logo.png'
    degrees: int = 180
    output_path: str = '/home/juan/Descargas/programacion/ejemplos_python/Python-rotate.png'
    rotate(path_img, degrees, output_path)