file= open('parties.txt' )
parties={}
votes={}
s=file.read().split('Votes:\n')
p=s[0].split('\n')
v=s[1].split('\n')
for party in p:
    if party!="Parties:" and party!='':
        parties[party]=0
for party in v:
    parties[party]+=1

for party in parties:
    votes[party]=(parties[party]/len(v))
for party in votes:
    if votes[party]>0.07:
        print(party)
    

