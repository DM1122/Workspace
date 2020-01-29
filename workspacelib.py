import os
import shutil


class Workspace:
    def __init__(self, paths, verbose=0):
        self.paths = paths
        self.verbose = verbose

        print('[workspace]: Instatiating workspace at "{}"'.format(os.getcwd())) if self.verbose>=1 else False

        for path in self.paths:
            if not os.path.exists(path):
                print('[workspace]: Creating path "{}"'.format(path)) if self.verbose>=2 else False
                os.mkdir(path)
            else:
                print('[workspace]: Path "{}" already exists'.format(path)) if self.verbose>=2 else False


    def clear(self):
        '''
        Clears workspace folders.
        '''

        print('[workspace]: Clearing workspace') if self.verbose>=1 else False
        
        for path in self.paths:
            try:
                shutil.rmtree(path)
                print('[workspace]: Removed "{}"'.format(path)) if self.verbose>=2 else False
            except:
                print('[workspace]: Unable to remove "{}"'.format(path)) if self.verbose>=2 else False


    def new(self, path):
        if not os.path.exists(path):
            print('[workspace]: Creating path "{}"'.format(path)) if self.verbose>=1 else False
            os.mkdir(path)
            self.paths.append(path)
        else:
            print('[workspace]: Path "{}" already exists'.format(path)) if self.verbose>=1 else False


    def getOpen(self, file_name, file_ext, output_path):
        '''
        Returns next available path name. Useful for batch data exports.
        '''

        self.new(path=output_path)

        base = output_path + '/' + file_name + '_'

        i = 0
        while os.path.exists(base + str(i) + file_ext):
            i += 1
        
        open_path = base + str(i) + file_ext


        return open_path



if __name__ == '__main__':
    ws = Workspace(paths=['folder_A','folder_A/subfolder','folder_B','folder_C'], verbose=2)


    input('Press any key to clear workspace...')
    ws.clear()
