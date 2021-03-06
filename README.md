
# Election_Analysis
## Project Overview
A Colorado Board of Elections employee has given Data Analysis, Inc. ("DAI") the following tasks to complete the election audit of a recent local congressional election.

*   Calculate the total number of votes cast.
    
*   By County:
    *   Get a list of counties in the vote.
    *   Calculate the percentage of votes for each county.
    *   Calculate the total votes for each county.
    *   Determine the county with the largest voter turnout.
    
*   By Candidate:
    *   Get a complete list of candidates who received votes.
    *   Calculate the total number of votes each candidate received.
    *   Calculate the percentage of votes each candidate won.
    *   Determine the winner of the election based on popular vote.

## Resources
- Data Source:  election_results.csv
- Software:  Python 3.7.6 Visual Studio Code, 1.59.1

## Results
The analysis of the election shows:

### Total Votes
  - There were 369,711 total votes cast in the election.
### Votes by County
  - The counties were:
      - Jefferson
      - Denver
      - Arapahoe
  - The county results were:
      - Jefferson county received 10.5% of the vote and 38,855 number of votes.
      - Denver county received 82.8% of the vote and 306,055 number of votes.
      - Arapahoe county received 6.7% of the vote and 24,801 number of votes.   
  - The largest county turnout was:
      - Denver
### Votes by Candidate        
  - The candidates were:
      - Charles Casper Stockham
      - Diana DeGette
      - Raymon Anthony Doane
  - The candiate results were:
      - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
      - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
      - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
  - The winner of the election was:
      - Diane Degette, who received 73.8% of the vote and 272,892 number of votes.
   
The data presented to the Colorado Board of Elections in text format was:
        
![Election_results_txtdata](https://user-images.githubusercontent.com/35401581/132077044-15f87f2e-9145-42c5-8203-60db8005d9e2.png)

## Summary
DAI was successful in providing accurate and timely election results to the Colorado Board of Elections.  The election results were tallied based on DAI's development of a Python coding script created by DAI's staff of experienced coders.  DAI worked with the Colorado Board of Elections to develop the script to accomplish their needs.  And, DAI wrote the script so that it could easily be applied to other similar elections.  In today's world voter integrity is a necessity.  DAI is offering to present this script to other election boards for implementation.

To that end, DAI can meet with other election boards so that the script fully meets their needs.  The script may require very few changes.  Specifically, a few modification examples could inlcude: 
   1. ***new data source file*** - Each election board would provide their own raw data file with the individual votes.  The raw data may be presented in a different format from one voting board to another.  In this event, a few tweaks to how the data is read into the script may be needed.  For example the code row locations ([2] and [1], respectively) can easily be changed to match the new Board's data file.
    
            candidate_name = row[2]
            county_name = row[1]
    
   2. ***further data breakouts*** - A voting board may also need data drilled down to include voting precincts as well as by county and by candidate.  Each county consists of multiple voting precints.  In this event, the script already developed for counties can easily be modified for precints and then added to the script as an additonal breakout.  For example,
 
            # The county code can be changed to precinct
            county_votes[county_name] +=1 
            precinct_votes[precinct_name] +=1

DAI is proposing a meeting with the election committee to allow for presentations of this program to other election boards.     
