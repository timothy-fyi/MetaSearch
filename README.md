# A simple command line Meta Critic search tool

![Demo](https://i.ibb.co/BrN1K7X/metasearchdemo.gif)

# Installation steps:
1. Download .zip folder
2. Open your command prompt
3. Navigate to the folder where the .zip is downloaded (ex. ```cd C:\Users\your_name\Downloads```)
4. Type ```pip install meta-me.zip``` (ensure you are in the folder where the .zip is downloaded!)
5. Run Meta Search from your command prompt at anytime, just type ```meta "movie or tv show or game here"```

# Tips:
- If the movie/tv show/game has multiple words, ensure to wrap your query in quotes. For example: ```meta "houses october built"```

# Planned Updates:
- Retreiving expanded search descriptions (currently only displays visible text within the decription before the "Read More" setion)

# Known Bugs
- SOME searches may not return the results you are looking for, IF you don't type the EXACT name of the game/movie/tv show. For example, if you search "Diablo 2", "Diablo 4" will return, but if you search "Diablo II: Lord of Destruction", you will get the correct result. This doesn't happen with all searches, but in some cases it does. This isn't ideal, so I plan to improve the logic to fix this in the future.
- It is possible to run across some python specific errors, all error handling isn't captured yet