import dwave_networkx as dnx
import jinja2


def _classify_coupler(first, second):
    if first[0:3] == second[0:3]:
        return "external"
    elif (first[0], first[1], first[3]) == (second[0], second[1], second[3]): # odd
        return "odd"
    else:
        return "internal"


def main():
    pegasus = dnx.pegasus_graph(3, coordinates=True)
    coordinates = dnx.pegasus_coordinates(3)
    positions = dnx.pegasus_layout(pegasus, crosses=True)
    linear_positions = {
        coordinates.pegasus_to_linear(node): tuple(position) for node, position in positions.items()
    }

    loader = jinja2.FileSystemLoader(searchpath="./")
    env = jinja2.Environment(loader=loader)
    template = env.get_template("pegasus.jinja2")

    with open("result.tex", "w") as f:
        f.write(
            template.render(
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
        )


if __name__ == '__main__':
    main()
