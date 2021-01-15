# raw-pillow-opener

**raw-pillow-opener** is a *simple* camera raw opener for *Pillow* base on *rawpy* library.

## Installation

You can install **raw-pillow-opener** from *PyPi*:

`pip install raw-pillow-opener`

or from GitHub:

`pip install https://github.com/samuelduann/raw-pillow-opener/archive/master.zip`

## How to use

```
from PIL import Image

from raw_pillow_opener import register_raw_opener

register_raw_opener()

image = Image.open('TEST.NEF')
image.load()
```

---


## License

Released under [MIT License](https://github.com/samuelduann/raw-pillow-opener/blob/master/LICENSE).
