import os
import shutil
import colorama


def main():
        
    images = []
    directory_name = input("Введите ссылку на папку: \n").replace("\"", "")

    # image_types = [".JPG", ".jpg", ".PNG", ".png"] # В дальнешем сделаю проход цикла по каждому формату

    def fill_image_list(images_list: list):
        """Фильтрует файлы и добавляет все названия фотографий в получаемый список"""

        for image in os.listdir(directory_name):
            if image.endswith(".heic") or image.endswith(".jpg"):
                images.append(image)


    def make_dir():
        """Создаёт папку с названием Images если она не существует."""

        if os.path.exists(f"{directory_name}\\Images"):
            print("CODE 101: Папка была обнаружена")
        else:
            os.mkdir(f"{directory_name}\\Images")
            print("CODE 100: Папка была создана")

    def move_images(directory: str, images_list: list):
        """Перещает фотографии в папку"""

        for image in images:
            print(image)
            shutil.move(f"{directory}\\{image}", f"{directory}\\Images")

            
    print("Вот список файлов, который я нашёл:")
    make_dir()
    fill_image_list(images_list = images)
    move_images(directory = directory_name, images_list = images)



    print(colorama.Fore.GREEN,"Все файлы перемещены.")
    print(colorama.Fore.WHITE)
    # C:\Users\62427\OneDrive\Рабочий стол\img

main()