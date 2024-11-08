from pathlib import Path
from typing import List, Optional
from scraper import Scraper
from systems import get_system_id

selected_system = ""
current_window = "console"
max_elem = 11
scraper = Scraper()
skip_input_check = False


def start(config_path: str) -> None:
    print("Starting Tiny Scraper...")
    scraper.load_config_from_json(config_path)
    process()


def process() -> None:
    available_systems = scraper.get_available_systems(scraper.romspath)
    for selected_system in available_systems:
        roms_list = scraper.get_roms(scraper.romspath, selected_system)
        system_path = Path(scraper.romspath) / selected_system
        imgs_folder = Path(f"{scraper.romspath}/{selected_system}/{scraper.imagedir}")

        if not imgs_folder.exists():
            imgs_folder.mkdir()
            imgs_files: List[str] = []
        else:
            imgs_files = scraper.get_image_files_without_extension(imgs_folder)

        roms_without_image = [rom for rom in roms_list if rom.name not in imgs_files]
        system_id = get_system_id(selected_system)

        if len(roms_without_image) < 1:
            print(f"{selected_system} already has images  for all roms...")
            continue;
     
        for rom in roms_without_image:
            if rom.name not in imgs_files:
                rom.set_crc(scraper.get_crc32_from_file(system_path / rom.filename))
                screenshot: Optional[bytes] = scraper.scrape_screenshot(
                    game_name=rom.name, crc=rom.crc, system_id=system_id
                )
                if screenshot:
                    img_path: Path = imgs_folder / f"{rom.name}.png"
                    img_path.write_bytes(screenshot)
                    print(f"Done scraping {rom.name}. Saved file to {img_path}")
                    success += 1
                else:
                    print(f"Failed to get screenshot for {rom.name}")
   