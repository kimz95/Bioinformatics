import time

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

def newsuptides(instr):
    arr = [];
    paddedarr = instr + instr;
    for i in range(0,len(instr)):
        for j in range(1,len(instr)):
            arr.append(paddedarr[i : i + j]);
    arr.append(instr);
    return arr

def Spectrum(Subs):
    masses = [];
    for i in Subs:
        spstr = list(i);
        sum = 0;
        for i in spstr:
            sum += dictionary.get(i,"Incorrect");
            masses.append(sum);
    masses.append(0);
    masses.sort();
    return masses

print("Please enter an amino acid")
string = input().upper();
subs = newsuptides(string);
print(subs);
massArr = Spectrum(subs);
print(massArr);   
print(massArr[-1]);
time.sleep(10);
