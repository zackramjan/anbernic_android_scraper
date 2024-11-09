import sys
import app
from scraper import Scraper
from systems import get_system_id
from pathlib import Path

scraper = Scraper()

def main():
    
    path = sys.argv[1]
    scraper.load_config_from_json(path)
    available_systems = scraper.get_available_systems(scraper.romspath)
    for selected_system in available_systems:
        print(f"generating gamelist.xml for  {selected_system} ...")
        roms_list = scraper.get_roms(scraper.romspath, selected_system)
        f = open(f"{scraper.romspath}/{selected_system}/gamelist.xml","w")
        f.write("<gameList>\n")
        for rom in roms_list:
            f.write("<game>\n")
            imgPath = Path(f"{rom.filename}")
            f.write(f"   <path>{rom.filename}</path>\n")
            f.write(f"   <name>{rom.filename}</name>\n")
            f.write(f"   <desc>{rom.filename}</desc>\n")
            f.write(f"   <image>{scraper.imagedir}/{imgPath.stem}.png</image>\n")
            f.write("</game>\n")
        f.write("<gameList>\n")
        f.close()


if __name__ == "__main__":
    main()


