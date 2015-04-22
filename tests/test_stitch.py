"Test stitching of Leica OME.TIF experiment."

import pytest
from py import path
from fijibin import macro


@pytest.fixture
def images(tmpdir):
    "'images' in tmpdir. Returns py.path object."
    e = path.local(__file__).dirpath().join('images')
    e.copy(tmpdir.mkdir('experiment'))
    return tmpdir.join('experiment')


def test_stitch(tmpdir, images):
    "It should stitch images without error."
    filenames = 'x{x}y{y}.png'
    outfile = tmpdir.join('stitched.png')
    m = macro.stitch(images.strpath, filenames, 1, 2, outfile.strpath)
    macro.run(m)

    # output file should exists
    assert outfile.check()
