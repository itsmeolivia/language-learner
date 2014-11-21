Olivia Nordquist
nolivia

To run the code, there needs to be the folders saved in the same directory.  Part one
has a function called "filenames" and part 2 has the filenames manually placed
to avoid unnecessary confusion among switching between test folders and training data.

1. The best guess that my naive Bayes made was .5 which is also the highest possible entropy.
I left P(c) = 1/2 throughout because the total data was split 50/50 and when one document is taken
out, a bias is given to the incorrect category.  I counted only unique words for n because I was having 
floating point errors initially and furthermore, I did want to give a bias towards more common words in the numerator. This unfortunately had the effect of always giving "lie" a higher probability as the denomintor of nk + |Vocab| was smaller.  The other version I tried had a less than random chance at .489

Another reason I think this may have occured is because I read through many examples and the lies that
corresponded to the truth had similar statements such as one person mentioning in both that they were
bought paint supplies by their bff/enemy.  Painting should have been relatively unique but appeared in
both categories. 

2. The predictions can be found through the print statements in the file.  By running a diff with the 
solutions, I found that only 16/300 were incorrect for an accuracy of 94.7%.  To smooth, I decided that 
if the bigram did not appear in the language, then there would be no added probability for it.  
Diacritical marks and accents were thus eliminated from English considerations instead of having a +1
factor.  Of course, there are some words that are exceptions but I felt that including a large set of
all possibilities lost the refinement that a stricter set gives.  The strict set was very demonstrative 
of the actual languages too. Also, to avoid floating point problems, I added the logs as mentioned in 
the text analysis slides.  