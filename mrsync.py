import options # import du fichier options.py
import filelist #import du fichier filelist.py
import server #import du fichier server.py
import generator #import du fichier generator.py

class File:
    def __init__(self):
        self.header = None
        self.name = None
        self.size = None
        self.hash = None
        #self.date = None
        self.data = None

class Sync :
    def __init__(self):
        self.args = None
        self.src = None
        self.files = []
        self.dest = None
        self.fd_src = None
        self.fd_dest = None

    def setArgs(self, args):
        self.args = args
    def setSrc(self, srcs):
        self.src = srcs
    def setDest(self, dest):
        self.dest = dest

if __name__ == '__main__':
    sync = Sync()
    sync.setArgs(options.getArgs())
    sync.setSrc(filelist.getSrcs(sync))
    sync.setDest(sync.args.dest)
    if sync.args.list_only:
        filelist.printSrcs(sync.src)
        exit(0)
    if sync.args.verbose:
        print("Source(s) : ", sync.src)
        print("Destination : ", sync.dest)
        #printLog(sync) function to print log while executing the copy
    generator.generateFiles(sync)
    server.createServer(sync)

