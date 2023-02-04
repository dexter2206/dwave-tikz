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

**Example 1**: simple C2 Chimera, output to chimera.tex

```shell
dwavetikz chimera 2 --output chimera.tex
```

![chimera](pictures/chimera.svg)