# -*- coding: utf-8 -*-
def filterTags(attrs):
    if not attrs:
        return
    tags = {}
    
    tags.update({'boundary':'administrative'})
    tags.update({'admin_level':'6'})
    tags.update({'border_type':'city'})
    tags.update({'source':'KSJ2/NO3'})
    tags.update({'source:ja':u'ほげほげ'})
    tags.update({'source_ref':'http://wiki.openstreetmap.org/wiki/Import/Catalogue/Japan_KSJ2_Import'})

    if attrs['N03_004']:
        tags.update({'admin_level':'10'})
        tags.update({'name':unicode(attrs['N03_004'],'shift_jis')})
        tags.update({'name:ja':unicode(attrs['N03_004'],'shift_jis')})
        tags.update({'name:ja_kana':unicode(attrs['N03_004'],'shift_jis')})
        tags.update({'name:ja_rm':unicode(attrs['N03_004'],'shift_jis')})
        tags.update({'name:en':unicode(attrs['N03_004'],'shift_jis')})
    return tags
