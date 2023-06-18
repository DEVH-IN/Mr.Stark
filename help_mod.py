class Script(object):
    AI = [
        {
            "desc": "Generates AI response from OpenAI",
            "cmds": ["gpt", "askgpt", "chatgpt"],
            "usage": "/gpt Who are you?"
        }
    ]
    CARBON = [
        {
            "desc": "Creates a carbon in doc format",
            "cmds": ["carbon"],
            "usage": "/carbon reply to a text message or give some text as input"
        },
        {
            "desc": "Creates a carbon in image format",
            "cmds": ["icarbon"],
            "usage": "/icarbon reply to a text message or give some text as input"
        }
    ]
    DEV = [
        {
            "desc": "Executes python code",
            "cmds": ["eval", "e"],
            "usage": "/e [python code]"
        },
        {
            "desc": "Run bash/terminal cmd",
            "cmds": ["bash", "sh"],
            "usage": "/bash [cmd]"
        }
    ]
    FUN = [
        {
            "desc": "Get a cat image",
            "cmds": ["cat"],
             "usage": "/cat"
        },
        {
            "desc": "Get a dog image",
            "cmds": ["dog"],
             "usage": "/dog"
        },
        {
            "desc": "Get a panda image",
            "cmds": ["panda"],
             "usage": "/panda"
        },
        {
            "desc": "Get a bored gif 🥱",
            "cmds": ["bored"],
             "usage": "/bored"
        },
        {
            "desc": "get a image or gif of pikachu",
            "cmds": ["pikachu"],
             "usage": "/pikachu"
        },
        {
            "desc": "Get a patting gif",
            "cmds": ["pat"],
             "usage": "/pat"
        },
        {
            "desc": "Get a hugging gif",
            "cmds": ["hug"],
             "usage": "/hug"
        },
        {
            "desc": "Get a winking gif",
            "cmds": ["wink"],
             "usage": "/wink"
        }
    ]
    FILETOOLS = [
        {
            "desc": "Downloads File to Local",
            "cmds": ["download"],
            "usage": "/download [reply to a doc/vid]"
        },
        {
            "desc": "Upload Files from Local",
            "cmds": ["upload"],
            "usage": "/upload [filename/path of the file]"
        },
    ]
    GOOGLE = [
        {
            "desc": "Google searcher!",
            "cmds": ["gs", "google"],
            "usage": "/gs [text to search]"
        },
    ]
    GTA5 = [
        {
            "desc": "Gta-V wasted effect on replied image",
            "cmds": ["wasted"],
            "usage": "/wasted [reply to a photo]"
        },
        {
            "desc": "Gta-V mission passed effect on replied image",
            "cmds": ["passed"],
            "usage": "/passed [reply to a photo]"
        }
    ]
    IMDB = [
        {
            "desc": "Get information about a Movie/Series",
            "cmds": ["imdb"],
            "usage": "/imdb [Movename/Series Name]"
        }
    ]
    IMAGETOOLS = [
        {
            "desc": "Create ur own memes",
            "cmds": ["memify"],
            "usage": "/memify [Upper text ; Lower text] | reply to a media"
        },
        {
            "desc": "Crop Image Into Round & Cool Sticker",
            "cmds": ["circle"],
            "usage": "/circle [reply to a photo or sticker]"
        },
        {
            "desc": "Get Fake Certificate With Given Name!",
            "cmds": ["genca", "gencertificate"],
            "usage": "/genca [Name on the certificate]"
        }
    ]
    INSTADL = [
        {
            "desc": "Download post/reel from instagram",
            "cmds": ["insta", "instadl", "insdl", "instadownload"],
            "usage": "/instadl [instagram post/reel link]"
        }
    ]
    LOGOS = [
        {
            "desc": "Makes a logo for you with black bg",
            "cmds": ["alogo"],
            "usage": "/alogo [text for logo]"
        },
        {
            "desc": "Makes a logo for you, try it out",
            "cmds": ["slogo"],
            "usage": "/slogo [text for logo]"
        }
    ]
    MISC = [
        {
   "desc": "Add chat to quote db",
   "cmds": ["ad_qt"],
   "usage": "/add_qt"
        },
        {
   "desc": "remove chat from quote db",
   "cmds": ["del_qt"],
   "usage": "/del_qt"
        },
        {
   "desc": "sends quote daily at 8:00 am and 6:00 pm",
   "cmds": ["no cmd"],
   "usage": "works automatically"
        }
    ]
    MEDIAINFO = [
        {
            "desc": "Gets MediaInfo of Replied Video",
            "cmds": ["mediainfo", "mediadata"],
            "usage": "/mediainfo [Reply to a video]"
        }
    ]
    MONGODB = [
        {
            "desc": "Adds MongoDB to database so that u can access",
            "cmds": ["adddb"],
            "usage": "/adddb [mongo uri]"
        },
        {
            "desc": "Get access to the MongoDB uri u added using /adddb",
            "cmds": ["showdb"],
            "usage": "/showdb"
        }
    ]
    PASTE = [
        {
            "desc": "Pastes the given text in spacebin",
            "cmds": ["paste"],
            "usage": "/paste [reply to message/text file]"
        }
    ]
    QR = [
        {
            "desc": "Generates qr for given text",
            "cmds": ["qr"],
            "usage": "/qr [text to make qr]"
        }
    ]
    QUOTLY = [
        {
            "desc": "Converts your text into a quote",
            "cmds": ["quote", "qt", "qu", "q"],
            "usage": "/q [reply to a text message / give text as input]\nNote:\n1. No need to use args like -r for reply | reply set as default\n2.Either give text as reply or input"
        }
    ]
    STICKER = [
        {
            "desc": "Creates a sticker with given text",
            "cmds": ["stcr"],
            "usage": "/stcr Mr.Stark"
        }
    ]
    SYSTEM = [
        {
            "desc": "Ping-Pong",
            "cmds": ["p", "ping"],
        },
        {
            "desc": " whether the bot is alive or not",
            "cmds": ["alive"],
        },
        {
            "desc": "Restarts the bot",
            "cmds": ["restart"],
        }
    ]
    TELEGRAPH = [
        {
            "desc": "Creates a telegraph",
            "cmds": ["/telegraph", "/tgraph"],
            "usage": "/tgraph [title for the telegraph | reply to a text message]"
        }
    ]
    TRANSLATE = [
        {
            "desc": "Translates the replied message",
            "cmds": ["tr", "translate"],
            "usage": "/tr [language code | reply to a text message]"
        }
    ]
    UPDATE = [
        {
            "desc": "Updates the system",
            "cmds": ["up", "update"],
        },
        {
            "desc": "Deletes snippets in gitlab",
            "cmds": ["d"],
        }
    ]
    URLUPLOADER = [
        {
            "desc": "download's file from given link",
            "cmds": ["urlupload"],
            "usage": "/urlupload [direct link of the file]"
        }
    ]
    WHOIS = [
        {
            "desc": "Know who the replied person is",
            "cmds": ["info", "whois"],
            "usage": "/info [user id/username | reply to a user message]"
        }
    ]
    WRITE = [
        {
            "desc": "Writes given text on a white paper",
            "cmds": ["write"],
            "usage": "/write hello"
        }
    ]
