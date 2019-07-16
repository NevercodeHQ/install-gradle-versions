#!/bin/sh

set -e
set -x

ARCHIVE_PATH="/tmp/install-gradles.zip"
REPO_DIR="install-gradle-versions-master"

wget https://github.com/NevercodeHQ/install-gradle-versions/archive/master.zip -O $ARCHIVE_PATH
unzip $ARCHIVE_PATH

CURRENT_DIR=`pwd`
cd $REPO_DIR
python install_versions.py

cd $CURRENT_DIR
rm $ARCHIVE_PATH
rm -r $REPO_DIR

