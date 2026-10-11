"""Copy source files without writing to them; use APFS clones when available."""
import ctypes,os,shutil,sys
from pathlib import Path

def copy_without_overwrite(source,destination):
    source=Path(source);destination=Path(destination)
    if source.is_symlink() or not source.is_file():raise ValueError('Source must be a regular non-symlink file')
    destination.parent.mkdir(parents=True,exist_ok=True)
    if destination.exists() or destination.is_symlink():raise FileExistsError(destination)
    if sys.platform=='darwin':
        libc=ctypes.CDLL('/usr/lib/libSystem.B.dylib',use_errno=True)
        clone=libc.clonefile;clone.argtypes=[ctypes.c_char_p,ctypes.c_char_p,ctypes.c_int];clone.restype=ctypes.c_int
        if clone(os.fsencode(source),os.fsencode(destination),0)==0:return 'APFS copy-on-write clone'
        if destination.exists():raise FileExistsError(destination)
    # Exclusive creation is the cross-platform overwrite guard.
    with source.open('rb') as incoming,destination.open('xb') as outgoing:shutil.copyfileobj(incoming,outgoing,length=8*1024*1024)
    shutil.copystat(source,destination)
    return 'independent byte copy'
