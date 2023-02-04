from argparse import ArgumentParser, FileType
import subprocess

from . import chimera, pegasus, zephyr


COMMANDS = [chimera, pegasus, zephyr]


def main(args=None):
    parser = ArgumentParser()

    parent_parser = ArgumentParser(add_help=False)
    parent_parser.add_argument("--output", type=FileType("w"), default="-")
    parent_parser.add_argument(
        "--scale",
        type=float,
        help=(
            "Scale of the picture (see D-Wave Networkx docs for precise meaning). By default, "
            "it is set to 7.0 for Zephyr and 30.0 for Pegasus and Chimera, which seems to look "
            "reasonably well."
        )
    )
    parent_parser.add_argument(
        "--compile",
        action="store_true",
        default=False,
        help=(
            "Whether to compile the output file just after producing it. Needs --output to be "
            "specified, and latexmk to be installed"
        )
    )
    parent_parser.add_argument(
        "--with-labels",
        action="store_true",
        default=False,
        dest="with_labels",
        help=(
            "Output labels (number) of nodes. This will probably require you do do sme extensive "
            "work when adjusting styles in tikz."
        )
    )
    subcommands = parser.add_subparsers(title="topology", required=True)

    for command in COMMANDS:
        cmd_parser = subcommands.add_parser(name=command.COMMAND_NAME, parents=[parent_parser])
        command.add_args(cmd_parser)
        cmd_parser.set_defaults(
            fill_dynamic_defaults=command.fill_dynamic_defaults,
            generate=command.generate
        )

    args = parser.parse_args(args)

    args.fill_dynamic_defaults(args)
    args.generate(args)

    if args.compile:
        args.output.close()
        subprocess.run(["latexmk", "-cd", "-pdf", args.output.name])
