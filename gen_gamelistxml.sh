#!/bin/bash

. /mnt/mod/ctrl/configs/functions &>/dev/null 2>&1
progdir=$(cd $(dirname "$0"); pwd)

program="python3 ${progdir}/tiny_scraper/generate_gamelistxml.py ${progdir}/tiny_scraper/config.json"
log_file="${progdir}/tiny_scraper/gamelist_log.txt"

$program > "$log_file" 2>&1