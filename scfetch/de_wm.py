import platform

def get_wm():
    if platform.system() == 'Linux':
        try:
            import os
            de_wm = os.environ['XDG_CURRENT_DESKTOP']
            return de_wm
        except KeyError:
            return 'CONTACT DEV WITH ERRCODE: de_wm_threw_exception'
    elif platform.system() == 'Windows':
        return 'Windows Explorer'
    elif platform.system() == 'Darwin':
        return 'Finder'
    else:
        return 'CONTACT DEV WITH ERRCODE: de_wm_threw_exception_unsupported_platform'