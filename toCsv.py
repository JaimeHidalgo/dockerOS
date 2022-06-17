from itertools import islice
import csv

def toCsv():
    Details = ['Collection Ranking','Collection Name','Collection Volune','Collection 24h%','Collection 7d%','Collection Floor Price','Collection Owners','Collection Items']
    rows = []
    with open('nftCollections.txt','r') as nfts:
       while True:
           lines = list(islice(nfts,8))
           rows.append(lines)
           if not lines:
            break


    with open('nftCollections.csv','w') as f:
        write = csv.writer(f)
        write.writerow(Details)
        write.writerows(rows)

if __name__ == '__main__':
    toCsv()