# Manzip - Compress and extract easily and fast

Installation

```
python3 -m venv env
source env/bin/activate
python3 -m pip install --editable .

manzip --help
```

## Usage

manzip [OPTIONS] COMMAND [ARGS]...

Options:
--help  Show this message and exit.

Commands:
compress  Compress a file/folder into a zip
extract   Extract a file/folder into a zip

### Compress

Usage: manzip compress [OPTIONS]

Compress a file/folder into a zip

Options:
-f, --file TEXT    Folder/file to compress
-o, --output TEXT  Name of the output zip, by default 'fzip'
--help             Show this message and exit.

### Example:

Compress a folder named "images_original" that containts images jpg into, If the output is empty by default is mzip

```
manzip compress -f images_original
```

To create the zip with another name you can use the option "—output", or "-o" followed by the file name output zip, it's not necessary that you specify the extension .zip, manzip does it for you

```
python app.py compress -f images_original -o salida
```

### Extact

Usage: manzip extract [OPTIONS]

Extract a zip into a folder

Options:
-f, --file TEXT    Zip file to extract
-o, --output TEXT  Path to te output zip file, by default current directoy
--help             Show this message and exit.

### Example:

If the parameter output is empty by default to be the current directory

```
python app.py extract --file mzip.zip
```

You can specify another path to save the output

```
python app.py extract --file fzip.zip -o /Users/hever/dev
```