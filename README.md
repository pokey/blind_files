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

Run eg

```sh
blind_files -i /Volumes/Caswell/DeltaVision/MSAI.4.18/HCT116_2 \
            -o /Volumes/Caswell/DeltaVision/MSAI.4.18/HCT116_2.randomized
```

This generates a `mapping.csv` file as well as `blind.sh` to blind and
`unblind.sh` to unblind.  So you'll likely want to immediately run

```sh
bash /Volumes/Caswell/DeltaVision/MSAI.4.18/HCT116_2.randomized/blind.sh
```

Credits
-------
This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter-pypackage).

nounlist from [here](http://www.desiquintans.com/downloads/nounlist/nounlist.txt).
