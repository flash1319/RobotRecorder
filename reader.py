#!/usr/bin/env python3

import optparse

from NTStorage import NTStorage
from NTPlotter import NTPlotter
import pickle
import time
import json


class RobotRecorder:
    def __init__(self, options):
        with open(options.file, 'rb') as f:
            self.session = pickle.load(f)

        with open(options.config) as config_file:
            self.config = json.load(config_file)

        self.ntgraph = NTPlotter(self.session, self.config)
        self.ntgraph.show_graph()


if __name__ == '__main__':
    parser = optparse.OptionParser()

    parser.add_option('-f', '--file', default='saves/examples/unnamed_match.ntstore', help='NTStorage file to be read')
    parser.add_option('-c', '--config', default='config.json', help='Config for graph layout')

    options, args = parser.parse_args()

    parser.add_option('-l', '--listkeys', default=False, action='store_true', help='Print out keys from dump')
    recorder = RobotRecorder(options)
