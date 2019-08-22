#!/usr/bin/env python
# coding: utf-8
#
# Licensed under MIT
#

import setuptools
setuptools.setup(
    name = "liquid_k8s_yaml_generator",
    version = "0.1",
    packages = ['liquid_k8s_yaml_generator'],
    package_dir={'liquid_k8s_yaml_generator':'liquid_k8s_yaml_generator/templates'},
    install_requires = [
    'jinja2>=2.10.1'
    ]
    )
