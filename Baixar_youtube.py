from yt_dlp import YoutubeDL

url = input('Cole a sua URL aqui: ')

ydl_opts = {
    'format': 'best',  
    'outtmpl': '%(title)s.%(ext)s'  
}

try:
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True) 
        print("Título:", info.get('title'))
        print("Thumbnail URL:", info.get('thumbnail'))
        print("Download concluído!")
except Exception as e:
    print("Ocorreu um erro:", e)
