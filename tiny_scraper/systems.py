systems = [
 {"name": "a5200", "id": 40, "extensions": ["a52", "bin", "zip"]},
    {
        "name": "amiga",
        "id": 64,
        "extensions": [
            "adf",
            "dms",
            "zip",
            "lha",
            "lzh",
            "hdf",
            "hdz",
            "hd",
            "hds",
            "hfe",
            "ipf",
            "uae",
        ],
    },
    {
        "name": "atarist",
        "id": 42,
        "extensions": ["st", "stx", "msa", "dim", "ipf", "ctr", "zip"],
    },
    {"name": "cps1", "id": 6, "extensions": ["zip", "chd", "ccd"]},
    {
        "name": "dos",
        "id": 135,
        "extensions": ["zip", "7z", "rar", "exe", "com", "bat", "iso", "img", "bin"],
    },
    {"name": "fbneo", "id": 142, "extensions": ["zip", "chd", "bin"]},
    {"name": "gb", "id": 9, "extensions": ["gb", "bin", "zip"]},
    {"name": "gg", "id": 21, "extensions": ["gg", "bin", "sms", "zip"]},
    {"name": "lynx", "id": 28, "extensions": ["lnx", "bin", "zip"]},
    {
        "name": "mdcd",
        "id": 20,
        "extensions": ["bin", "ccd", "chd", "cue", "img", "iso", "sub", "wav", "zip"],
    },
    {"name": "naomi", "id": 56, "extensions": ["chd", "bin", "gdi", "raw", "zip"]},
    {"name": "ngp", "id": 82, "extensions": ["ngp", "ngc", "bin", "zip"]},
    {"name": "pce", "id": 105, "extensions": ["pce", "cue", "ccd", "sgx", "zip"]},
    {"name": "pico", "id": 234, "extensions": ["p8", "png", "zip"]},
    {
        "name": "ps",
        "id": 57,
        "extensions": [
            "bin",
            "img",
            "mdf",
            "iso",
            "cue",
            "ccd",
            "pbp",
            "chd",
            "m3u",
            "toc",
            "cbn",
            "sub",
            "zip",
        ],
    },
    {"name": "scummvm", "id": 123, "extensions": ["zip", "scummvm", "svm"]},
    {"name": "sms", "id": 2, "extensions": ["sms", "bin", "zip"]},
    {"name": "vic20", "id": 0, "extensions": ["zip"]},
    {"name": "a7800", "id": 0, "extensions": ["zip"]},
    {"name": "atomiswave", "id": 53, "extensions": ["chd", "bin", "gdi", "zip"]},
    {"name": "cps2", "id": 7, "extensions": ["zip", "chd", "ccd"]},
    {"name": "dreamcast", "id": 23, "extensions": ["cdi", "gdi", "chd", "bin", "zip"]},
    {
        "name": "fc",
        "id": 3,
        "extensions": ["nes", "fds", "unf", "unif", "nez", "nsf", "zip"],
    },
    {"name": "gba", "id": 12, "extensions": ["gba", "bin", "zip"]},
    {"name": "gw", "id": 52, "extensions": ["mgw", "zip"]},
    {"name": "mame", "id": 75, "extensions": ["zip", "chd", "bin"]},
    {
        "name": "msx",
        "id": 113,
        "extensions": ["rom", "dsk", "cas", "mx1", "mx2", "col", "zip"],
    },
    {"name": "nds", "id": 15, "extensions": ["nds", "bin", "zip"]},
    {"name": "ons", "id": 0, "extensions": ["zip"]},
    {
        "name": "pcecd",
        "id": 114,
        "extensions": ["cue", "ccd", "chd", "pce", "iso", "sgx", "zip"],
    },
    {"name": "poke", "id": 211, "extensions": ["min", "zip"]},
    {"name": "ps2", "id": 58, "extensions": ["iso","bin"]},
    {
        "name": "psp",
        "id": 61,
        "extensions": ["iso", "cso", "pbp", "chd", "m3u", "toc", "zip"],
    },
    {
        "name": "sega32x",
        "id": 19,
        "extensions": [
            "32x",
            "smd",
            "md",
            "bin",
            "ccd",
            "cue",
            "img",
            "iso",
            "sub",
            "wav",
            "zip",
        ],
    },
    {"name": "varcade", "id": 0, "extensions": ["zip"]},
    {"name": "ws", "id": 45, "extensions": ["ws", "wsc", "bin", "zip"]},
    {"name": "a800", "id": 0, "extensions": ["zip"]},
    {"name": "atari", "id": 0, "extensions": ["zip"]},
    {
        "name": "c64",
        "id": 66,
        "extensions": ["d64", "t64", "tap", "prg", "crt", "bin", "ark", "c64", "zip"],
    },
    {"name": "cps3", "id": 8, "extensions": ["zip", "chd", "ccd"]},
    {"name": "easyrpg", "id": 0, "extensions": ["zip"]},
    {"name": "fds", "id": 0, "extensions": ["zip"]},
    {"name": "gbc", "id": 10, "extensions": ["gb", "gbc", "bin", "zip"]},
    {"name": "hbmame", "id": 0, "extensions": ["zip"]},
    {"name": "md", "id": 1, "extensions": ["gen", "md", "smd", "bin", "sg", "zip"]},
    {"name": "n64", "id": 14, "extensions": ["n64", "v64", "z64", "bin", "zip"]},
    {"name": "neogeo", "id": 0, "extensions": ["zip"]},
    {"name": "ngc", "id": 13, "extensions": ["iso"]},
    {"name": "wii", "id": 16, "extensions": ["iso"]},
    {"name": "3ds", "id": 17, "extensions": ["3ds"]},

    {"name": "openbor", "id": 214, "extensions": ["pak", "zip"]},
    {"name": "pgm2", "id": 0, "extensions": ["zip"]},
    {
        "name": "saturn",
        "id": 22,
        "extensions": ["chd", "bin", "iso", "cue", "mdf", "m3u", "zip"],
    },
    {"name": "sfc", "id": 4, "extensions": ["sfc", "smc", "fig", "swc", "mgd", "zip"]},
    {"name": "vb", "id": 11, "extensions": ["vb", "bin", "vboy", "zip"]},
]


def get_system_id(system_name: str) -> int:
    for system in systems:
        if system["name"] == system_name:
            return system["id"]
    return -1


def get_system_extension(system_name: str) -> list[str]:
    for system in systems:
        if system["name"] == system_name:
            return system["extensions"]
    return []
