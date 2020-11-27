#!/usr/bin/env python
#
# pygtk-sane:  a Python/GTK SANE front-end
# Copyright (C) 2020 Jeremy A Gray <jeremy.a.gray@gmail.com>.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sane
from PIL import Image

def about():
    project='pyGTK-sane'
    year=2020
    author='Jeremy A Gray'
    email='jeremy.a.gray@gmail.com'
    s = rf'''{project}:  Copyright (C) {year} {author} <{email}>.
This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
This is free software, and you are welcome to redistribute it
under certain conditions; type `show c' for details.'''

    return s

def init():
    # Initialize.
    sane.init()


def get_devices():
    # Try to find the devices.
    try:
        return sane.get_devices()
    except _sane.error:
        print('no devices found')
    finally:
        sane.exit()


if __name__ == '__main__':
    # print(about())
    # l = License('PyGTK=SANE', 'Jeremy A Gray', 'jeremy.a.gray@gmail.com')
    # print(l.about())
    sane.init()

    devices = get_devices()
    scanner = sane.open(devices[0][0])
    # options = scanner.get_options()
    # for option in options:
    #     print(option)

    print(scanner.get_parameters())

    print(scanner['mode'])
    scanner.mode = 'Color'
    print(scanner['mode'])

    print(scanner['resolution'])
    scanner.resolution = 600
    print(scanner['resolution'])

    # 600 dpi.
    # scanner.mode = 'Color'
    # scanner.resolution = 600

    # Scan.
    scanner.start()
    img = scanner.snap()

    # Letter paper: 600 dpi * 8.5 in = 5100 width
    #               600 dpi * 11 in = 6600 length

    # img.resize((5100, 6600)).save('test.pdf')
    img.save('test.pdf')

    print(scanner['mode'])
    print(scanner['resolution'])

    # Call sane.close() before sane.exit() to avoid a segmentation fault.
    scanner.close()

    sane.exit()
