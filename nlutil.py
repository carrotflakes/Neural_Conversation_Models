# -*- coding: utf-8 -*-

import re
import unicodedata


def decouple_reply(text):
    reply_part, body = re.match(r"^((?:@[a-zA-Z0-9_]+\s+)*)(.+)$", text, flags=re.S).groups()
    return reply_part.split(), body

def decouple_end_hush(text):
    match = re.match(r"(?:\s+[#＃][^#＃]+)+\s*$", text)
    if match is None:
        return text, []
    else:
        end_hush_part = match.group(0)
        return text[:-len(end_hush_part)], end_hush_part.split()

def replace_url(text, replace=""):
    return re.sub(r"https?://\S+", replace, text)

def normalize(text):
    return unicodedata.normalize('NFKC', text)
