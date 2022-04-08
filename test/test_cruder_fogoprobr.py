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
from fogoprobr import add
from fogoprobr import remove


valid_files = [os.path.join(relative_path, 'folder', 'file.txt'), os.path.join(test_folder_path, 'folder', 'file.txt')]
valid_folders = [os.path.join(relative_path, 'folder'), os.path.join(test_folder_path,'folder')]

valid_paths = valid_files + valid_folders

invalid_files = [os.path.join(relative_path, 'folder', 'fake-file.txt'), os.path.join(test_folder_path, 'folder', 'fake-file.txt')]
invalid_folders = [os.path.join(relative_path, 'fake-folder'), os.path.join(test_folder_path,'fake-folder')]

invalid_paths = invalid_files + invalid_folders

# testa arquivos validsos
def test_valid_file():
    for valid_scope in valid_files:
        assert check.isfile(valid_scope) is True, "check.isfile({}) is {}".format(valid_scope, check.isfile(valid_scope))

# testa pastas validas como arquivos invalidsos
def test_invalid_file_with_folders():
    for invalid_scope in valid_folders:
        assert check.isfile(invalid_scope) is False, "check.isfile({}) is {}".format(invalid_scope, check.isfile(invalid_scope))

# testa arquivos invalidas
def test_invalid_file_with_files():
    for invalid_scope in invalid_files:
        assert check.isfile(invalid_scope) is False, "check.isfile({}) is {}".format(invalid_scope, check.isfile(invalid_scope))

# testa pastas validas
def test_valid_folder():
    for valid_scope in valid_folders:
        assert check.isfolder(valid_scope) is True, "check.isfolder({}) is {}".format(valid_scope, check.isfile(valid_scope))

# testa arquivos validos como pastas invalidsos
def test_invalid_folder_with_files():
    for invalid_scope in valid_files:
        assert check.isfolder(invalid_scope) is False, "check.isfolder({}) is {}".format(invalid_scope, check.isfile(invalid_scope))

# testa pastas invalidas
def test_invalid_folder_with_folders():
    for invalid_scope in invalid_folders:
        assert check.isfolder(invalid_scope) is False, "check.isfolder({}) is {}".format(invalid_scope, check.isfile(invalid_scope))

# testa existencia de paths
def test_valid_path():
    for valid_scope in valid_paths:
        assert check.exists(valid_scope) is True, "check.exists({}) is {}".format(valid_scope, check.isfile(valid_scope))

# testa inexistencia de paths
def test_invalid_path():
    for invalid_scope in invalid_paths:
        assert check.exists(invalid_scope) is False, "check.exists({}) is {}".format(invalid_scope, check.isfile(invalid_scope))

# testa criacao de pasta
def test_mkdir():
    assert add.dir('test-folder', __file__) is True, "add.dir('test-folder', {})".format(__file__)

# testa remocao de pasta
def test_rmdir():
    assert remove.dir('test-folder', __file__) is True, "remove.dir('test-folder', {})".format(__file__)