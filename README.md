# Bulk Image Resizer and Converter

A Python script to batch resize and convert images in a folder using the Pillow library. Supports resizing by fixed dimensions or percentage, format conversion (JPEG, PNG, WEBP, etc.), and quality adjustment.

---

## 📦 Features

- Resize images by **width**, **height**, or **percentage**
- Convert images to another **format** (JPEG, PNG, WEBP, etc.)
- Adjust **quality** of output images (for lossy formats)
- **Dry-run mode** to preview which files will be processed
- Automatically skips corrupt or non-image files
- Prevents overwriting by appending a counter to duplicate filenames

---

## 🛠 Requirements

- Python 3.x
- Pillow library

Install dependencies with:

```bash
pip install Pillow
```

## 🚀 Usage
```bash
python resize.py <input_folder> <output_folder> [options]
```

## 🔧 Options

| Option      | Description                                             |
|-------------|---------------------------------------------------------|
| `--width`   | Target width in pixels                                  |
| `--height`  | Target height in pixels                                 |
| `--percent` | Resize images by percentage (e.g., 50 for 50%)          |
| `--format`  | Output image format: JPEG, PNG, WEBP, etc.              |
| `--quality` | Output quality (1–100, default: 85)                     |
| `--dry-run` | Preview files to be processed without saving            |


Note: If only width or height is provided, aspect ratio is maintained.

## 📁 Examples
Resize by Width
```bash
python resize.py images resized --width 800
```
Resize by Percentage
```bash
python resize.py images resized --percent 50
```
Resize and Convert to PNG
```bash
python resize.py images output --width 600 --format PNG
```
Dry Run Preview
```bash
python resize.py images output --percent 30 --dry-run
```
## ⚠️ Notes
Output files are saved in the specified output directory.

If a file with the same name already exists, a counter is appended (e.g., image_1.jpg, image_2.jpg).

Supported formats depend on what Pillow supports on your system.
