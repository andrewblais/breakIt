# breakIt

A [Turtle](https://docs.python.org/3/library/turtle.html) Breakout-style game

-->>
Written with Python OOP approach, many methods which I've tried to break down into
readable pieces.

The static folder contains lots and lots of lists of words for the typing test. I scoured
Project Gutenberg, Seinfeld scripts and other places for the data. This gave me a good
opportunity to practice my text-cleaning skills.

---

-->>
Future updates will include further separation of concerns and efficiency in the main
class.

More words and phrases to be added to the word banks. Suggestions welcome!

---

### Documentation:

_Printed via `help(LoremIpsum) in `lorem_main.py`:_

```markdown

```

---

## Assignment for Angela Yu's Course:

### I created this project in completing Day 87, Professional Portfolio

**Project - [GUI]: _Assignment 6, "Breakout Game"_**

- _from [Angela Yu 100 Days of Code](https://www.udemy.com/course/100-days-of-code/)_

### Here are the instructions for the assignment:

**Assignment: Breakout Game**

_Using Python Turtle, build a clone of the 80s hit game Breakout._

Assignment instructions

Breakout was a hit game originally coded up by Steve Wozniak before he and Jobs started
Apple. It's a simple game that is similar to Pong where you use a ball and paddle to
break down a wall.

[Breakout Wikipedia Page](https://en.wikipedia.org/wiki/Breakout_(video_game))

![Breakout Game Image](./.projectReference/imagesCreation/breakout.png)

You can try out the gameplay here:

https://elgoog.im/breakout/

A good starting point is to review the lessons on Day 22 when we built the Pong game. But
you will have plenty of things to Google, figure out and struggle through to complete
this project. Try to avoid going to a tutorial on how to build breakout, instead spec out
the project, figure out how it's going to work. Write down a checklist of todos and draw
out a flow chart (if it helps).

### My reflections on the assignment:

The course asks:

```
This is a place to journal your experience of completing this project. This will help you
figure out how to improve as a developer.

Write down how you approached the project. What was hard, what was easy. How might you improve
for the next project? What was your biggest learning from today? What would you do differently
if you were to tackle this project again?
```

My answers:
-->>
Here's my projects repo's address: https://github.com/andrewblais/checkPracticeTyping

It was helpful having completed the Image Watermarking assigment prior to this, which
really
refreshed my memory on using Tkinter.

I set up the skeleton of the GUI and added/refined which widgets should appear after much
trial and
error and after seeing what worked best for the simple interface I was trying to achieve.

I did a better job in this project of waiting to make sure the core functionality was
operational before
adding bells and whistles and fine-tuning.

When my brain got too tired from figuring out some of the more advanced concepts to do
with getting the functionality
beyond just the appearance to work, I enjoyed scouring the Internet for word lists I
could use for my typing test's
data.

The hardest part was getting the functionality around checking the user's entries
compared with the text they are
typing. Also, getting the timer countdown functionality was hard, too. I did a lot of
work looking at Tkinter
documentaion, Stack Overflow/Geeks for Geeks/W3 and other resources, and ChatGPT 3.5 was
very helpful when
I got stuck and needed a tutor.

I did my best to refer to these references and not depend on them or copy anything,
originality and creativity
are important to me and I strive to create a fun, unique project.

I also used PyInstaller to generate a standalone .exe for non-Python users. This was
tricky, especially
integrating with the (venv) and getting the Bash commands right.

I'm happy with the outcome, the simplicity of the GUI and ease-of-use.

Much refactoring is needed to simplify the main class methods and provide better
error-handling, but I'm happy
for now and ready to submit my work.

What did I learn? I learned to take my time and approach big projects like this with
simplicity and functionality
on a basic level in mind. I easily get ahead of myself with goals that might be too
complex for the task at hand.
I did follow through on some of the more complex goals, but it took over a week to
complete this assigment. I think
that's okay, though. 100 Days is probably more like 400 Days for me, as I'm a very slow
and methodical learner.
I'm not in a rush, so I'm trying to give myself permission to go at my own pace and use
the '100 Days' as a guide
but not a rule.

Next project I may try to do a bit faster and make a bit simpler.

Thanks for the guidance and encouragement, Angela!!
