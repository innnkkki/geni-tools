#----------------------------------------------------------------------
# Copyright (c) 2013 Raytheon BBN Technologies
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and/or hardware specification (the "Work") to
# deal in the Work without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Work, and to permit persons to whom the Work
# is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Work.
#
# THE WORK IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE WORK OR THE USE OR OTHER DEALINGS
# IN THE WORK.
#----------------------------------------------------------------------
from gmoc import * #GMOCObject


class GENIObject(GMOCObject):
    def __init__(self, id ):
        # Could do this but really don't want anything but id
        # return super(GENIObject, self).__init__(id)
        self.id = id
    def __str__(self):
        retVal = ""+str(self.__class__.__name__)+"( "+str(self.__dict__['__id'])+" )"
        for key, value in self.__dict__.items():
            if key == "__id":
                continue
            retVal += "\n  "+str(key)+" : "+str(value)+""
        return retVal

def validateInt( integer ):
    if type(integer) == int:
        return integer
    else:
        try:
            return int( integer )
        except:
            return None

class URN(GENIObject):
    '''URN'''
    __metaclass__ = GMOCMeta
    __ID__ = validateURN
    def __init__(self, urn):
        self.id = urn

class GENIObjectWithURN(GENIObject):
    __metaclass__ = GMOCMeta
    __ID__ = validateInt

    def __init__(self, id, urn=None):
        super(GENIObjectWithURN, self).__init__(id)
        self._urn = urn

    @property
    def urn(self):
        return self.urn

    @urn.setter
    def urn(self, value):
        if value != None:
            if type(value) == URN:
                self._urn = value
            elif isinstance(value, str):
                self._urn = URN( value )
            else:
                raise TypeError("urn must be a valid URN")
        else:
            self._urn = None
        
