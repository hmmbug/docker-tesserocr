= docker-tesserocr

A docker container based on [hmmbug/tesseract](https://github.com/hmmbug/docker-tesseract) with Tesseract 4.00 (alpha), Python 2.7 and the tesseroct python bindings.

= Usage

== Run a python script

```
docker run --name tesserocr -v appdir:/work -w work hmmbug/tesserocr myapp.py arg1 ... argn
```

where:

- 'appdir' is the local directory containing the app code which will be mounted in the container
- 'myapp.py' is the script to run
- arg1 ... argn are the arguments to provide to the script

== Run an interactive shell

```
docker run --rm -ti hmmbug/tesserocr /bin/sh
```

== Other options

```
docker run hmmbug/tesserocr [-h|-t]
```

- -h  Print the usage text
- -t  Run a test script
```

= Shortcut

A shell alias can be a convenient way to run the container:

```
alias tesserocr='docker run --rm -v `pwd`:/work -w /work hmmbug/tesserocr'
```

Then just run:

```
$ tesserocr -t
hmmbug/tesserocr test script

Software versions:
     python: 2.7.13
  tesseract: 4.00.00alpha
  leptonica: leptonica-1.74
  tesserocr: 2.2.0-beta

   Image: hello_world.png
Expected: Hello world.
  Actual: Hello world.
  Result: OK (0.266s)

   Image: quick_fox.png
Expected: The quick brown fox jumps over the lazy dog
  Actual: The quick brown fox jumps over the lazy dog
  Result: OK (0.756s)

$
```

= Test script

The supplied test script loads a list of image files and performs OCR on them
and then checks the actual output from the expected output.

Current tests:

- hello_world.png: Hello world.
- quick_fox.png: The quick brown fox jumps over the lazy dog
