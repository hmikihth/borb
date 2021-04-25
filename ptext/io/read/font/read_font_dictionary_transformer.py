#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    This implementation of ReadBaseTransformer is responsible for reading a Font object
"""
import io
import typing
from typing import Optional, Any, Union

from ptext.io.read.read_base_transformer import (
    ReadBaseTransformer,
    ReadTransformerContext,
)
from ptext.io.read.types import AnyPDFType, Dictionary
from ptext.pdf.canvas.event.event_listener import EventListener
from ptext.pdf.canvas.font.cid_font_type_0 import CIDFontType0
from ptext.pdf.canvas.font.cid_font_type_2 import CIDFontType2
from ptext.pdf.canvas.font.font import Font
from ptext.pdf.canvas.font.font_type_0 import FontType0
from ptext.pdf.canvas.font.font_type_1 import FontType1
from ptext.pdf.canvas.font.font_type_3 import FontType3
from ptext.pdf.canvas.font.true_type_font import TrueTypeFont


class ReadFontDictionaryTransformer(ReadBaseTransformer):
    """
    This implementation of ReadBaseTransformer is responsible for reading a Font object
    """

    def can_be_transformed(
        self, object: Union[io.BufferedIOBase, io.RawIOBase, io.BytesIO, AnyPDFType]
    ) -> bool:
        """
        This function returns True if the object to be transformed is a \Font Dictionary
        """
        return (
            isinstance(object, dict) and "Type" in object and object["Type"] == "Font"
        )

    def transform(
        self,
        object_to_transform: Union[io.BufferedIOBase, io.RawIOBase, AnyPDFType],
        parent_object: Any,
        context: Optional[ReadTransformerContext] = None,
        event_listeners: typing.List[EventListener] = [],
    ) -> Any:
        """
        This function reads a \Font Dictionary from a byte stream
        """

        # convert dictionary like structure
        assert isinstance(object_to_transform, Dictionary)
        subtype_name = object_to_transform["Subtype"]

        font_obj: Optional[Font] = None
        if subtype_name == "TrueType":
            font_obj = TrueTypeFont()
        elif subtype_name == "Type0":
            font_obj = FontType0()
        elif subtype_name == "Type1":
            font_obj = FontType1()
        elif subtype_name == "Type3":
            font_obj = FontType3()
        elif subtype_name == "CIDFontType0":
            font_obj = CIDFontType0()
        elif subtype_name == "CIDFontType2":
            font_obj = CIDFontType2()
        else:
            assert False, "Unsupported font type %s" % subtype_name

        # None
        if font_obj is None:
            return None

        # set parent
        assert font_obj is not None
        font_obj.set_parent(parent_object)  # type: ignore [union-attr]

        # add listener(s)
        for l in event_listeners:
            font_obj.add_event_listener(l)  # type: ignore [union-attr]

        # convert key/value pair(s)
        assert isinstance(object_to_transform, Dictionary)
        for k, v in object_to_transform.items():
            if k == "Parent":
                continue
            v = self.get_root_transformer().transform(v, font_obj, context, [])
            if v is not None:
                font_obj[k] = v

        # return
        return font_obj
