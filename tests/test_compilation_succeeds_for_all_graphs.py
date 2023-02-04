from dwavetikz.cli import main

import pytest


@pytest.mark.parametrize(
    "args, output_path",
    [
        (["chimera", "2"], "chimera_1"),
        (["chimera", "4", "--scale", "10"], "chimera_2"),
        (["pegasus", "3"], "pegasus_1"),
        (["pegasus", "3", "--scale", "50"], "pegasus_2"),
        (["zephyr", "3"], "zephyr_1"),
        (["zephyr", "4", "--scale", "20"], "zephyr_2"),
    ]
)
class TestExistenceOfOutputFiles:
    def test_tikz_file_is_successfully_generated(self, args, output_path, tmp_path):
        output_path = tmp_path / output_path
        args = args + ["--output", str(output_path)]
        main(args)

        assert output_path.exists()

    def test_pdf_file_is_successfully_generated(self, args, output_path, tmp_path):
        output_path = tmp_path / output_path
        args = args + ["--output", str(output_path), "--compile"]
        main(args)

        assert output_path.with_suffix(".pdf").exists()
