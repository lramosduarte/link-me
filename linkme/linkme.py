import sys

from linkme.args import InitiatorArgs, ACTIONS


def main():
    initiator = InitiatorArgs()
    args = initiator.start(sys.argv[1:])
    if hasattr(args, 'commands'):
        ACTIONS[args.commands]()
