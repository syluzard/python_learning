#       ACTGATCGATTACGTATAGTAGAATTCTATCATACAT  
#           G*AATTC  
#       ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT 
#           G*AATTC  

def getfragments(seq, motif):
    bool = True;
    frag1 = "";
    frag2 = "";

    #1
    seq = seq.strip().upper()
    motif = motif.strip().upper()
    #print("seq: ",  seq );
    #print("motif: ",  motif );
    int_motif_len = len(motif)
    start_motif_position = motif.find('*')

    #2-1
    pre_motif_str  = motif[:start_motif_position];
    #print("pre_motif_str: ",  pre_motif_str );

    #2-2
    post_motif_str = motif[start_motif_position+1:];
    #print("post_motif_str: ", post_motif_str);

    #3-1
    pre_motif_in_seq_fistposition = seq.find(pre_motif_str)
    #print("len(pre_motif_str): ", len(pre_motif_str))
    #print("seq[pre_motif_in_seq_fistposition+len(pre_motif_str):] : ",seq[pre_motif_in_seq_fistposition+len(pre_motif_str):]);

    #3-2
    post_motif_in_seq_fistposition  = seq[pre_motif_in_seq_fistposition+len(pre_motif_str):].find(post_motif_str)
    #print("pre_motif_in_seq_fistposition: ",  pre_motif_in_seq_fistposition );
    #print("post_motif_in_seq_fistposition: ", post_motif_in_seq_fistposition);

    #3-3
    if start_motif_position < 0:
        exist = False;
        return exist, frag1, frag2;
    elif pre_motif_in_seq_fistposition < 0 :
        exist = False;
        return exist, frag1, frag2;
    elif pre_motif_in_seq_fistposition < 0 :
        exist = False;
        return exist, frag1, frag2;
    elif pre_motif_in_seq_fistposition + len(pre_motif_str) + post_motif_in_seq_fistposition + 2 + len(post_motif_str) == len(seq):
        exist = False;
        return exist, frag1, frag2;
    else : 
        exist = True;

    #4
    #print(seq);
    #print(seq[:pre_motif_in_seq_fistposition]);
    #print(seq[pre_motif_in_seq_fistposition:]);
    frag1 = seq[:post_motif_in_seq_fistposition+len(pre_motif_str)+pre_motif_in_seq_fistposition];
    frag2 = seq[post_motif_in_seq_fistposition+len(pre_motif_str)+pre_motif_in_seq_fistposition:];
    print("frag1: ", frag1)
    print("frag2: ", frag2)


    
    return exist, frag1, frag2;

def main():
    seq = input("Give me the sequence: ")
    motif = input("Give me the enzyme motif: ")




    exist, frag1, frag2 = getfragments(seq, motif)
    if exist:
        print('Fragment 1 (%s):' % len(frag1), frag1)
        print('Fragment 2 (%s):' % len(frag2), frag2)
    else:
        print('No site exists.')

main()

