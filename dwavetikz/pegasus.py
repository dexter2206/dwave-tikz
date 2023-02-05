import dwave_networkx as dnx

from ._generate import generate_tikz_picture


COMMAND_NAME = "pegasus"


def _classify_coupler(first, second):
    if first[0:3] == second[0:3]:
        return "external"
    elif (first[0], first[1], first[3]) == (second[0], second[1], second[3]): # odd
        return "odd"
    else:
        return "internal"


def add_args(parser):
    parser.add_argument("n", type=int, help="Size of the Pegasus graph")
    parser.add_argument(
        "--cross",
        action="store_true",
        help=(
            "If provided, Chimera unit cells will be presented in cross layout, "
            "as opposed to the default L-layout"
        )
    )


def fill_dynamic_defaults(args):
    if args.scale is None:
        args.scale = 50.0


def generate(args):
    picture_source = generate_tikz_picture(
        graph=(graph := dnx.pegasus_graph(args.n, coordinates=True)),
        linearize_coord=dnx.pegasus_coordinates(args.n).pegasus_to_linear,
        layout=dnx.pegasus_layout(graph, crosses=args.cross, scale=args.scale),
        classify_coupler=_classify_coupler,
        template_name="pegasus.jinja2",
        with_labels=args.with_labels
    )

    args.output.write(picture_source)
