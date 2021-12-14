import requests
import re

with open('rosalind_mprt.txt') as handle:
    uniprot_ids = handle.read().splitlines()

regex = re.compile(r"(?=N[^P][S|T][^P])") # pattern = Starts with [N] + anything but [P] + any one of [S] or [T] + anything but [P]

with open('output_mprt.txt', 'w') as outfile:
    for id in uniprot_ids:
        try:  # another way = urllib.request.urlopen(url).read().decode('utf-8') but it's compromised by url redirect
            content = requests.get(url='http://www.uniprot.org/uniprot/'+id+'.fasta', allow_redirects=True).text
            seq = ''.join(content.splitlines()[1:]) # take only sequence data starting from: line 2
        except: 
            print('accession ID not valid')

        span = [match.span() for match in list(re.finditer(regex, seq))] # re.finditer gives a match_object with span,group attr.
        
        if len(span) > 0:
            outfile.write(id + '\n' + ' '.join(str(start+1) for start,end in span)+'\n')