from os import path

from youtube_dl import YoutubeDL

from TamilBots.config import DURATION_LIMIT
from TamilBots.helpers.errors import DurationLimitError
ydl_opts = {
    "format": "bestaudio/best",
    "verbose": True,
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}
ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info["duration"] / 60)

    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"❌ 𝐕𝐢𝐝𝐞𝐨 𝐢𝐬 𝐋𝐨𝐧𝐠𝐞𝐫 𝐓𝐡𝐚𝐧 {DURATION_LIMIT} 𝐌𝐢𝐧𝐮𝐭𝐞(𝐬) 𝐀𝐫𝐞𝐧'𝐭 𝐀𝐥𝐥𝐨𝐰𝐞𝐝, 𝐓𝐡𝐞 𝐏𝐫𝐨𝐯𝐢𝐝𝐞𝐝 𝐕𝐢𝐝𝐞𝐨 𝐈𝐬 {duration} 𝐌𝐢𝐧𝐮𝐭𝐞(𝐬)"
        )
    try:
        ydl.download([url])
    except:
        raise DurationLimitError(
            f"❌ 𝐕𝐢𝐝𝐞𝐨 𝐢𝐬 𝐋𝐨𝐧𝐠𝐞𝐫 𝐓𝐡𝐚𝐧 {DURATION_LIMIT} 𝐌𝐢𝐧𝐮𝐭𝐞(𝐬) 𝐀𝐫𝐞𝐧'𝐭 𝐀𝐥𝐥𝐨𝐰𝐞𝐝, 𝐓𝐡𝐞 𝐏𝐫𝐨𝐯𝐢𝐝𝐞𝐝 𝐕𝐢𝐝𝐞𝐨 𝐈𝐬 {duration} 𝐌𝐢𝐧𝐮𝐭𝐞(𝐬)"
        )
    return path.join("downloads", f"{info['id']}.{info['ext']}")
