__author__ = 'aftab'

import atom
import basisset
import molecule
import pertabdict
import shell

#Basis set parser for standard basis set files in Quantum Chemistry
#Tested as working on 2/3/2014 by Aftab Patel
#TODO: Add some safety

#utility function to count no of lines in a file
def file_len(file_reference):
    position = file_reference.tell()
    for i, l in enumerate(file_reference):
        pass
    file_reference.seek(position)
    return i + 1

class Parser:

    def count_primitives(self, file_reference):
        no_primitives = 0
        condition = True
        position = file_reference.tell()
        while condition:
            line = file_reference.readline()
            contents = line.split()
            if line == '':
                condition = False
                continue
            elif contents[0] in pertabdict.periodic_table:
                condition = False
            else:
                no_primitives = no_primitives + 1
        # print 'primitives counted', no_primitives
        file_reference.seek(position)
        return no_primitives

#Main parser, fully initializes an Atom object
    def gen_atom(self, center, filename):
        file_reference = open(filename, 'r')
        atom_gen = atom.Atom()
        atom_gen.center = center
        no_lines = file_len(file_reference)
        print no_lines
        for lc in range(no_lines):
            #print 'master line no', lc
            line = file_reference.readline()
            contents = line.split()
            if line == '':
                continue
            elif contents[0] in pertabdict.periodic_table:
                atom_gen.atomic_number = pertabdict.periodic_table[contents[0]]
                ang_mom = pertabdict.shell_types[contents[1]]
                position = file_reference.tell()
                probe_line = file_reference.readline()
                no_shells_added = len(probe_line.split()) - 1
                #print 'shells added', no_shells_added
                shells = [shell.Shell() for i in range(no_shells_added)]
                #initialize shells
                file_reference.seek(position)
                no_primitives = self.count_primitives(file_reference)
                for i in range(no_primitives):
                    data_line = file_reference.readline()
                    data_content = data_line.split()
                    for i in range(no_shells_added):
                        shells[i].angular_momentum = ang_mom
                        shells[i].exponents.append(data_content[0])
                        shells[i].coefficients.append(data_content[i + 1])
                atom_gen.shells.extend(shells)
                atom_gen.no_shells = atom_gen.no_shells + no_shells_added
                file_reference.seek(position)
            else:
                continue
        file_reference.close()
        return atom_gen

if __name__ == '__main__':
    #basis_file = open('./cc_pvdz_c.basis','r')
    par = Parser()
    C_atom = par.gen_atom([0.0, 0.0, 0.0],'./cc_pvdz_c.basis')
    print C_atom.no_shells


















