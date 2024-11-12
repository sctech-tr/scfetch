import locale

def get_locale():
    try:
        return locale.getdefaultlocale()[0] or "CONTACT DEV WITH ERRCODE: locale_info_returned_none"
    except Exception:
        return "CONTACT DEV WITH ERRCODE: locale_info_threw_exception"