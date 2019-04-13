# strat2file

_The International Chronostratigraphic Chart from International Commission on Stratigraphy, in computer readable formats._

Computer-readable versions of the [The International Chronostratigraphic Chart](http://www.stratigraphy.org/ICSchart/ChronostratChart2018-08.jpg). I couldn't find any, so I made a version for you. 

All rights belong to [International Commission on Stratigraphy](http://www.stratigraphy.org)

Please report any typos or suggest improvements, e.g. another way to represent the [American subperiods](https://en.wikipedia.org/wiki/Mississippian_(geology)). I might implement the colour scheme as well in future.

## Notebooks:

[strat2file](https://github.com/TobbeTripitaka/strat2file/blob/master/strat2file.ipynb) is the code just to convert excel spreadsheet to JSON, XML etc. 

[strat2my](https://github.com/TobbeTripitaka/strat2file/blob/master/strat2my.ipynb) is a function that takes a string of geological time and convert it to a number, e.g. Permian to 'average age', start and end: 
get_time('Danian') 
(63.8, 61.6, 66.0)

![Stratigraphy, Svalbard](https://github.com/TobbeTripitaka/strat2file/blob/master/fig/strat_img.jpg?raw=true)
_photo: Tobias Stål_
