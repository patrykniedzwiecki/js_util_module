#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2021 Huawei Device Co., Ltd.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import shutil
import platform
import argparse
import subprocess


def run_command(in_cmd):
    print(" ".join(in_cmd))
    proc = subprocess.Popen(in_cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          universal_newlines=True,
                          shell=False)
    stdout, stderr = proc.communicate()
    if stdout != "":
        raise Exception(stdout)

if __name__ == '__main__':


    PARSER_INST = argparse.ArgumentParser()
    PARSER_INST.add_argument('--dst-file',
                        help='the converted target file')
    PARSER_INST.add_argument('--module-path',
                        help='the module path')
    PARSER_INST.add_argument('--out-file',
                        help='js output file')
    INPUT_ARGUMENTS = PARSER_INST.parse_args()

    BUILD_PATH = os.path.abspath(os.path.join(os.getcwd(), "../.."))
    os.chdir(("%s" + INPUT_ARGUMENTS.module_path) % BUILD_PATH)
    NODE_PATH = '../../../../prebuilts/build-tools/common/nodejs/\
node-v12.18.4-linux-x64/bin/node'
    if not os.path.exists(NODE_PATH):
        raise Exception('NO souch file or directory')
    TSC_PATH = '../../../../ark/ts2abc/ts2panda/node_modules/\
typescript/bin/tsc'
    CMD_INST = [NODE_PATH, TSC_PATH]
    run_command(CMD_INST)
    if not os.path.exists(INPUT_ARGUMENTS.out_file):
        raise Exception('error:NO souch file or directory')
    CMD_INST = shutil.copy(INPUT_ARGUMENTS.out_file, INPUT_ARGUMENTS.dst_file)

    CMD_INST = shutil.rmtree('./out')

    exit(0)