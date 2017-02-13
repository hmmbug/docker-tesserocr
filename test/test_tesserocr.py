#!/usr/bin/python

import sys
import tesserocr
from time import time

versions = tesserocr.tesseract_version().split()
# versions will be a list like this:
#   ['tesseract', '4.00.00alpha', 'leptonica-1.74', 'libjpeg', '8d',
#   '(libjpeg-turbo', '1.5.1)', ':', 'libpng', '1.6.25', ':', 'libtiff',
#   '4.0.7', ':', 'zlib', '1.2.8', 'Found', 'AVX', 'Found', 'SSE']

print "hmmbug/tesserocr test script"
print
print "Software versions:"
print "     python:", ".".join([str(i) for i in sys.version_info[:3]])
print "  tesseract:", versions[1]
print "  leptonica:", versions[2]
print "  tesserocr:", tesserocr.__version__
print

TESTS = {
    # a list of tests as image_file: text_in_image
    u"hello_world.png": u"Hello world.",
    u"quick_fox.png": u"The quick brown fox jumps over the lazy dog",
}

exit_code = 0

with tesserocr.PyTessBaseAPI() as api:
    for img, txt in TESTS.iteritems():
        timer = time()
        api.SetImageFile(img)
        ocr = api.GetUTF8Text().strip()
        timer = time() - timer

        if ocr == txt:
            result = "OK"
        else:
            result = "FAILED"
            exit_code = 1

        print u"   Image:", img
        print u"Expected:", txt
        print u"  Actual:", ocr
        print u"  Result: %s (%0.3fs)" % (result, timer)
        print

exit(exit_code)
