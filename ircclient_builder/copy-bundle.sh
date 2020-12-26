#!/bin/sh

set -e
set -x

mkdir -p /bundle
rm -r /bundle/* || true
cp -r /app/kiwiirc/dist/* /bundle/
