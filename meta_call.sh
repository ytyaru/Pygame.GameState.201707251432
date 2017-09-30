#!/bin/bash
user_name=ytyaru
description="ゲーム状態とその変更のフレームワークを仮実装してみた。"
homepage=http://ytyaru.hatenablog.com/entry/2018/07/12/000000
path_dir_pj=$(cd $(dirname $0) && pwd)

path_script=/media/mint/85f78c06-a96e-4020-ac36-9419b7e456db/mint/root/pj/auto/GitHub/python/v3.2/GitHubUploader.py
python3 ${path_script} "${path_dir_pj}" -u  "${user_name}" -d "${description}" -l "${homepage}"

