from PIL import Image
import os

def convert_png_to_ico(png_path, ico_path=None, sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]):
    """
    Convert a PNG image to an ICO file while preserving transparency.
    
    :param png_path: Path to the input .png file.
    :param ico_path: Path to the output .ico file. If not provided, uses the same name as the .png.
    :param sizes: List of tuples representing the sizes to include in the .ico file.
    """
    try:
        # If no .ico path is provided, derive it from the .png path
        if ico_path is None:
            ico_path = os.path.splitext(png_path)[0] + '.ico'
        
        # Open the PNG image
        img = Image.open(png_path)
        
        # Ensure the image has an alpha channel (transparency)
        if img.mode != 'RGBA':
            img = img.convert('RGBA')
        
        # Save the image as an .ico file with the specified sizes
        img.save(ico_path, format='ICO', sizes=sizes)
        print("Conversion successful! Saved as:", ico_path)
    except Exception as e:
        print("Error converting PNG to ICO:", e)

if __name__ == "__main__":
    # Example usage:
    convert_png_to_ico(r'F:\xampp\htdocs\search\favicon.png')
