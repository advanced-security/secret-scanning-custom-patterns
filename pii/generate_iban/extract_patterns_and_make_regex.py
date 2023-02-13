#!/usr/bin/env python3

from argparse import ArgumentParser
from bs4 import BeautifulSoup
import yaml
import logging


LOG = logging.getLogger(__name__)


IBAN_HEADINGS = ['Country', 'Code', 'SEPA',	'Length', 'Account Check', 'Branch', 'IBAN Example']


def add_args(parser: ArgumentParser) -> None:
    """Add command-line arguments."""
    parser.add_argument("html_file", help="HTML from iban.com/structure")
    parser.add_argument("--debug", "-d", action="store_true", help="Debug output")


def main() -> None:
    """Run the app."""
    parser = ArgumentParser(description="Parse official IBAN structure and create regex")
    add_args(parser)
    args = parser.parse_args()

    logging.basicConfig()
    if args.debug:
        LOG.setLevel(logging.DEBUG)

    with open(args.html_file) as hf:
        html_doc = hf.read()
        soup = BeautifulSoup(html_doc, 'html.parser')

        countries = []

        # read all of the tr entries in the table rows
        for tr in soup.find_all("tr"):
            country = {}
            for i, td in enumerate(tr.find_all("td")):
                contents = ''.join(td.contents[0].stripped_strings) if td.contents else None 
                label = IBAN_HEADINGS[i]

                # a little normalisation
                if contents:
                    if 'tick' in contents:
                        contents = 'Y'
                    elif contents == "No":
                        contents = 'N'
                    elif contents == 'Yes':
                        contents = 'Y'
                else:
                    contents = 'N'

                country[label] = contents

            countries.append(country)

        LOG.debug(countries)

        # make some regex
        patterns = []

        for country in countries:
            pattern = {}

            try:
                pattern['name'] = f"IBAN for {country['Country']}"
                pattern['type'] = f"iban_{str(country['Code']).lower()}"

                # sometimes patterns end in letters, so allow the final 3 to be A-Z instead of numbers
                regex = f"{country['Code']}" + "(?:[0-9][ -]?)" + "{" + str(int(country['Length']) - 3) + '}' + '(?:(?:[0-9][ -]){3}|[A-Z]{3})'

                pattern["regex"] = {}
                pattern["regex"]["pattern"] = regex
                pattern["regex"]["start"] = r"\A|[^A-Za-z0-9-]"
                pattern["regex"]["end"] = r"\z|[^A-Za-z0-9-]"

                data = country['IBAN Example']
                pattern["test"] = {
                    "data": data,
                    "start_offset": 0,
                    "end_offset": len(data)
                }
            except KeyError as err:
                LOG.debug("Missing key: %s", err)
                continue
            except ValueError as err:
                LOG.debug("Wrong value: %s", err)
                continue

            patterns.append(pattern)
      
        LOG.debug(patterns)

        output = { 'name': 'IBANs', 'patterns': patterns }

        # write to YAML
        print(yaml.safe_dump(output))


if __name__ == "__main__":
    main()

