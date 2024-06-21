systems = [
    {"name": "A5200", "id": 1, "extensions": []},
    {"name": "AMIGA", "id": 64, "extensions": ["adf","dms","zip","lha","lzh","hdf","hdz","hdf","hd","hds","hfe","ipf","uae","adf","dms","zip","lha","lzh","hdf","hdz","hdf","hd","hds","hfe","ipf","uae"]},
    {"name": "ATARIST", "id": 1, "extensions": []},
    {"name": "CPS1", "id": 1, "extensions": []},
    {"name": "DOS", "id": 1, "extensions": []},
    {"name": "FBNEO", "id": 1, "extensions": []},
    {"name": "GB", "id": 9, "extensions": ["gb", "bin"]},
    {"name": "GG", "id": 1, "extensions": []},
    {"name": "LYNX", "id": 1, "extensions": []},
    {"name": "MDCD", "id": 1, "extensions": []},
    {"name": "NAOMI", "id": 56, "extensions": ["chd", "bin", "gdi", "raw"]},
    {"name": "NGP", "id": 1, "extensions": []},
    {"name": "PCE", "id": 1, "extensions": []},
    {"name": "PICO", "id": 234, "extensions": ["p8", "png"]},
    {"name": "PS", "id": 57, "extensions": ["bin","img","mdf","iso","cue","ccd","pbp","chd","m3u","toc","cbn","sub","ccd"]},
    {"name": "SCUMMVM", "id": 1, "extensions": []},
    {"name": "SMS", "id": 2, "extensions": ["sms,bin"]},
    {"name": "VIC20", "id": 1, "extensions": []},
    {"name": "A7800", "id": 1, "extensions": []},
    {"name": "ATOMISWAVE", "id": 1, "extensions": []},
    {"name": "CPS2", "id": 1, "extensions": []},
    {"name": "DREAMCAST", "id": 23, "extensions": ["cdi","gdi","chd","bin","gdi"]},
    {"name": "FC", "id": 3, "extensions": ["nes","fds","unf","unif","nez","nsf","nez"]},
    {"name": "GBA", "id": 12, "extensions": ["gba","bin"]},
    {"name": "GW", "id": 52, "extensions": ["mgw"]},
    {"name": "MAME", "id": 75, "extensions": ["zip","chd","bin"]},
    {"name": "MSX", "id": 1, "extensions": []},
    {"name": "NDS", "id": 15, "extensions": ["nds","bin"]},
    {"name": "ONS", "id": 1, "extensions": []},
    {"name": "PCECD", "id": 1, "extensions": []},
    {"name": "POKE", "id": 211, "extensions": ["min"]},
    {"name": "PSP", "id": 1, "extensions": []},
    {"name": "SEGA32X", "id": 1, "extensions": []},
    {"name": "VARCADE", "id": 1, "extensions": []},
    {"name": "WS", "id": 45, "extensions": ["ws","wsc","bin"]},
    {"name": "A800", "id": 1, "extensions": []},
    {"name": "ATARI", "id": 1, "extensions": []},
    {"name": "C64", "id": 1, "extensions": []},
    {"name": "CPS3", "id": 1, "extensions": []},
    {"name": "EASYRPG", "id": 1, "extensions": []},
    {"name": "FDS", "id": 1, "extensions": []},
    {"name": "GBC", "id": 10, "extensions": ["gb","gbc","bin"]},
    {"name": "HBMAME", "id": 1, "extensions": []},
    {"name": "MD", "id": 1, "extensions": ["gen","md","smd","bin","sg"]},
    {"name": "N64", "id": 14, "extensions": ["n64", "v64", "z64", "bin"]},
    {"name": "NEOGEO", "id": 1, "extensions": []},
    {"name": "OPENBOR", "id": 214, "extensions": ["pak"]},
    {"name": "PGM2", "id": 1, "extensions": []},
    {"name": "SATURN", "id": 22, "extensions": ["chd","bin","iso","cue","mdf","m3u"]},
    {"name": "SFC", "id": 4, "extensions": ["sfc","smc","fig","swc","mgd", "zip"]},
    {"name": "VB", "id": 11, "extensions": ["vb", "bin", "vboy"]},
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