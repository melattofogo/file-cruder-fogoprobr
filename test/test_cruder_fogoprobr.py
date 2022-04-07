import sys
import os

# full path para este script
file_path = os.path.realpath(__file__)
# full path para pasta deste script
test_folder_path = os.path.dirname(os.path.realpath(__file__))
# full path para pasta root do proj (2 naveis acima)
proj_root_path = os.path.dirname(test_folder_path)
# path deste script relativo a getcwd (path do terminal) 
relative_path = os.path.relpath(test_folder_path, os.getcwd())

# adiciona caminho a root do projeto em sys.path para import reconhecer fogoprobr
sys.path.append(proj_root_path)
from fogoprobr import check

valid_files = [os.path.join(relative_path, 'folder', 'file.txt'), os.path.join(test_folder_path, 'folder', 'file.txt')]
valid_folders = [os.path.join(relative_path, 'folder'), os.path.join(test_folder_path,'folder')]

valid_paths = valid_files + valid_folders

invalid_files = [os.path.join(relative_path, 'folder', 'fake-file.txt'), os.path.join(test_folder_path, 'folder', 'fake-file.txt')]
invalid_folders = [os.path.join(relative_path, 'fake-folder'), os.path.join(test_folder_path,'fake-folder')]

invalid_paths = invalid_files + invalid_folders

# testa arquivos validsos
def test_valid_file():
    for valid_scope in valid_files:
        assert check.isfile(valid_scope) is True

# testa pastas validas como arquivos invalidsos
def test_invalid_file_with_folders():
    for invalid_scope in valid_folders:
        assert check.isfile(invalid_scope) is False

# testa arquivos invalidas
def test_invalid_file_with_files():
    for invalid_scope in invalid_files:
        assert check.isfile(invalid_scope) is False

# testa pastas validas
def test_valid_folder():
    for valid_scope in valid_folders:
        assert check.isfolder(valid_scope) is True

# testa arquivos validos como pastas invalidsos
def test_invalid_folder_with_files():
    for invalid_scope in valid_files:
        assert check.isfolder(invalid_scope) is False

# testa pastas invalidas
def test_invalid_folder_with_folders():
    for invalid_scope in invalid_folders:
        assert check.isfolder(invalid_scope) is False

# testa existencia de paths
def test_valid_path():
    for valid_scope in valid_paths:
        assert check.exists(valid_scope) is True

# testa inexistencia de paths
def test_invalid_path():
    for invalid_scope in invalid_paths:
        assert check.exists(invalid_scope) is False