# templated-settings
Templated settings generator written in Python

# Usage
## As is
```
python(3) generate_settings.py project-path [-c CONFIG] [-C CONFIG-FILE] [-s SOURCE] [-o OUT]
```

Default values are:\
    * -c (first one defined)\
    * -C (project-path)/ProjectConfigs.json\
    * -s (project-path)/ProjectSettings.jinja\
    * -o (project-path)/settings

## Compiled with nuitka
```
pip(3) install nuitka
nuitka ./generate_settings.py --no-deployment-flag=self-execution
```

# Example
```
python(3) generate_settings.py ./example -o settings.py -c (Dev|Prod)
```
