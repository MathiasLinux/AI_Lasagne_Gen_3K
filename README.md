# AI Lasagne Generator 3000

## Table of Contents

- [About](#about)
- [Technologies](#technologies)
- [Setup](#setup)
- [Build](#build)
- [Features](#features)
- [Status](#status)
- [License](#license)
- [Thanks](#thanks)

## About

This projet is a GUI to create products on a Prestashop website. It used the Serge API, the Stable Diffusion API and the Prestashop API. It was made for a College project. It create products using the Serge AI for the text and the Stable Diffusion AI for the images.

## Technologies

<a href="https://www.python.org/" title="Python"><img src="https://github.com/get-icon/geticon/raw/master/icons/python.svg" alt="Python" width="64px" height="64px"></a>
<a href="https://www.prestashop.com/" title="PrestaShop"><img src="https://github.com/get-icon/geticon/raw/master/icons/prestashop.svg" alt="PrestaShop" width="64px" height="64px"></a>

## Setup

You can run this projet from the source code of the GUI or from the executable file.

### From the source code

1. Clone the repository
2. Install the dependencies with `pip install -r requirements.txt`
3. Install my fork of the Prestashop module by getting the release from [here](https://github.com/MathiasLinux/prestashop/releases/tag/v0.1.5a) and install it in this project's folder
    1. Download the release
    2. Unzip it in the root folder of this project
    3. Go in it and run `pip install .`
4. Run the GUI with `python gui.py` or `python3 gui.py` (depending on your system)

### From the executable file
Go in the release section of this repository and download the latest release. Then, run the executable file.

Please note that the executable file is only available for Windows and Linux. The Windows setup is not signed.

## Build

To build the executable file, I have used [auto-py-to-exe]("https://pypi.org/project/auto-py-to-exe/") which is a GUI for PyInstaller. You can find the configuration file in the root folder of this project.

P.S. : The configuration file won't work if you don't change the path of the different files (gui.py and the images).

1. Install auto-py-to-exe with `pip install auto-py-to-exe`
2. Run `auto-py-to-exe` (You can specify a build folder with `auto-py-to-exe -bdo ./build` (The folder must exist)
3. Select the configuration file
4. Change the path of the different files
5. Click on "Convert .py to .exe"

If you want to avoid the false positive of Windows Defender, you can rebuild the bootloader of Pyinstaller [here](https://www.pyinstaller.org/en/stable/bootloader-building.html).

If you want an installer, like me, you can use [Inno Setup](https://jrsoftware.org/isinfo.php). You can find my configuration file in the root folder of this project. You have to modify the path of the different files. You also have to add certain information about your project and also a GUID. You can find more information [here](https://jrsoftware.org/ishelp/index.php?topic=scriptsetupsection).

## Features

- Easy configuration of the different APIs (even with an Apache Authentification)
- You can get the last created products from the Prestashop API
- You can create one or multiple products at once (up to 100)
- The created products have 4 images
- You can Specify the category of the products
- You can specify a product to generate
- The advance of the generation is displayed in the GUI

## Status

This project is finished but the only language available is French.

## License

This project is under the GNU GPLv3 license. See the [LICENSE](LICENSE) file for more information.

## Thanks

Thanks to [Serge](https://github.com/serge-chat/serge) and Stable Diffusion especially to [Stable Diffusion webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui) for their amazing work. Also thanks to [Prestashop]("https://prestashop.fr") for their amazing CMS.