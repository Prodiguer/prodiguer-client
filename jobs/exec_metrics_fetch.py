# -*- coding: utf-8 -*-

"""
.. module:: jobs/exec_metrics_fetch.py
   :copyright: @2015 IPSL (http://ipsl.fr)
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Fetches simulation metrics from remote repository.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import argparse

import hermes_client as hermes



# Define command line arguments.
_parser = argparse.ArgumentParser("Fetches simulation metrics from remote repository.")
_parser.add_argument(
    "-g", "--group",
    help="A metrics group identifier",
    dest="group",
    type=str
    )
_parser.add_argument(
    "-f", "--filter",
    help="Path to a metrics filter to be applied",
    dest="filter",
    type=str,
    default=None
    )



def _main(args):
    """Main entry point.

    """
    data = hermes.metrics.fetch(args.group, args.filter)
    hermes.log("fetch :: {}".format(data), module="METRICS")


# Main entry point.
if __name__ == '__main__':
    _main(_parser.parse_args())
