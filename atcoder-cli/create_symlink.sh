#!/bin/sh

# get script located dir
DIR=$(cd $(dirname $0);pwd)

set -e
set -x

ln -shf "$DIR/cpp" "$(acc config-dir)/cpp"
ln -shf "$DIR/python" "$(acc config-dir)/python"
