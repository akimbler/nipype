# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import ExtractMainComponent


def test_ExtractMainComponent_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr="%s",
            extensions=None,
            mandatory=True,
            position=1,
        ),
        out_file=dict(
            argstr="%s",
            extensions=None,
            name_source="in_file",
            name_template="%s.maincmp",
            position=2,
        ),
    )
    inputs = ExtractMainComponent.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_ExtractMainComponent_outputs():
    output_map = dict(
        out_file=dict(
            extensions=None,
        ),
    )
    outputs = ExtractMainComponent.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
