import dwave_networkx as dnx

from ._generate import generate_tikz_picture


COMMAND_NAME = "zephyr"


def _classify_coupler(first, second):
    if first[0:4] == second[0:4]:
        return "external"
    elif first[0:3] == second[0:3]:
        return "internal"
    else:
        return "odd"


def fill_dynamic_defaults(args):
    if args.scale is None:
        args.scale = 10


def add_args(parser):
    parser.add_argument("n", type=int, help="Size of the Zephyr graph")


def generate(args):
    picture_source = generate_tikz_picture(
        graph=(graph := dnx.zephyr_graph(args.n, coordinates=True)),
        linearize_coord=dnx.zephyr_coordinates(args.n).zephyr_to_linear,
        layout=dnx.zephyr_layout(graph, scale=args.scale),
        classify_coupler=_classify_coupler,
        template_name="zephyr.jinja2",
        with_labels=args.with_labels
    )

    args.output.write(picture_source)
