import unicodedata
from string import printable

for i in range(10869):
    c = chr(i)
    x = unicodedata.normalize('NFKC', c)
    if x != c and len(x) > 1:
        print(c, x, i)


kk = [
    'ﬀ', 'ﬁ', 'ﬂ', 'ﬃ', 'ﬄ', 'ﬅ', 'ﬆ',  # Latin ligatures
    'Ǆ', 'ǅ', 'ǆ', 'Ǉ', 'ǈ', 'ǉ',        # Serbian and Croatian ligatures
    'Æ', 'æ', 'Œ', 'œ', 'Ĳ', 'ĳ',        # Latin extended ligatures
    'Ꜳ', 'ꜳ', 'Ꜵ', 'ꜵ', 'Ꜷ', 'ꜷ',      # Additional Latin ligatures
    'Ꜹ', 'ꜹ', 'Ꜻ', 'ꜻ', 'Ꜽ', 'ꜽ', 
]

# eval("ﬀﬄag[0]>'S'or .1.a", )
# ﬀﬄag[0]>'S'or .1.a
# ﬀﬄag[0]>'Q'or .1.a

# galf[0]>'}'or(*rr({}),)
# galf[0]>'S'or(*rr({}),)
# ),)}{(rr*(ro'}'>]0[flag
# ),)}{(rr*(ro'u'>]0[flag

# pass
#  ),)}{(rr*(ro'h'>]0[flag

# fail
# ),)}{(rr*(ro'~'>]0[flag

# ),)}{(rr*(ro' '>]0[flag