# teste

Instalação do ```pytest```
```
pip install commitizen
```

Executar testes
```
pytest
```

# commitizen

Instalação do ```commitizen```
```
pip install commitizen
```

Instalação do cz ```cz_fogoprobr```
```
pip install commitizen-cz-fogoprobr
```

Alias para commit usando ```cz_fogoprobr```
```
git config alias.czf "cz --name=cz_fogoprobr commit"
```

# log

Alias para log usando ```--oneline```
```
git config alias.l "log --oneline"
```

# status

Alias para status
```
git config alias.l "status"
```

# version

Instalação do ```bumpversion```
```
pip install bumpversion
```

Atualização ```major``` (major, minor ou patch) da versão atual ```1.0.0``` nos arquivos ```setup.py``` e ```filecruder_fogoprobr/__init__.py```
```
bumpversion --current-version 1.0.0 major setup.py filecruder_fogoprobr/__init__.py
```

## tag

Cria ```tag``` *local*
```
git tag -a v.0.0.0 [commit-hash] -m "Release 0.0.0"
```

Push de tags locais para remote
```
git push --tags
```

Lista ```tag``` *local*
```
git tag -l
```

Deleta ```tag``` *local*
```
git tag -d v.0.0.0
```

Deleta ```tag``` em *remote*
```
git push --delete origin v.0.0.0
```

# publishing

Instalação do ```twine```
```
pip install twine
```

Publish em ```test.pypi.org```
```
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

Publish em ```pypi.org```
```
twine upload dist/*
```

## building
```
python setup.py sdist bdist_wheel
```

## check

Avaliação do *build* em ```dist/```
```
twine check dist/*
```