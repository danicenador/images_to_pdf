from PIL import Image
import os
from typing import List

INPUT_FOLDER: str = "input"
OUTPUT_FOLDER: str = "output"


def get_all_folders_in_input() -> List[str]:
    """
    Get all folders in the input directory.
    """
    return [
        f
        for f in os.listdir(INPUT_FOLDER)
        if os.path.isdir(os.path.join(INPUT_FOLDER, f))
    ]


def get_all_image_files(folder: str) -> List[str]:
    """
    Get all image files in the specified folder.
    """
    image_files = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                image_files.append(os.path.join(root, file))
    return image_files


def build_pdf(image_files: List[str], output_file_name: str) -> None:
    """
    Build a PDF from the list of image files.
    """
    output_path = os.path.join(OUTPUT_FOLDER, output_file_name)
    images = [Image.open(img).convert("RGB") for img in image_files]
    images[0].save(output_path, save_all=True, append_images=images[1:])


def main():
    folders: List[str] = get_all_folders_in_input()
    for folder in folders:
        folder_path = os.path.join(INPUT_FOLDER, folder)
        image_files = get_all_image_files(folder_path)
        if image_files:
            output_file_name: str = folder + ".pdf"
            build_pdf(image_files, output_file_name)
            print(f"PDF created successfully: {output_file_name}")
        else:
            print(f"No images found in folder: {folder}")


if __name__ == "__main__":
    main()
