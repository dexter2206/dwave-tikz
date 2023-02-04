from dwavetikz.render import render


def generate_tikz_picture(
    graph,
    linearize_coord,
    layout,
    classify_coupler,
    template_name,
    with_labels
):
    linear_positions = {
        linearize_coord(node): tuple(position) for node, position in layout.items()
    }

    tikz_picture = render(
        template_name,
        nodes=linear_positions,
        edges=[
            (linearize_coord(n1), linearize_coord(n2), classify_coupler(n1, n2))
            for n1, n2 in graph.edges
        ],
        with_labels=with_labels
    )

    return tikz_picture
