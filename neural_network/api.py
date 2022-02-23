"""
Online application to easily access the trained neural network.

Author: Gijs G. Hendrickx
"""
import sys
import os


def run():
    from neural_network.application.app import APP
    APP.run_server()


root = '\\'.join(os.path.abspath(os.path.dirname(__file__)).split('\\')[:-1])

if root not in sys.path:
    sys.path.append(root)

run()
