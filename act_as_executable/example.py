from act_as_executable import act_as_executable

class C:

    @act_as_executable('ifconfig $arg_0 $state')
    def ifconfig(self, *args, **results):
        print 'ifconfig output: %s' % (results)
        return None



if __name__ == '__main__':
    c = C()
    c.ifconfig('eth0', state='up')
