#!/usr/bin/env python3

import os
import subprocess

gradle_wrapper_properties_template = """\
#Mon Apr 24 12:14:06 EEST 2017
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-{version}-{distribution_type}.zip
"""

versions = [
    '5.5',
    '5.5.1',
    '5.6',
    '5.6.1',
    '5.6.2',
    '5.6.3',
    '5.6.4',
    '6.0',
    '6.0.1',
    '6.1',
    '6.1.1',
    '6.2',
    '6.2.1',
    '6.2.2',
    '6.3',
    '6.4',
    '6.4.1',
    '6.5',
    '6.5.1',
    '6.6',
    '6.6.1',
]

distribution_types = ['bin', 'all']

for version in versions:
    for distribution_type in distribution_types:
        gradle_wrapper_properties = gradle_wrapper_properties_template.format(
            version=version, distribution_type=distribution_type)
        with open('gradle/wrapper/gradle-wrapper.properties', 'w') as fd:
            fd.write(gradle_wrapper_properties)

        print("\n\n== Gradle version %s ==\n\n" % version)
        return_code = subprocess.call(['./gradlew', '--version'])
        if return_code != 0:
            raise ValueError("Installing Gradle %s failed" % version)

