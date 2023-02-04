import dwave_networkx as dnx

from .render import render


def _classify_coupler(first, second):
    if first[0:3] == second[0:3]:
        return "external"
    elif (first[0], first[1], first[3]) == (second[0], second[1], second[3]): # odd
        return "odd"
    else:
        return "internal"


def generate_pegasus_picture(args):
    pegasus = dnx.pegasus_graph(args.n, coordinates=True)
    coordinates = dnx.pegasus_coordinates(args.n)
    positions = dnx.pegasus_layout(pegasus, crosses=args.cross)
    linear_positions = {
        coordinates.pegasus_to_linear(node): tuple(30*position) for node, position in positions.items()
    }

    picture = render(
        "pegasus.jinja2",
        nodes=linear_positions,
        edges=[
            (
                coordinates.pegasus_to_linear(n1),
                coordinates.pegasus_to_linear(n2),
                _classify_coupler(n1, n2)
            )
            for n1, n2 in pegasus.edges
        ]
    )

    args.output.write(picture)
