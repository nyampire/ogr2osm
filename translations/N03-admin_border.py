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
# 国土数値情報は cbfファイルがshift_jisで書かれているので、文字コードを指定。
    if attrs['N03_001']:
        tags.update({'is_in:prefecture':unicode(attrs['N03_001'],'shift_jis')})
    else:
        pass

    if attrs['N03_002']:
        tags.update({'is_in:sub_prefecture':unicode(attrs['N03_002'],'shift_jis')})
    else:
        pass

    if attrs['N03_003']:
        tags.update({'is_in:county':unicode(attrs['N03_003'],'shift_jis')})
    else:
        pass

# 市町村名称の項目をもとにタグを追加
# ここも文字コードを指定。name:ja_kana, name:ja_rm, name:enは、JOSMに読み込んだ後に手動変換。dbfファイルを直接いじりたい
    if attrs['N03_004']:
        tags.update({'admin_level':'7'})
        tags.update({'boundary':'administrative'})
        tags.update({'name':unicode(attrs['N03_004'],'shift_jis')})
        tags.update({'name:ja':unicode(attrs['N03_004'],'shift_jis')})
        tags.update({'name:ja_kana':unicode(attrs['N03_004'],'shift_jis')})
        tags.update({'name:ja_rm':unicode(attrs['N03_004'],'shift_jis')})
        tags.update({'name:en':unicode(attrs['N03_004'],'shift_jis')})

# 市、町、村のそれぞれで、placeタグを分類。
    check_city = unicode(attrs['N03_004'],'shift_jis').encode('utf-8')    # ファイルからshift_jisで読み込んで、utf-8で格納。文字列比較のため、文字コードをあわせてる。
    if   check_city.endswith('市'):
        tags.update({'border_type':'city'})
    elif check_city.endswith('町'):
        tags.update({'border_type':'town'})
    elif check_city.endswith('村'):
        tags.update({'border_type':'village'})
    else:
        pass

    return tags

