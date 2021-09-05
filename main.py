#Main python file

def operators():
    parser = OptionParser()
    parser.add_option("-s", "--source", dest="srcfile",
                      help="Select source directory to back up.")
    parser.add_option("-d", "--destination", dest="destfile",
                      help="Select destination directory to save backup.")
    (srcfile, destfile) = parser.parse_args()
    return srcfile, destfile