# This is a FORK of https://github.com/Julioevm/tiny-scraper that attemps to make things generic and command line, suitable for mac/pc/android 

# Tiny Scraper

![Platform](https://img.shields.io/badge/platform-Anbernic-orange.svg)

A small utility to scrape game covers for a generic folder structure, as found on anbernic android devices such as RG406V, RG556, etc

## Features

- **Easy Downloads:** Download cover media directly onto your Anbernic device.
- **User-Friendly Interface:** Simple and intuitive interface designed specifically for Anbernic devices.
- **Wide Compatibility:** Supports various ROM file types and multiple Anbernic models.

## Supported Devices

I've personally only tested it on the RG406V SD card structure


#
3. **Setup config**
   - create a `config.json` file inside the `tiny_scraper` folder with a valid user and password from https://www.screenscraper.fr. Register if you haven't.
   - the roms path is the path to your top level sdcard that contains the subfolders for your various platforms (ex: cps1, ss, gba, etc)
   - imagedir is the subfolder that we will store your downloaded images into. 
```
{
    "user": "your_user",
    "password": "your_password",
    "media_type": "sstitle",
    "region": "us"
    "romspath": "/Volumes/emuroms/,
    "imagedir": "images"
}
```

- Media type let's you select the type of media to download: The main options I suggest are `ss` for a game screenshot, `sstitle`, for the title screen or `box-2D` or `box-3D` for a box, `mixrbv1` for a mix of screenshot, wheel and so on. For more options check the screenscraper.fr documentation. Keep the capital letters.
- Region let's you prioritize the region of the media to download. Some games have different covers for Japan, some for Europe and some for the rest of the world. If the region is not specified it will prioritize the world covers. Valid regions are `wor`, `jp`, `eu`, `asi`, `kr`, `ss`, `us`.

3. **Start Tiny Scraper:**
   - Plug in your sdcard and run tiny.scraper.sh


## Troubleshooting


