# -*- coding: utf-8 -*-

class AbstractFormError(Exception):
    def __init__(self, valtype, val):
        self.value = val
        self.valtype = valtype
    def __str__(self):
        return 'Can not build abstract form for {0} ({1})'.format(self.valtype,
                                                                self.value)
