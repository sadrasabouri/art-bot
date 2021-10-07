# -*- coding: utf-8 -*-
import os

def make_outputs_dir():
    """
    Make 'outputs/' directory in current directory.

    :return: None
    """
    if "outputs" not in os.listdir():
        os.mkdir("outputs")
