#!/bin/sh

set -e
set -x

# pip3 install online-judge-tools
# npm install -g atcoder-cli
# oj login https://atcoder.jp/

# http://tatamo.81.la/blog/2018/12/07/atcoder-cli-tutorial/
acc config default-test-dirname-format test
acc config default-template python
acc config default-task-choice all
