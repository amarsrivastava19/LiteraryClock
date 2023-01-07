# Literary Clock
Building a clock that tells you the time through pages from famous books.


A few years ago, the Guardian proposed a clock that could tell you the time only using text from famous publish works. So, instead of a clock-face, you would instead see an excerpt written by James Joyce, Vonnegut, Shakespeare, etc. that contained some reference to what time it was. 

So, it might look something like this:

![image](https://user-images.githubusercontent.com/49100740/211166126-b43048e4-515c-4256-8fbe-ed01076abbeb.png)



I want to take the same idea, but use OpenAI's generative models to both illustrate these passages and potentially fill in missing gaps in the dataset.

Illustrating this dataset is kind of a trivial task as you simply need to call OpenAI's image generation API for however many quotes you wish the model to draw. 

Text generation on the other hand is a little more interesting, as you would want the model to mimic the base dataset, or maybe even draw from known authors such as Joyce and Shakespeare, in such a way that it can "sneak" the time of day into the story. 



Ideally, I'd like to take the finished clock and publish it free-to-use on the app-store for people to turn their phones or tablets into clocks. 


Free-to-use is the key part, as all good art is a profitless endeavor. 
