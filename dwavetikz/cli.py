from argparse import ArgumentParser, FileType
import subprocess

from .chimera import generate_chimera_picture
from .pegasus import generate_pegasus_picture
from .zephyr import generate_zephyr_picture


def main():
    parser = ArgumentParser()

    parent_parser = ArgumentParser(add_help=False)
    parent_parser.add_argument("--output", type=FileType("w"), default="-")
    parent_parser.add_argument(
        "--compile",
        action="store_true",
        default=False,
        help=(
            "Whether to compile the output file just after producing it. Needs --output to be "
            "specified, and latexmk to be installed"
        )
    )
    subcommands = parser.add_subparsers(title="topology", required=True)

    chimera = subcommands.add_parser("chimera", parents=[parent_parser])
    chimera.add_argument("n", type=int, help="The number of rows in the Chimera graph")
    chimera.add_argument(
        "-m",
        type=int,
        help=(
            "The number of columns in the Chimera graph. "
            "If not provided, defaults to the number of rows."
        )
    )
    chimera.add_argument(
        "-t",
        type=int,
        help=(
            "Shore size of the Chimera unit cell. "
            "If not provided, the default shore size of 4 will be used."
        )
    )

    pegasus = subcommands.add_parser("pegasus", parents=[parent_parser])
    pegasus.add_argument("n", type=int, help="Size of the Pegasus graph")
    pegasus.add_argument(
        "--cross",
        action="store_true",
        help=(
            "If provided, Chimera unit cells will be presented in cross layout, "
            "as opposed to the default L-layout"
        )
    )
    zephyr = subcommands.add_parser("zephyr", parents=[parent_parser])
    zephyr.add_argument("n", type=int, help="Size of the Zephyr graph")

    chimera.set_defaults(generate=generate_chimera_picture)
    pegasus.set_defaults(generate=generate_pegasus_picture)
    zephyr.set_defaults(generate=generate_zephyr_picture)

    args = parser.parse_args()
    args.generate(args)

    if args.compile:
        args.output.close()
        subprocess.run(["latexmk", "-pdf", args.output.name])


if __name__ == '__main__':
    main()

