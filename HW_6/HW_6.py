from pathlib import Path
import re
import shutil
import sys

file_list = []

def selected_folder():
    return sys.argv[1]
    

def normalize(name):
    CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
    TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
                   "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

    TRANS = {}

    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()

    name = re.sub(r'\W', '_', name)
    return (name.translate(TRANS))

def sort(path = selected_folder()):
    path = Path(path)
    global file_list
    
    for i in path.iterdir():
        
        if i.is_dir():
            sort(i)
       
        if i.is_file():
            k = normalize(Path(i).stem)+i.suffix
            i = i.rename(i.with_name(k))
            file_list.append(i) 
    
    return file_list

def sort_files_to_def_folders(file_list = sort(), path = selected_folder()):
    dirs_list = ['images', 'documents', 'audio', 'video', 'archives', 'unknown']
    video_ext = ('.AVI', '.MP4', '.MOV', '.MKV')
    images_ext = ('.JPEG', '.PNG', '.JPG', '.SVG')
    audio_ext = ('.MP3', '.OGG', '.WAV', '.AMR')
    documents_ext = ('.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.PPTX')
    archives_ext = ('.ZIP', '.GZ', '.TAR')

    for folder in dirs_list:
        path = Path.home() / 'Sorted_files' / folder
        sorted_files = Path.home() / 'Sorted_files'
 
        path.mkdir(parents=True, exist_ok=True)
        
    for file in file_list:
        ext = str(file.suffix).upper()
        if ext in video_ext:
            shutil.move(file, Path.home()/'Sorted_files'/'video')
        elif ext in images_ext:
            shutil.move(file, Path.home()/'Sorted_files'/'images')
        elif ext in audio_ext:
            shutil.move(file, Path.home()/'Sorted_files'/'audio')
        elif ext in documents_ext:
            shutil.move(file, Path.home()/'Sorted_files'/'documents')
        elif ext in archives_ext:
            shutil.move(file, Path.home()/'Sorted_files'/'archives')
        else:
            shutil.move(file, Path.home()/'Sorted_files'/'unknown')
    print(f'All yours files are sorted here: {sorted_files}')

def remove_empty_folders(pth = Path(selected_folder())):
    
    for child in pth.iterdir():
        remove_empty_folders(child)
    pth.rmdir()


def archive_unpack(c=Path(Path.home()/'Sorted_files'/'archives')):

    for arch in c.iterdir():
        t = str(Path.home()/'Sorted_files'/'archives') + '/' + Path(arch).stem
        shutil.unpack_archive(arch, t)


sort_files_to_def_folders()
remove_empty_folders()
archive_unpack()