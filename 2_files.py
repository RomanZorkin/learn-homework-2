"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

import tempfile
from pathlib import Path
from urllib import request

import httpx

TARGET_PATH = Path('files')
FINISH_FILE = TARGET_PATH / 'referat2.txt'
# In the end of url we see dl=1 - this need for downloading file
# from dropbox site. In original url dl=0
file_url = 'https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=1'


def file_downloader(url: str) -> str:
    """Function download and read file from resource.

    Args:
        url (str): file resource url address

    Returns:
        str: file text.
    """
    file_data = httpx.get(file_url, follow_redirects=True)
    return file_data.text


def text_handler(text: str) -> str:
    """Function for processing and converting the current text of the file.

    The function determines the number of words in the text.\
    Replaces dots with an exclamation mark.

    Args:
        text (str): file text

    Returns:
        str: new file text
    """
    text_list = text.split()
    text = text.replace('.', '!', text.count('.'))
    print(f'Количесвто слов в файле referat составляет: {len(text_list)}')
    return text


def file_writer(text: str) -> None:
    with open(FINISH_FILE, 'w', encoding='utf-8') as new_referat:
        new_referat.write(text)
        print(
            'Файл с новыми значениями успешно сохранен! Адрес: {0}'.format(
                FINISH_FILE.resolve(),
            ),
        )


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    file_text = file_downloader(file_url)
    print(f'Длина строки файла referat составляет {len(file_text)} символов.')
    file_writer(
        text_handler(file_text),
    )


if __name__ == '__main__':
    main()
