import os
import sys
from multiprocessing import Process

def Robot():
    os.system("./Robot.py")     
def testSSH():
    os.system("./testSSH.py") 

if __name__ == '__main__':
    a = Process(target=Robot)
    b = Process(target=testSSH)
    a.start()
    b.start()
    a.join()
    b.join()
    
# import os                                                                       
# from multiprocessing import Pool                                                
                                                                                
                                                                                
# processes = ('testSSH.py', 'Robot.py')                                    
                                                  
                                                                                
# def run_process(process):                                                             
#     os.system('python {}'.format(process))                                       
                                                                                
                                                                                
# pool = Pool(processes=2)                                                        
# pool.map(run_process, processes)    