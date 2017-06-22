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
    '1.6', '1.7', '1.8', '1.9', '1.10', '1.11', '1.12',
    '2.0', '2.1', '2.2', '2.2.1', '2.3', '2.4', '2.5',
    '2.6', '2.7', '2.8', '2.9', '2.10', '2.11', '2.12',
    '2.13', '2.14', '2.14.1', '3.0', '3.1', '3.2',
    '3.2.1', '3.3', '3.4', '3.4.1', '3.5', '3.5.1', '4.0',
    '4.1-milestone-1'
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

