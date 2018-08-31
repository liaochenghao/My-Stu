# coding: utf-8
import hashlib


def generate_menu_tree(data_list, node):
    node['children'] = []
    if node['extra']:
        node['name'] = node['name'] + node['extra']
    for data in data_list:
        if data.get('parent_id') == node.get('id'):
            child = generate_menu_tree(data_list, data)
            node['children'].append(child)
    return node


def decorate_menu_tree(full_tree, menu_id_list):
    for data in full_tree:
        data['choose'] = True if data.get('id') in menu_id_list else False
        if data['children']:
            for child in data['children']:
                decorate_menu_tree([child], menu_id_list)


def md5(data):
    m2 = hashlib.md5()
    m2.update(data.encode("utf-8"))
    return m2.hexdigest()
