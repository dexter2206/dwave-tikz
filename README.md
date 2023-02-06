# d-wave tikz: tools for generating TikZ pictures of various D-Wave topologies

## What is this??

A collection of Python-based command line utilities that can generate 
standalone LateX documents with TikZ pictures of all currently available
D-Wave annealers' topologies. The pictures contain minimum styling and 
should serve only for defining the "skeleton" of the graph.

The generated pictures heavily utilize TikZ styles, so you can adjust the looks
of the pictures by tweaking style definitions at the very beginning of your 
TikZ picture.

## What is this not?

The `dwave-tikz` is not designed for producing pretty pictures. Yes, it 
contains basic styling, but the assumption is that you tweak the style 
definition in the produced .tex file. Writing a comprehensive CLI allowing 
one to control every single aspect of TikZ picture would be time consuming 
beyond the point of being useful.

## Installation

Python >= 3.8 is required. Other Python dependencies will be downloaded 
during installation. The `--compile` flag assumes that `latexmk` is 
available in your `PATH` variable.

To install the latest version just run:

```shell
pip install dwave-tikz
```

This should install the `dwavetikz` script in your path. To verify, run

```shell
dwavetikz -h
```

## Usage

The CLI invocation looks as follows:

```text
dwavetikz <topology> <size> [options] 
```
Some options are common to all topologies, others are specific to only given 
topology. Anyway, you can always run

```text
dwavetikz <topology> -h
```

to learn about all arguments available for given topology (both common and 
specific). For instance, `dwavetikz pegasus -h` will give you all available 
options for pegasus topoloy.

By default, the output is printed to stdout. You can either redirect it as 
usually, or use `--output` parameter to provide a file name.

Additionally, if `--compile` flag is provided, an attempt will be made to 
compile the output .tex file. Obviously, this only works in conjunction with 
`--output` flag.


### Examples

> **Warning**
> If you are using dark Github theme, the SVG pictures presented in this section may look 
> slightly unreadable, because they have transparent backgrounds.

**Example 1**: simple C2 Chimera, output to chimera.tex

```shell
dwavetikz chimera 2 --output chimera.tex
```

![chimera](https://github.com/dexter2206/dwave-tikz/raw/master/pictures/chimera.svg)

**Example 2**: the same Chimera, but with labels.

```shell
dwavetikz chimera 2 --output chimera2.tex --with-labels
```

![chimera](https://github.com/dexter2206/dwave-tikz/raw/master/pictures/chimera2.svg)


**Example 3**: the same Chimera, with labels, and after changing styles.

```shell
dwavetikz chimera 2 --output chimera3.tex --with-labels
```

The styles were modified as follows (relevant part of `chimera3.tex`):

```latex
\begin{tikzpicture}[
        scale=1,
        coupler/.style={draw},
        qubit/.style={
            circle, line width=2pt, font={\large \bfseries}, fill=White,draw=darkgray,minimum size=7mm, inner sep=0.5mm
        },
        hidden/.style={opacity=0.0},
        internal/.style={color=RoyalBlue, ultra thick, dashed},
        external/.style={color=Tan, ultra thick},
    ]
```

![chimera](https://github.com/dexter2206/dwave-tikz/raw/master/pictures/chimera3.svg)

**Example 4**: Chimera with 2 rows, 3 columns and nonstandard shore size of 8 (unit cells of 
such Chimera are ports of the Zephyr topology). It also uses larger scaling of coordinates to 
spread out nodes further away from each other (otherwise the nodes would overlap).

```shell
dwavetikz chimera 2 -n 3 -t 8 --output chimera4.tex --scale 40 --compile
```

![chimera](https://github.com/dexter2206/dwave-tikz/raw/master/pictures/chimera4.svg)

**Example 5**: The P3 Pegasus using the default L-layout for Chimera unit cells.

```shell
dwavetikz pegasus 3 --output pegasus.tex
```

![pegasus](https://github.com/dexter2206/dwave-tikz/raw/master/pictures/pegasus.svg)

**Example 6**: The P3 Pegasus using the cross layout for Chimera unit cells.

```shell
dwavetikz pegasus 3 --cross --output pegasus2.tex
```

![pegasus](https://github.com/dexter2206/dwave-tikz/raw/master/pictures/pegasus2.svg)

**Example 7**: The Z3 Zephyr graph.

```shell
dwavetikz zephyr 3 --cross --output zephyr.tex
```

![zephyr](https://github.com/dexter2206/dwave-tikz/raw/master/pictures/zephyr.svg)
