from json import loads as load_json
from jinja2 import Environment, FileSystemLoader
from sys import argv
from argparse import ArgumentParser

def main() -> None:
    parser = ArgumentParser(prog=argv[0])
    
    parser.add_argument('project-path')
    parser.add_argument('-c', '--config')
    parser.add_argument('-C', '--config-file')
    parser.add_argument('-s', '--source')
    parser.add_argument('-o', '--out')

    # Get arguments as a dictionary
    args = vars(parser.parse_args())

    # Set default value if not present
    args['config_file'] = args['config_file'] or 'ProjectConfigs.json'
    args['source'] = args['source'] or 'ProjectSettings.jinja'
    args['out'] = args['out'] or 'settings'

    # Load the configuration file
    with open(f'{args['project-path']}/{args['config_file']}', 'r') as f:
        configs = load_json(f.read())

    # The default configuration will be the first one defined
    args['config'] = args['config'] or configs['configs'][0]

    # Jinja setup
    env = Environment(loader=FileSystemLoader(args['project-path']))
    content = env.get_template(args['source']).render(config=args['config'])

    # Finally
    with open(f'{args["project-path"]}/{args['out']}', 'w') as f:
        f.write(content)

if (__name__ == '__main__'): main()
