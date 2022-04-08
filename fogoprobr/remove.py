from . import check
import os
import shutil

def dir(directory, file_path):
    """
    Signature:
    ----------
    remove.dir(
        directory: 'str',
        file_path: 'str'
    )

    Docstring:
    ----------
    Remove pasta 'directory' na mesma pasta de 'file_path'
    'file_path' é referencia de onde remover a pasta e
    pode ser __file__
    
    Parameters:
    ----------
    directory: Nome da pasta que será removida
    file_path: Path de referencia para remover a pasta 'directory'. Deve ser realpath (path completo) até a pasta [ou arquivo na] onde a pasta 'directory' será removida. Pode ser __file__ para criar pasta em './'

    """
    parent_dir = os.path.dirname(os.path.abspath(file_path))
    if check.isfile(file_path):
        parent_dir = os.path.dirname(os.path.abspath(file_path))
    elif check.isfolder(file_path):
        parent_dir = os.path.abspath(file_path)
    else:
        raise Exception('Invalid file_path. Make sure file or folder existis')
    
    path = os.path.join(parent_dir, directory)

    if os.path.isdir(path):
        print(path)
        shutil.rmtree(path)
        print("Pasta '% s' removida" % directory)
        return True
    else:
        print("Pasta '% s' não existe" % directory)
        return False
