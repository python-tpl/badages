# -*- coding:utf-8 -*-

import os
from candy_path.iter import list_files
from candy_prompt.prompt import prompt, prompt_list


def construct():
    history = os.path.join(os.path.expanduser('~'), '.templates', 'tpl.history')
    namespace = prompt('Github Namespace: ', history=history)
    repo = prompt('Repo Name: ', default=os.getcwd().split("/")[-1], history=history)
    badages = []
    optional_badages = []
    for file in list_files(os.path.dirname(__file__), recursion=False):
        if not file.endswith('.badages'):
            continue
        for line in open(file):
            line = line.strip()
            if not line:
                continue
            optional_badages.append(line.format(namespace=namespace, repo=repo))

    while True:
        input = prompt_list(message='Badage: ', completions=optional_badages, history=history)
        if input == 'q':
            break
        if not input:
            continue
        badages.append(input)

    return {
        "badages":  badages
    }
