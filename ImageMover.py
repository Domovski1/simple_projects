import os
import shutil
import colorama
# image_types = [".JPG", ".jpg", ".PNG", ".png"] # В дальнешем сделаю проход цикла по каждому формату


def fill_image_list(directory: str) -> list:
    """Фильтрует файлы и добавляет все названия фотографий в получаемый список"""

    images = []
    for image in os.listdir(directory):
        if image.endswith(".heic") or image.endswith(".jpg") or image.endswith(".HEIC"):
            images.append(image)
    return images


def make_dir(directory: str):
    """Создаёт папку с названием Images если она не существует."""

    if os.path.exists(f"{directory}\\Images"):
        print("CODE 101: Папка была обнаружена")
    else:
        os.mkdir(f"{directory}\\Images")
        print("CODE 100: Папка была создана")


def move_images(directory: str, images_list: list):
    """Перещает фотографии в папку"""

    for image in images_list:
        print(image)
        shutil.move(f"{directory}\\{image}", f"{directory}\\Images")


if __name__ == "__main__":
    directory_name = input("Введите ссылку на папку: \n").replace("\"", "")
    make_dir(directory_name)
    move_images(directory = directory_name, images_list = fill_image_list(directory = directory_name))
    print(colorama.Fore.GREEN,"Все файлы перемещены.")
    print(colorama.Fore.WHITE)
    