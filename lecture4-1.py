import sys


#1-1
sequence = input('Enter your sequence: ')
#print("sequence: ", sequence)
str_sequence = sequence.strip().upper()
#print("str_sequence: ", str_sequence)

#1-2
int_sequence_len = len(str_sequence)
K_fistposition = str_sequence.find('K')
K_lastsition   = str_sequence.rfind('K')
R_fistposition = str_sequence.find('R')
R_lastsition  = str_sequence.rfind('R')
P_fistposition = str_sequence.find('P')
P_lastsition  = str_sequence.rfind('P')

#print("int_sequence_len", int_sequence_len);
#print("K_fistposition:",K_fistposition);
#print("K_lastsition:",  K_lastsition);
#print("R_fistposition:",R_fistposition);
#print("R_lastsition:",  R_lastsition);
#print("P_fistposition:",P_fistposition);
#print("P_lastsition:",  P_lastsition);


#2-1
if str_sequence.count('K') + str_sequence.count('R')  > 1 :
    print("The sequence should have either one arginine, one lysine, or neither.")
    sys.exit(0) 

#2-2-1
if K_fistposition == -1 and R_fistposition == -1 :
    print("There is no digestion site.")
    sys.exit(0) 

#2-2-2
if K_fistposition == int_sequence_len - 1 or R_fistposition == int_sequence_len - 1 :
    print("There is no digestion site.")
    sys.exit(0) 

#2-2-3
if str_sequence[K_fistposition+1] == 'P' or str_sequence[R_fistposition+1] == 'P' :
    print("There is no digestion site.")
    sys.exit(0) 


#3

if K_fistposition >= 0 : 
    fistposition = K_fistposition
if R_fistposition >= 0 :
    fistposition = R_fistposition

print('Fragment 1 (length ', fistposition+1 ,'): ', str_sequence[:fistposition+1]);
print('Fragment 2 (length ', int_sequence_len - fistposition -1 ,'): ', str_sequence[fistposition+1:]);
