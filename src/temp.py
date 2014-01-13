'''
Created on Jan 10, 2014

@author: Andrew
'''
# encoding: utf-16
def print_out(greetings):
    for greeting in greetings:
        print (greeting)
    
    print(copyright)
    
if __name__ == "__main__":
    
    greetings = [ 'HELLLLO', 'Bonjiorno', 'Buenos Dias' ]
    copyright = 'Copyright \xa9 iBitchin inc., All rights reserved'
    print_out(greetings)    
