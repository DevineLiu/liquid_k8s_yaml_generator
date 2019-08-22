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
    package_data={'liquid_k8s_yaml_generator':['templates/*.tmpl']},
    include_package_data=True,
    install_requires = [
    'jinja2>=2.10.1'
    ]
    )
