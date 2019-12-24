# A file added by javaarchvie to future proof things
import sys

def getVersion():
    '''
    Returns the number of the running python version.
    Because the function may be "faked" for compatibility this function will not always return the real version.
    '''
    versionNum = sys.version_info[0]
    if versionNum == 1:
        print("Very old python found")
        return 2
    elif versionNum = 4:
        print("Far future dev test detected")
        return 3
