Introduction
============

A modified version of https://github.com/adafruit/Adafruit_CircuitPython_RGB_Display.git that adds text and other comforts. Only supports the
ST7735r display for now, I did not release any other displays because I lack the hardware to test such code.

.. note:: This driver currently won't work on micropython.org firmware.

This CircuitPython driver currently supports displays that use the following display-driver chips: ST7735R.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_
* `https://github.com/TG-Techie/TG-Fonts.git`_

Please ensure all dependencies are available on the CircuitPython filesystem, with TG_RGB & TG_Fonts inside of a folder marked 'TG_Modules'
This is easily achieved by downloading

Contributing
============

Contributions are welcome! Please read Adafruit's `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_RGB_Display/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Building locally
================

To build this library locally you'll need to install the
`circuitpython-build-tools <https://github.com/adafruit/circuitpython-build-tools>`_ package.

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install circuitpython-build-tools

Once installed, make sure you are in the virtual environment:

.. code-block:: shell

    source .env/bin/activate

Then run the build:

.. code-block:: shell

    circuitpython-build-bundles --filename_prefix adafruit-circuitpython-rgb_display --library_location .
