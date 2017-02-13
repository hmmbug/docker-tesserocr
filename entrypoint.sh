#!/bin/sh

usage() {
	cat <<EOF
Usage:

1. To run a python script in current directory with the tesserocr API:

   docker run --name tesserocr -v appdir:/work -w work hmmbug/tesserocr \\
     myapp.py arg1 ... argn

   where:
     'appdir' is the local directory containing the app code
     'myapp.py' is the script to run
     arg1 ... argn are the arguments to provide to the script

2. To run with an interactive shell:

   docker run --rm -ti hmmbug/tesserocr /bin/sh

3. Other options

   docker run --name tesserocr hmmbug/tesserocr [-h|-t]

		 -h  Print this usage text
		 -t  Run the test script

EOF
}

test_tesserocr() {
	cd /test
	python test_tesserocr.py
	exit $?
}

# if empty args or "-h"
if [ "$#" -eq 0 ]; then
	usage
	echo "Error: No args supplied."
	exit 1
fi

case "$1" in
"-h")
	usage
	exit 1
	;;

"-t")
	test_tesserocr
	;;
esac

[ -d /work ] && cd /work

# Display args to the user
echo "Args: $@"

# exec script
exec $@
