ссылка на бота: https://t.me/w3bcam3ra_bot

чтобы бот работал, напишите фразу "запусти камеру"

чтобы программа работала, необходимо скачать себе файл "тг бот ...", "webcamera.py" и преобразовать его в формат .exe

руководство по преобразованию: 
1. откройте командную строку и напишите в ней следующее: pip install pyinstaller
2. следующая команда: cd C:\путь до вашей папки, куда вы сохранили файл webcamera.py
3. следующая команда: pyinstaller --onefile webcamera.py
4. ждем. готовый файл .exe будет находиться в папке dist
5. если все удалось, то заходим в бота, пишем фразу и ждем, пока откроется наша вебкамера (это может занять некоторое время)

так же можно изменить размер окна камеры. для этого в коде программы webcamera.py измените цифру в строке cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600) на желаемую. изменится ширина окна. так же и со строкой cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480), где изменяется высота окна.

еще один важный пункт. чтобы бот запускал наш .exe файл, нужно в строке программы тг бот ... os.startfile(r'C:\Users\motor\OneDrive\Рабочий стол\pythonProject1\dist\webcamera.exe') указать путь на ВАШЕМ компьютере, где будет храниться файл .exe
