from pathlib import Path
import graphic as gr
import input
import sys
import time
from anbernic import anbernic

from scraper import available_systems, get_image_files_without_extension, get_roms, load_config_from_json, scrape_screenshot
from systems import get_system_id

selected_position = 0
roms_selected_position = 0
selected_system = ""
current_window = "console"
max_elem = 11
an = anbernic.Anbernic()
skip_input_check = False

load_config_from_json("config.json")

def start():
	load_console_menu()

def update():
	global current_window, selected_position, skip_input_check

	if skip_input_check:
		input.reset_input()
		skip_input_check = False
	else:
		input.check()

	if input.key("MENUF"):
		gr.draw_end()
		sys.exit()
	
	if current_window == "console":
		load_console_menu()
	elif current_window == "roms":
		load_roms_menu()
	else:
		load_console_menu()

def load_console_menu():
	global rom_provider, selected_position, selected_system, current_window, skip_input_check

	console_available = available_systems(an.get_sd_storage_path())
 
	if  not console_available:
		gr.draw_clear()
		gr.draw_text((320, 240), "No roms found", anchor="mm")
		gr.draw_paint()
		time.sleep(3)
		gr.draw_clear()
		return

	if input.key("DY"):
		if input.value == 1:
			if selected_position < len(console_available) - 1:
				selected_position += 1
		elif input.value == -1:
			if selected_position > 0:
				selected_position -= 1
	elif input.key("A"):
		selected_system = console_available[selected_position][0]
		current_window = "roms"
		gr.draw_log("Searching roms...", fill=gr.colorBlue, outline=gr.colorBlueD1)
		gr.draw_paint()
		skip_input_check = True
		return

	gr.draw_clear()
	
	gr.draw_rectangle_r([10, 40, 630, 440], 15, fill=gr.colorGrayD2, outline=None)
	gr.draw_text((320, 20), "Tiny Scraper", anchor="mm")

	start_idx = int(selected_position / max_elem) * max_elem
	end_idx = start_idx + max_elem
	for i, c in enumerate(console_available[start_idx:end_idx]):
		row_list(c[0], (20, 50 + (i * 35)), 600, i == (selected_position % max_elem))

	button_circle((30, 460), "A", "Select")
	button_circle((133, 460), "M", "Exit")

	gr.draw_paint()

def load_roms_menu():
	global rom_provider, selected_position, current_window, roms_selected_position, skip_input_check, selected_system

	roms_list = get_roms(an.get_sd_storage_path(), selected_system)

	imgs_folder = Path(f"{an.get_sd_storage_path()}/{selected_system}/Imgs")
	if not imgs_folder.exists():
		imgs_folder.mkdir()
		imgs_files = []
	else:
		imgs_files = get_image_files_without_extension(imgs_folder)

	roms_without_image = [rom.name for rom in roms_list if rom.name not in imgs_files]
	system_id = get_system_id(selected_system)

	if len(roms_list) < 1:
		current_window = "console"
		gr.draw_clear()
		return

	if input.key("B"):
		current_window = "console"
		selected_system = ""
		gr.draw_clear()
		# gr.draw_paint()
		roms_selected_position = 0
		skip_input_check = True
		return
	elif input.key("A"):
		gr.draw_log("Scraping...", fill=gr.colorBlue, outline=gr.colorBlueD1)
		gr.draw_paint()
		rom = roms_list[roms_selected_position]
		
		screenshot = scrape_screenshot(
                game_name=rom.name, crc=rom.crc, system_id=system_id
            )
		if screenshot:
			img_path = f"{imgs_folder}/{rom.name}.png"
			with open(img_path, "wb") as img_file:
				img_file.write(screenshot)
		if screenshot:
			gr.draw_log("Scraping completed!", fill=gr.colorBlue, outline=gr.colorBlueD1)
		else:
			gr.draw_log("Scraping failed!", fill=gr.colorBlue, outline=gr.colorBlueD1)
		gr.draw_paint()
		time.sleep(3)
	elif input.key("START"):
		gr.draw_log("Scraping...", fill=gr.colorBlue, outline=gr.colorBlueD1)
		gr.draw_paint()
		for rom in roms_list:
			if rom.name not in imgs_files:
				screenshot = scrape_screenshot(
					game_name=rom.name, crc=rom.crc, system_id=system_id
				)
				if screenshot:
					img_path = f"{imgs_folder}/{rom.name}.png"
					with open(img_path, "wb") as img_file:
						img_file.write(screenshot)
					print(f"Done scraping {rom.name}.")
				else :
					print(f"Failed to get screenshot for {rom.name}")
		gr.draw_log("Scraping completed!", fill=gr.colorBlue, outline=gr.colorBlueD1)
		gr.draw_paint()
		time.sleep(3)
	elif input.key("Y"):
		an.switch_sd_storage()
	elif input.key("DY"):
		if input.value == 1:
			if roms_selected_position < len(roms_list) - 1:
				roms_selected_position += 1
		elif input.value == -1:
			if roms_selected_position > 0:
				roms_selected_position -= 1
	elif input.key("L1"):
		if roms_selected_position > 0:
			if roms_selected_position - max_elem >= 0:
				roms_selected_position = roms_selected_position - max_elem
			else:
				roms_selected_position = 0
	elif input.key("R1"):
		if roms_selected_position < len(roms_list) - 1:
			if roms_selected_position + max_elem <= len(roms_list) - 1:
				roms_selected_position = roms_selected_position + max_elem
			else:
				roms_selected_position = len(roms_list) - 1
	elif input.key("L2"):
		if roms_selected_position > 0:
			if roms_selected_position - 100 >= 0:
				roms_selected_position = roms_selected_position - 100
			else:
				roms_selected_position = 0
	elif input.key("R2"):
		if roms_selected_position < len(roms_list) - 1:
			if roms_selected_position + 100 <= len(roms_list) - 1:
				roms_selected_position = roms_selected_position + 100
			else:
				roms_selected_position = len(roms_list) - 1

	gr.draw_clear()

	gr.draw_rectangle_r([10, 40, 630, 440], 15, fill=gr.colorGrayD2, outline=None)
	gr.draw_text((320, 20), "Tiny Scraper", anchor="mm")
	gr.draw_text((320, 30), f"Console: {selected_system}, Roms: {len(roms_list)}", anchor="mm")
	gr.draw_text((320, 40), f"Roms without image: {len(roms_without_image)}", anchor="mm")
	

	start_idx = int(roms_selected_position / max_elem) * max_elem
	end_idx = start_idx + max_elem
	for i, rom in enumerate(roms_list[start_idx:end_idx]):
		row_list(rom.name[0] if len(rom.name[0]) <= 50 else rom.name[0][:48] + "...", (20, 50 + (i * 35)), 600, i == (roms_selected_position % max_elem))
	
	button_circle((30, 460), "Start", "Download All")
	button_circle((170, 460), "A", "Download")
	button_circle((260, 460), "B", "Back")
	button_circle((355, 460), "Y", "SD: {}".format(an.get_sd_storage()))
	button_circle((460, 460), "M", "Exit")

	gr.draw_paint()

def row_list(text, pos, width, selected):
	gr.draw_rectangle_r([pos[0], pos[1], pos[0]+width, pos[1]+32], 5, fill=(gr.colorBlue if selected else gr.colorGrayL1))
	gr.draw_text((pos[0]+5, pos[1] + 5), text)

def button_circle(pos, button, text):
	gr.draw_circle(pos, 15, fill=gr.colorBlueD1)
	gr.draw_text(pos, button, anchor="mm")
	gr.draw_text((pos[0] + 20, pos[1]), text, font=13, anchor="lm")