

import configparser
import os

CONFIG_PATH = os.path.abspath("../config/default.cfg")


class PipelineInit:

    def __init__(self, config_path=CONFIG_PATH):
        self.config_path = config_path
        self.config = {}

    def load_config(self):
        config_parser = configparser.ConfigParser()
        config_parser.read(self.config_path)
        self.config = dict(config_parser["SDG"]) if "SDG" in config_parser else {}

    def run(self):
        self.load_config()

        print(f"PipelineInit running with config: {self.config_path}")


if __name__ == "__main__":
    pipeline = PipelineInit()
    pipeline.run()
