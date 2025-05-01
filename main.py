import os
import argparse
from PIL import Image

def resize_image(input_path, output_path, width=None, height=None, percentage=None, format=None, quality=85):
    with Image.open(input_path) as img:
        input_format = img.format
        if percentage:
            width = int(img.width*(percentage/100))
            height = int(img.height*(percentage/100))
        elif width and not height:
            height = int((width/img.width)*img.height)
        elif height and not width:
            width = int((height/img.height)*img.width)
        
        if width and height:
            img = img.resize((width, height), Image.Resampling.LANCZOS)
        
        output_format = format.upper() if format else input_format
        extension = "jpg" if output_format == "JPEG" else output_format.lower()

        base = os.path.splitext(os.path.basename(input_path))[0]
        out_file = os.path.join(output_path, f"{base}.{extension}")
        counter = 1
        while os.path.exists(out_file):
            out_file = os.path.join(output_path, f"{base}_{counter}.{extension}")
            counter += 1
        
        img.save(out_file, output_format, quality=quality)
        print(f"✅ Saved: {out_file}")
        

def process_folder(input_dir, output_dir, width, height, percentage, format, quality, dry_run):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for file in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file)
        if os.path.isfile(file_path):
            try:
                with Image.open(file_path) as img:
                    img.verify()
                if dry_run:
                    print(f"Would process: {file}")
                else:
                    resize_image(file_path, output_dir, width, height, percentage, format, quality)
            except (IOError, SyntaxError) as e:
                print(f"❌ Skipping non-image or corrupt file: {file}")
            except Exception as e:
                print(f"❌ Error processing {file}: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bulk Image Resizer and Converter")
    parser.add_argument("input", help="Input folder with images")
    parser.add_argument("output", help="Output folder to save processed images")
    parser.add_argument("--width", type=int, help="Resize width in pixels")
    parser.add_argument("--height", type=int, help="Resize height in pixels")
    parser.add_argument("--percent", type=float, help="Resize by percentage")
    parser.add_argument("--format", help="Convert image format: JPEG, PNG, WEBP, etc.")
    parser.add_argument("--quality", type=int, default=85, help="Quality for output image (1-100)")
    parser.add_argument("--dry-run", action="store_true", help="Preview files to be processed")

    args = parser.parse_args()
    process_folder(
        args.input, args.output, args.width, args.height,
        args.percent, args.format, args.quality, args.dry_run
    )

