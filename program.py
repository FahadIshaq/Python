from PIL import Image
import os
import pillow_avif

def convert_to_high_quality_png(input_directory, output_directory):
    # Check if the output directory exists
    counter = 1
    original_output_directory = output_directory
    while os.path.exists(output_directory):
        output_directory = f"{original_output_directory}_{counter}"
        counter += 1

    # Ensure the newly determined output directory exists
    os.makedirs(output_directory, exist_ok=True)

    for filename in os.listdir(input_directory):
        input_path = os.path.join(input_directory, filename)

        # Check if the item in the directory is a file and has a valid image extension
        if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.avif', '.webp', '.gif')):
            try:
                # Open the image
                image = Image.open(input_path)

                # If the image is in WEBP format, convert it to JPEG first
                if filename.lower().endswith('.webp'):
                    buffer_path = input_path.replace('.webp', '.jpg')  # Temporary path
                    image.convert('RGB').save(buffer_path, format='JPEG', quality=95)
                    image = Image.open(buffer_path)
                    os.remove(buffer_path)  # Removing the temporary JPEG image

                # For AVIF format, create a new Image object to work with
                if filename.lower().endswith('.avif'):
                    new_image = Image.new("RGBA", image.size)
                    new_image.paste(image, (0, 0))
                    image = new_image

                # Ensure the image has an alpha channel for transparency (PNG)
                if image.mode != 'RGBA':
                    image = image.convert('RGBA')

                # Create the output path
                output_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.png")

                # Save the image as PNG with high quality (adjust the quality as needed)
                image.save(output_path, format='PNG', quality=95)

                # Delete the original image file
                os.remove(input_path)

                print(f"Converted {input_path} to {output_path} and deleted the original.")
            except Exception as e:
                print(f"Error converting {input_path}: {e}")

if __name__ == "__main__":
    input_directory = "/Users/fahad_ishaq/Downloads/Downloads/Pics/Website_Pictures"  # Specify the directory containing the input images
    output_directory = "/Users/fahad_ishaq/Downloads/Downloads/Pics/Website_Pictures/converted"  # Specify the directory where the converted images will be saved

    convert_to_high_quality_png(input_directory, output_directory)
