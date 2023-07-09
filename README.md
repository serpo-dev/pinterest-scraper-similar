# Pinterest similar pins scraper (breadth-first search)

## Introduction

The script can scrap the links to the similar pins of the source one and also use the obtained links in the same algo as the source. Thus, the script works according to the breadth-first search algorithm. The depth of scraping is set in the command line, by default, it is 3, which, when taking the first 100 similar pins, will result in about 1 million links to pins. Then the script also allows downloading all images according to the obtained links to pins.

## Deps

- selenium (4.10.0)

## Usage

1. Install dependencies:

`pip install -r requirements.txt`

2. Run by the command:

`python main.py`
