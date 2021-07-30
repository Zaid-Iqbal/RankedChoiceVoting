---


---

<h1 id="ranked-choice-voting">Ranked Choice Voting</h1>
<p>A Python porject that calculates the the winner of a Ranked Voting Contest</p>
<h2 id="skills">Skills</h2>
<ul>
<li>Data Strutures
<ul>
<li>Stack</li>
<li>Dictionary</li>
</ul>
</li>
<li>Text File Reading</li>
</ul>
<h2 id="requirements">Requirements</h2>
<p>Candidates.txt must be populated as follows</p>
<ol>
<li>[Candidate 1]</li>
<li>[Candidate 2]</li>
<li>[Candidate 3]</li>
<li>[Candidate 4]</li>
<li>[Candidate 5]</li>
<li>[Candidate 6]<br>
…</li>
</ol>
<p>An Example of this is</p>
<ol>
<li>Hannah Strickland</li>
<li>Rosa Vaughn</li>
<li>Shari Ruiz</li>
<li>Lucia Stokes</li>
<li>Jeannie Santiago</li>
<li>Sergio Moss</li>
<li>Victor Watkins</li>
<li>Wilbert Logan</li>
<li>Tanya Harmon</li>
<li>Joey Russell</li>
</ol>
<p>Votes.txt must be populates as follows</p>
<ol>
<li>[choice 1], [choice 2], [choice 3], [choice 4], …</li>
<li>[choice 1], [choice 2], [choice 3], [choice 4], …</li>
<li>[choice 1], [choice 2], [choice 3], [choice 4], …</li>
<li>[choice 1], [choice 2], [choice 3], [choice 4], …</li>
<li>[choice 1], [choice 2], [choice 3], [choice 4], …</li>
<li>[choice 1], [choice 2], [choice 3], [choice 4], …<br>
…</li>
</ol>
<p>An Example of this is</p>
<ol>
<li>10,5,2,4,7,6,1,9,8,3</li>
<li>6,10,2,8,5,9,4,3,7,1</li>
<li>1,6,4,2,5,10,8,3,9,7</li>
<li>10,1,4,8,3,5,6,7,9,2</li>
<li>4,3,8,10,2,7,6,9,1,5</li>
<li>4,10,7,5,8,3,1,6,9,2</li>
<li>5,9,10,7,1,8,4,6,2,3</li>
<li>7,8,9,2,4,5,10,6,1,3</li>
<li>4,6,1,9,2,10,7,5,8,3</li>
<li>1,10,5,6,9,8,4,2,7,3</li>
</ol>
<p>The rankings must be ordered using the number of the candidate. So, for example, voter #1’s order [1. 10,5,2,4,7,6,1,9,8,3] is</p>
<p>[1. Joey Russell, Jeannie Santiago, Rosa Vaughn, Victor Watkins, Sergio Moss, Hannah Strickland, Tanya Harmon, Wilbert Logan, Shari Ruiz ]</p>
<p>There should be no candidates repeated twice in the order, and each voter must rank every single candidate in candidates.txt.</p>
<h2 id="procedure">Procedure</h2>
<ol>
<li>
<p>Create a List[String] of candidates from candidates.txt where each candidate’s name is a String</p>
</li>
<li>
<p>Create a List[Stack] of votes from votes.txt where each vote is a Stack</p>
</li>
<li>
<p>Create a Dictionary[String,List[Stack]] where each candidate is defined by their List of votes</p>
<ul>
<li>Iterate through each vote in List[Stack] and peek each vote to see which candidate that vote should be appended to.</li>
</ul>
</li>
<li>
<p>Check to see if there is a winner in Round 1</p>
<ul>
<li>Iterate through the items of the Dictionary and just see which candidate has a longer list length
<ul>
<li>Longer list length = more votes</li>
</ul>
</li>
<li>If one candidate got &gt;50% of the votes then the program ends and that candidate is the winner</li>
</ul>
</li>
<li>
<p>If no one got &gt;50% of the votes, Run through each round of voting until one candidate remains</p>
<ul>
<li>Each round will do the following…
<ol>
<li>Find the candidate with the lowest # of votes</li>
<li>pop the top of the stack of each vote of the loser candidate</li>
<li>Redistribute the loser candidate’s votes based on that voters next choice in their rank
<ul>
<li>If the stack is empty, the vote card is deleted</li>
</ul>
</li>
</ol>
</li>
</ul>
</li>
<li>
<p>Step 5 is repeated until one candidate remains or there is a tie</p>
</li>
</ol>

