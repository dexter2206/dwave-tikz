import dwave_networkx as dnx

from ._generate import generate_tikz_picture


COMMAND_NAME = "chimera"


def _classify_coupler(first, second):
    if first[0:2] == second[0:2]:
        return "internal"
    else:
        return "external"


def add_args(parser) -> None:
    parser.add_argument("m", type=int, help="The number of rows in the Chimera graph")
    parser.add_argument(
        "-n",
        type=int,
        help=(
            "The number of columns in the Chimera graph. "
            "If not provided, defaults to the number of rows."
        )
    )
    parser.add_argument(
        "-t",
        type=int,
        help=(
            "Shore size of the Chimera unit cell. "
            "If not provided, the default shore size of 4 will be used."
        )
    )


def fill_dynamic_defaults(args):
    if args.n is None:
        args.n = args.m
    if args.scale is None:
        args.scale = 20.0


def generate(args):
    picture_source = generate_tikz_picture(
        graph=(graph := dnx.chimera_graph(args.m, args.n, args.t, coordinates=True)),
        linearize_coord=dnx.chimera_coordinates(args.m, args.n, args.t).chimera_to_linear,
        layout=dnx.chimera_layout(graph, scale=args.scale),
        classify_coupler=_classify_coupler,
        template_name="chimera.jinja2",
        with_labels=args.with_labels
    )

    args.output.write(picture_source)
