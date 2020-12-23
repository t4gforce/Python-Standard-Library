# -*- coding: utf-8 -*-
import sys

if __name__ == "__main__":
    print('platform : ' + sys.platform)

    print('script path : ' + sys.path[0])
    print('env variable : ' + str(sys.path[1:]))

    print('script name : ' + sys.argv[0])
    print('argv : ' + str(sys.argv[1:]))

    print('python path : ' + sys.executable)

    print('windows version : ' + str(sys.getwindowsversion()))
    
    print('python version : ' + sys.version)
    print('version info : ' + str(sys.version_info))
    
    print('copyright : ' + sys.copyright)

    print('exit')
    try:
        sys.exit()
    except SystemExit:
        print(sys.exc_info())