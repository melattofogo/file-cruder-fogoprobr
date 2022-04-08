from . import check
import os

def dir(directory, file_path):
    """
    Signature:
    ----------
    add.dir(
        directory: 'str',
        file_path: 'str'
    )

    Docstring:
    ----------
    cria pasta 'directory' na mesma pasta de 'file_path'
    'file_path' é referencia de onde criar a pasta e
    pode ser __file__
    
    Parameters:
    ----------
    directory: Nome da pasta que será criada
    file_path: Path de referencia para criar a pasta 'directory'. Deve ser realpath (path completo) até a pasta [ou arquivo na] onde a pasta 'directory' será criada. Pode ser __file__ para criar pasta em './'

    """
    parent_dir = os.path.dirname(os.path.abspath(file_path))
    if check.isfile(file_path):
        parent_dir = os.path.dirname(os.path.abspath(file_path))
    elif check.isfolder(file_path):
        parent_dir = os.path.abspath(file_path)
    else:
        raise Exception('Invalid file_path. Make sure file or folder existis')
    
    path = os.path.join(parent_dir, directory)

    if not os.path.isdir(path):
        print(path)
        os.mkdir(path)
        print("Pasta '% s' criada" % directory)
        return True
    else:
        print("Pasta '% s' já existe" % directory)
        return False
