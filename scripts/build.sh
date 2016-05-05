#!/bin/bash

SDIR="$(cd -P "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

rm -rf $SDIR/../openconfig_bindings
mkdir -p $SDIR/../openconfig_bindings

export PYANGPATH=`which pyang`
$SDIR/build_openconfig_bindings.py
