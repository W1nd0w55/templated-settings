# templated-settings
Templated settings generator written in Python


# Usage
## As is
```
python(3) generate_settings.py project-path [-c CONFIG] [-C CONFIG-FILE] [-s SOURCE] [-o OUT]
```

Default values are:
    -c (first one defined)
    -C (project-path)/ProjectConfigs.json
    -s (project-path)/ProjectSettings.py
    -o (project-path)/settings

## Compiled with nuitka
```
pip(3) install nuitka
nuitka ./generate_settings.py
```
