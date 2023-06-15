import youtube_dl
def download_hls_video(url, save_path):
    ydl_opts = {
        'outtmpl': save_path,
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


video_url = "https://crs.ccdntech.com/rds/playerh7vodcdn?vod41/1030-delta-ch.mp4&cname&hls"
save_path = "C:\\Users\\user\\Desktop\\法說會_A\\2308台達電_2018Q3法人說明會_20181030.mp4"


download_hls_video(video_url, save_path)