import pytest
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

def get_lines(path):
    file = open(path, 'r')
    lines = file.readlines()
    file.close()
    return lines

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

# testa erro de arquivo inexitente para add.patch
def test_exception_invalid_path_add_patch():
    for invalid_scope in invalid_files:
        with pytest.raises(Exception) as exception_info:
            add.patch(invalid_scope, 1)
        assert "Invalid file path" in str(exception_info.value)

# testa erro de arquivo inexitente para remove.patch
def test_exception_invalid_path_remove_patch():
    for invalid_scope in invalid_files:
        with pytest.raises(Exception) as exception_info:
            remove.patch(invalid_scope, 1)
        assert "Invalid file path" in str(exception_info.value)

# testa erro de linha maior do que o tamanho do arquivo para add.patch
def test_exception_row_add_patch():
    for valid_scope in valid_files:
        with pytest.raises(Exception) as exception_info:
            add.patch(valid_scope, 2, 'linha 2')
        assert "Row out of range" in str(exception_info.value)

# testa erro de linha maior do que o tamanho do arquivo para remove.patch
def test_exception_row_remove_patch():
    for valid_scope in valid_files:
        with pytest.raises(Exception) as exception_info:
            remove.patch(valid_scope, 6)
        assert "Row out of range" in str(exception_info.value)

# testa add.path em arquivo em branco
def test_add_patch_content_in_blank_file():
    add.patch(valid_files[0], 1, 'content in blank file')
    lines = get_lines(valid_files[0])
    assert lines[0] == 'content in blank file\n'

# testa add.path na ultima linha
def test_add_patch_content_in_last_row():
    add.patch(valid_files[0], 2, 'content in last row')
    lines = get_lines(valid_files[0])
    assert lines[1] == 'content in last row\n'

# testa add.path no intervalo de linhas
def test_add_patch_content_in_row_range():
    add.patch(valid_files[0], 2, 'content in row range')
    lines = get_lines(valid_files[0])
    assert (lines[1] == 'content in row range\n') and (lines[2] == 'content in last row\n')

# testa add.path retorna True ao executar
def test_add_patch_return_true():
    assert add.patch(valid_files[0], 1, 'return True') is True

# testa remove.path no intervalo de linhas
def test_remove_patch_content_in_row_range():
    remove.patch(valid_files[0], 3)
    lines = get_lines(valid_files[0])
    assert (lines[0] == 'return True\n') and (lines[1] == 'content in blank file\n') and (lines[2] == 'content in last row\n') and (len(lines) == 3), "lines = {}".format(lines)

# testa remove.path na ultima linha
def test_remove_patch_content_in_last_row():
    remove.patch(valid_files[0], 3)
    lines = get_lines(valid_files[0])
    assert lines[0] == 'return True\n' and lines[1] == 'content in blank file\n' and len(lines) == 2, "lines = {}".format(lines)

# testa remove.path até arquivo estar em branco
def test_remove_patch_content_to_blank_file():
    while len(get_lines(valid_files[0])) > 0:
        remove.patch(valid_files[0], 1)
    lines = get_lines(valid_files[0])
    assert len(lines) == 0, "lines = {}".format(lines)