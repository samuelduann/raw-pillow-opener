import os
from unittest import mock

import PIL
import pytest
from PIL import Image

from raw_pillow_opener import register_raw_opener

register_raw_opener()

@pytest.mark.parametrize(
    ['image_name'],
    [
        ('DSC_0704.NEF',),
    ]
)

def test_open_image(image_name):
    image = Image.open(os.path.join('tests', 'images', 'DSC_0704.NEF'))

    assert image is not None

@mock.patch.object(Image, 'register_open')
@mock.patch.object(Image, 'register_decoder')
@mock.patch.object(Image, 'register_extensions')
def test_register_heif_opener(
    register_open_mock,
    register_decoder_mock,
    register_extensions_mock,
):
    register_raw_opener()

    register_open_mock.assert_called_once()
    register_decoder_mock.assert_called_once()
    register_extensions_mock.assert_called_once()
