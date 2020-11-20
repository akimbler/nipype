# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..converters import DWICompare


def test_DWICompare_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inputVolume1=dict(
            argstr="--inputVolume1 %s",
            extensions=None,
        ),
        inputVolume2=dict(
            argstr="--inputVolume2 %s",
            extensions=None,
        ),
    )
    inputs = DWICompare.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_DWICompare_outputs():
    output_map = dict()
    outputs = DWICompare.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
