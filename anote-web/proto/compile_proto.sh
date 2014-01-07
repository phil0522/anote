#!/bin/bash

protoc --python_out=../genfiles/proto/ ./*.proto
