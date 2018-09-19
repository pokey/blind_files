Blind files
===========

Generates a mapping from file names to blind but memorable file names.

Installing on OS X
------------------

1. Install [Homebrew](http://brew.sh/)
1. From a terminal, run

   ```
   brew install python3
   pip3 install -e .
   ```

Running on OS X
---------------

This script has two modes of operation:

Using a delimiter
=================
In the first mode of operation, you can specify a delimiter to use such that
all the text before the delimiter in each file name will be replaced.  For
example:

```sh
blind_files -m delimiter -d _foo -i input_dir -o output_dir
```

In this case, if `input_dir` contains the following files:

```
sample_1_foo.txt
sample_1_foo-bar.csv
hello.txt
```

Then `output_dir` will contain

```



This generates a `mapping.csv` file as well as `blind.sh` to blind and
`unblind.sh` to unblind.  So you'll likely want to immediately run

```sh
bash output_dir/blind.sh
```

Credits
-------
This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter-pypackage).

nounlist from [here](http://www.desiquintans.com/downloads/nounlist/nounlist.txt).
