import re;
import csv

f = open("resume.txt","r");
resume = f.read();

resume_cleaned = re.sub('[^a-zA-Z\n]', ' ', resume);
resume_cleaned = resume_cleaned.lower();
#print (resume_cleaned);

resume_cleaned = resume_cleaned.replace("\n","");
resume_words = resume_cleaned.split(" ");
print(resume_words);

frequency_map = dict();

detector = ['']
for word in resume_words:
        if word not in detector:
            if word not in frequency_map.keys():
                frequency_map[word]=1;
            else:
                frequency_map[word]+=1;

with open('mycsvfile.csv', 'w') as f:  # Just use 'w' mode in 3.x
    w = csv.DictWriter(f, frequency_map.keys())
    w.writeheader()
    w.writerow(frequency_map)