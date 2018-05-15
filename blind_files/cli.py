# -*- coding: utf-8 -*-

"""
Console script for blind_files.

nounlist from http://www.desiquintans.com/downloads/nounlist/nounlist.txt

"""

import csv
import sys
from hashlib import blake2b
from itertools import product
from pathlib import Path

import click


DELIMITER = '_R3D'


class IdentifierMapper:
    def __init__(self, key):
        self.key = key
        nouns = [line.strip() for line in open('nounlist.txt')][:4096]
        self.noun_pairs = list(product(nouns, repeat=2))

    def __call__(self, identifier):
        hash_value = blake2b(
            identifier.encode('utf-8'),
            digest_size=3,
            key=self.key.encode(),
        ).digest()
        index = int.from_bytes(hash_value, byteorder='big')
        noun_pair = self.noun_pairs[index]
        return '_'.join(noun_pair)


@click.command()
@click.option(
    '--dry/--no-dry',
    default=False,
)
@click.option(
    '--key',
    '-k',
    default='key',
)
@click.option(
    "--input-dir",
    '-i',
    type=click.Path(exists=True, file_okay=False),
    required=True,
)
@click.option(
    "--output-dir",
    '-o',
    type=click.Path(file_okay=False),
    required=True,
)
def main(dry, key, input_dir, output_dir):
    """Console script for blind_files."""
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    identifier_mapper = IdentifierMapper(key)

    identifiers = set()
    for file in input_dir.iterdir():
        if DELIMITER not in file.name:
            continue
        file_name = file.name
        index = file_name.index(DELIMITER)
        identifier = file_name[:index]
        identifiers.add(identifier)
        mapped = identifier_mapper(identifier)
        out_file_name = output_dir / (mapped + file_name[index:])
        if dry:
            click.echo(f"mv {file} {out_file_name}")
        else:
            file.rename(out_file_name)

    with open(output_dir / 'mapping.csv', 'w') as mapping_file:
        mapping_writer = csv.writer(mapping_file)
        mapping_writer.writerow(['original', 'name'])

        for identifier in sorted(identifiers):
            mapping_writer.writerow([
                identifier,
                identifier_mapper(identifier)
            ])


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
