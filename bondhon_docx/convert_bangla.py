#!/usr/bin/env python

import argparse

import os

from docx import Document

from bondhon_docx import conversion

def main():
    parser = argparse.ArgumentParser(description='Convert Bengali Documents between encodings.')
    parser.add_argument('from_enc', help='Original Encoding of File')
    parser.add_argument('to', help='The Encoding you want to convert to')
    parser.add_argument('path', help='The path of the file')

    args = parser.parse_args()

    document = Document(args.path)
    conversion.convert_document(args.from_enc, args.to, document)
    path_without_ext, _ = os.path.splitext(args.path)
    document.save(path_without_ext + '.converted.docx')
