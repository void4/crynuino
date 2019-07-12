# Crynuino

Takes fast screenshots and sends them as bytes via serial connection to your Arduino

## Installation

```
chmod +x install.sh
./install.sh
```

Alternatively,

`pip install -r requirements.txt`

## Instructions

1. Set the uppercase constant values in `main.py` (path to Arduino serial connection, display size)

2. To send PNG (or other, formatted/compressed) image data, uncomment the BytesIO lines in `util.py`.
