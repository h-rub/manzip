# manzip created by h-rub
# This program is distributed under the MIT License, you can use and modify if you want

import os
import zipfile
import click
import platform

@click.group()
def main():
    global path_slash
    global cwd
    global sys
    system = platform.system()
    cwd = os.getcwd()
    
    if system == "Windows":
        path_slash = "\\"
        sys = {"path_slash":path_slash, "cwd":cwd}
        return sys
    
    else:
        path_slash = "/"
        sys = {"path_slash":path_slash, "cwd":cwd}
        return sys

# Command to compress
@main.command(help="Compress a file/folder into a zip")
@click.option('--file', '-f', help="Folder/file to compress")
@click.option('--output', '-o', default='mzip', help="Name of the output zip, by default to be 'mzip'")
def compress(file, output):
    path_output_zip = sys['cwd']+sys['path_slash']+f'{output}.zip'
    dir_walk = os.walk(sys['cwd']+sys['path_slash']+f'{file}')
    zip_file = zipfile.ZipFile(path_output_zip, 'w')
    for folder, subfolder, files in dir_walk:
        for file in files:
            zip_file.write(os.path.join(folder,file),os.path.relpath(os.path.join(folder,file), cwd), compress_type=zipfile.ZIP_DEFLATED)
    print(f"Compressed succesfully => {path_output_zip}")

# Command to extract
@main.command(help="Extract a zip into a folder")
@click.option('--file', '-f', help="Zip file to extract")
@click.option('--output', '-o', default="", help="Path to te output zip file, by default to be the current directoy")
def extract(file, output):
    if output != '':
        path_output = output
        zip_file_to_extract = zipfile.ZipFile(file)
        zip_file_to_extract.extractall(path_output)
        zip_file_to_extract.close()
        return print(f"Files extracted succesfully => {path_output}")         
    else:
        path_zip = cwd+path_slash+file
        path_output = cwd
        zip_file_to_extract = zipfile.ZipFile(path_zip)
        zip_file_to_extract.extractall(path_output)
        zip_file_to_extract.close()
        return print(f"Files extracted succesfully => {path_output}")

if __name__ == "__main__":
    main()