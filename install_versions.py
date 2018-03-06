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
    '3.0', '3.1', '3.2', '3.2.1', '3.3', '3.4', '3.4.1', '3.5', '3.5.1', '4.0',
    '4.0.1', '4.0.2', '4.1', '4.2', '4.2.1', '4.3.1', '4.4', '4.4.1', '4.5', '4.5.1', '4.6'
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

