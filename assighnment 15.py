
import re
#Q2

text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
bword=re.findall("[Bb][a-z]{1,20}",text)
print(bword)

#Q3
sentence = "A, very very; irregular_sentence"
sen=re.sub("[,;_]"," ",sentence)
print(sen)

#Q1
emails = "zuck26@facebook.com page33@google.com jeff42@amazon.com"
pattern = r'(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})'
a=re.findall(pattern, emails, flags=re.IGNORECASE)
print(a)