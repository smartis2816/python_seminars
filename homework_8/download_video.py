from pytube import YouTube

def choose_stream(videos):
    count = 1
    for item in videos:
        print(f'{count}) {item}')
        count += 1
    itag_num = input('Введите itag: ')
    return itag_num

def init_video():
    url = input(f'Вставьте ссылку на видео: ')
    yt = YouTube(url)
    print(f'Название видео - {yt.title}')
    return yt

def download_stream(itag_num, yt):
    download_path = input('Укажите путь загрузки: ')
    stream = yt.streams.get_by_itag(itag_num)
    stream.download(output_path=download_path)


yt = init_video()
videos = yt.streams
download_stream(choose_stream(videos), yt)

