# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..denoising import UnbiasedNonLocalMeans


def test_UnbiasedNonLocalMeans_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        hp=dict(
            argstr="--hp %f",
        ),
        inputVolume=dict(
            argstr="%s",
            extensions=None,
            position=-2,
        ),
        outputVolume=dict(
            argstr="%s",
            hash_files=False,
            position=-1,
        ),
        ps=dict(
            argstr="--ps %f",
        ),
        rc=dict(
            argstr="--rc %s",
            sep=",",
        ),
        rs=dict(
            argstr="--rs %s",
            sep=",",
        ),
        sigma=dict(
            argstr="--sigma %f",
        ),
    )
    inputs = UnbiasedNonLocalMeans.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_UnbiasedNonLocalMeans_outputs():
    output_map = dict(
        outputVolume=dict(
            extensions=None,
            position=-1,
        ),
    )
    outputs = UnbiasedNonLocalMeans.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
