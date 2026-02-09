### Disclaimer
This is for educational purpose only. Learning and expandind knowledge of tools and resources that are used frequently in the world today to educate you on how to protect yourself more. There is no Blue Team knowledge without having Red Team Knowledge. These tutorials and techniques should only be practiced on your own systems and computers.

# What-Now?
List and break down of tutorials and what nows. These are for educational purpose only

**Do you ever feel like you get to a point and go, "Well, shit.... What Now?"**
We have all been there before and if you are new to the cyber world, its a common feeling to have.
With AI now, we just search and dont use our brains as much. This repo is to help you break away and not be so reliant on AI to give you the answers. **Following old school tutorials of what to do next, reading and working through it is the best way to learn**

# What Is Here?
There are mutliple different scenarios and workings that you can find in here. Showing the basics to the expert level approaches.

# Have Fun. Don't Be Malicious. Learn and Teach. Knowledge Is The #1 Currency.

-------------------------------------------------------------------------------

# wordlists.py
To use the wordlists.py use the below command with your .txt files in the same directory as the script
```
python3 wordlists.py *.txt -o masterlist.txt
```

**Be aware that if the files are too big, it will not be able to combine them and crash. Try using cat instead**
```
mkdir -p ./tmp_sort                        
cat *.txt | sort -T ./tmp_sort -u > masterlist1.txt
rm -rf ./tmp_sort
```


