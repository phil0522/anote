#!/bin/bash

protoc --python_out=../genfiles/proto/ ./*.proto
touch ../genfiles/proto/__init__.py
