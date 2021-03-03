#!/usr/bin/env python3

import shutil
import subprocess
from pathlib import Path

gradle_wrapper_properties_template = """\
#Mon Apr 24 12:14:06 EEST 2017
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-{version}-{distribution_type}.zip
"""

DISTRIBUTION_TYPES = ('bin', 'all')

VERSIONS = (
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
    '6.7',
    '6.7.1',
    '6.8',
    '6.8.1',
    '6.8.2',
    '6.8.3',
)


def remove_unnecessary_files(version, distribution_type):
    dists_dir = Path(f'~/.gradle/wrapper/dists').expanduser()
    installation_path = dists_dir / f'gradle-{version}-{distribution_type}'

    distribution_package = next(installation_path.glob(f'*/{installation_path.name}.zip'), None)
    if distribution_package and distribution_package.is_file():
        print(f'Remove {distribution_package}')
        distribution_package.unlink(missing_ok=True)

    src_path = next(installation_path.glob('*/gradle-*/src'), None)
    docs_path = next(installation_path.glob('*/gradle-*/docs'), None)
    for path in (src_path, docs_path):
        if path and path.is_dir():
            print(f'Remove {path}')
            shutil.rmtree(path)


def download_version(version, distribution_type):
    gradle_wrapper_properties = gradle_wrapper_properties_template.format(
        version=version, distribution_type=distribution_type)
    with open('gradle/wrapper/gradle-wrapper.properties', 'w') as fd:
        fd.write(gradle_wrapper_properties)

    print(f"\n\n== Gradle version {version} ==\n\n")
    return_code = subprocess.call(['./gradlew', '--version'])
    if return_code != 0:
        raise ValueError(f"Installing Gradle {version} failed")


def main():
    for version in VERSIONS:
        for distribution_type in DISTRIBUTION_TYPES:
            download_version(version, distribution_type)
            remove_unnecessary_files(version, distribution_type)


if __name__ == '__main__':
    main()
