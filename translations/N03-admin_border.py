# -*- coding: utf-8 -*-
def filterTags(attrs):
    if not attrs:
        return
    tags = {}

# 基本のタグ付け
    tags.update({'source':'KSJ2/NO3'})
    tags.update({'note:ja':u'国土数値情報（行政区画）平成24年　国土交通省'})
    tags.update({'source_ref':'http://wiki.openstreetmap.org/wiki/Import/Catalogue/Japan_KSJ2_Import'})

# 県とか郡とかの is_inを付与。
# 国土数値情報は dbfファイルがshift_jisで書かれているので、文字コードを指定。
    if attrs['N03_001']:
        tags.update({'is_in:prefecture':attrs['N03_001']})
    else:
        pass

    if attrs['N03_002']:
        tags.update({'is_in:sub_prefecture':attrs['N03_002']})
    else:
        pass

    if attrs['N03_003']:
        tags.update({'is_in:county':attrs['N03_003']})
    else:
        pass

# 市町村名称の項目をもとにタグを追加
# ここも文字コードを指定。name:ja_kana, name:ja_rm, name:enは、JOSMに読み込んだ後に手動変換。dbfファイルを直接いじりたい
    if attrs['N03_004']:
        tags.update({'admin_level':'7'})
        tags.update({'boundary':'administrative'})
        tags.update({'name':attrs['N03_004']})
        tags.update({'name:ja':attrs['N03_004']})
        tags.update({'name:ja_kana':attrs['N03_004']})
        tags.update({'name:ja_rm':attrs['N03_004']})
        tags.update({'name:en':attrs['N03_004']})

# 市、町、村のそれぞれで、placeタグを分類。
    check_city = attrs['N03_004']
    if check_city.endswith('市'):
        tags.update({'border_type':'city'})
    elif check_city.endswith('町'):
        tags.update({'border_type':'town'})
    elif check_city.endswith('村'):
        tags.update({'border_type':'village'})
    else:
        pass

    return tags
