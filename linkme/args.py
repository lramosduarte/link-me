import argparse

from collections import namedtuple

from linkme.commands.unread import exibe_links_nao_lidos
from linkme.commands.upload import upload_file


Args = namedtuple('Args', ['positionals', 'optionals', 'command'])
ARGS_OPTIONALS = (
    Args(
        positionals=('--uploader', '-U'),
        optionals={'help': 'Informe um custom script para envio dos bookmarks'},
        command=None,
    ),
)

ARGS_POSITIONALS = (
    Args(
        positionals='unread',
        optionals={
            'help': 'Show unread links on bookmarks.',
        },
        command=exibe_links_nao_lidos,
    ),
    Args(
        positionals='upload',
        optionals={
            'help': 'Send bookmarks file to destination specified by uploader engine.',
        },
        command=upload_file,
    ),
)


class InitiatorArgs:
    DADOS_INICIAIS_ARGS = {
        'description': 'Linkme funciona como um armazenador de links(favoritos)',
    }

    def __init__(self):
        self.parser = argparse.ArgumentParser(**self.DADOS_INICIAIS_ARGS)

        self._inicia_argumentos_aceitos()

    def _inicia_argumentos_aceitos(self):
        for _args in ARGS_OPTIONALS:
            self.parser.add_argument(*_args.positionals, **_args.optionals)

        subparsers = self.parser.add_subparsers(title='Commands', metavar='')
        for _args in ARGS_POSITIONALS:
            subparser = subparsers.add_parser(_args.positionals, **_args.optionals)
            subparser.set_defaults(commands=_args.positionals)

    def start(self, args):
        return self.parser.parse_args(args)
