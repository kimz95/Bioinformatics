## The comment on the variable 'I' can be removed for user input
## This progam is a solution to the cyclopeptides sequencing problem using branch and bound

import time
from collections import Counter

dictionary = {
     "G" : 57,
     "A" : 71,
     "S" : 87,
     "P" : 97,
     "V" : 99,
     "T" : 101,
     "C" : 103,
     "I" : 113,
     "L" : 113,
     "N" : 114,
     "D" : 115,
     "K" : 128,
     "Q" : 128,
     "E" : 129,
     "M" : 131,
     "H" : 137,
     "F" : 147,
     "R" : 156,
     "Y" : 163,
     "W" : 186,
}

inv_dict = {v: k for k, v in dictionary.items()};

def newsuptides(sub):
    arr = []
    for i in range(0,len(sub)):
        for j in range(1,len(sub)):
            if(i+j <= len(sub)):
                arr.append(sub[i : i + j])
        
    arr.append(sub)
    return arr


def linearspectrum(arrOfSubs):
    arr = []
    for i in arrOfSubs:
            spstr = list(i)
            sum = 0
            for i in spstr:
                sum += dictionary.get(i,"Incorrect")
            arr.append(sum)
                
    arr.sort()
    return arr


def findsubs(sub):
    out=[];
    for key,value in dictionary.items():
        if(value != dictionary.get(sub[-1])):
            temp = sub + key;
            out.append(temp);
      
    return out;


def isconsistent(sub,spectrum):
    
    printb=False;
    if (sub=="TVT"):
        printb=True;
        
    SubSpectrum=linearspectrum(newsuptides(sub));
    
    c1= Counter(SubSpectrum);
    c2= Counter(spectrum);
    diff = c1-c2;
    diff=list(diff.elements());
    
    if(len(diff)==0):
        return True
    
    return False

def initial_list(spectrum):
    lista=[];
    
    for i in spectrum:
        if(i>187):
            break;
        OneMer=inv_dict[i];
        if(OneMer not in lista):
            lista.append(OneMer);
        
    return lista;


print("Please input the spectrum")
I= "0 97 97 99 101 103 196 198 198 200 202 295 297 299 299 301 394 396 398 400 400 497";
#I=input();
stringspectrum=I.split(" ");
spectrum=[int(i) for i in stringspectrum if int(i) != 0];
init_list =initial_list(spectrum);
#print("The initial list is: ");
#print(init_list);

final_list=[init_list];
previouslist=init_list;

for i in range(2,6):
    nextlist=[];

    for j in previouslist:
        subs=findsubs(j);
        
        for k in subs:
            if(isconsistent(k,spectrum)):
                nextlist.append(k);
            
    final_list.append(nextlist);        
    previouslist=nextlist+[];

print(final_list);
time.sleep(60);
