import os
from PIL import Image

def resize_images(input_folder, output_folder, size=(800, 800), format="PNG"):
    """
    Resize and convert all images from input_folder and save to output_folder.
    """

    # create output folder if not exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        try:
            file_path = os.path.join(input_folder, filename)

            # check if file is image
            if filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):

                img = Image.open(file_path)

                # resize the image
                img_resized = img.resize(size)

                # new file name
                new_name = os.path.splitext(filename)[0] + f".{format.lower()}"

                save_path = os.path.join(output_folder, new_name)

                # save image
                img_resized.save(save_path, format=format)

                print(f"[DONE] {filename} → {new_name}")

            else:
                print(f"[SKIPPED] Not an image: {filename}")

        except Exception as e:
            print(f"[ERROR] Cannot process {filename} → {e}")


if __name__ == "__main__":
    input_folder = "input_images"
    output_folder = "output_images"

    resize_images(input_folder, output_folder, size=(600, 600), format="PNG")
    print("✨ Batch processing completed!")
