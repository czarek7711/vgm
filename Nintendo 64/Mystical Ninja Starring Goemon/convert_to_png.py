import os
from PIL import Image

def convert_images_to_png(directory='.', max_size=(500, 500), num_colors=128, dpi=72, compression_level=9):
    # Get all fitting images in the current directory
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.jpg', '.jpeg', '.bmp', '.gif', '.png', '.webp')):
            input_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, 'cover.png')
            
            # Open the input image
            with Image.open(input_path) as img:
                # Resize the image only if it's bigger than max_size
                if img.size[0] > max_size[0] or img.size[1] > max_size[1]:
                    img.thumbnail(max_size, Image.LANCZOS)
                # Convert the image to indexed mode with a limited number of colors
                img = img.convert('P', palette=Image.ADAPTIVE, colors=num_colors)
                # Strip metadata
                img.info = {}
                # Save the image in PNG format with adjusted DPI and max compression level
                img.save(output_path, format='PNG', dpi=(dpi, dpi), compress_level=compression_level)
                print(f"Image {filename} converted and saved as {output_path}")

# Example usage
convert_images_to_png()
