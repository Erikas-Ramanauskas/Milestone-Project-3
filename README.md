# Diablo 4 Trading

[View the live project here](https://milestone-project-3-89cfc062fae7.herokuapp.com/)

Diablo 4 trade is a website specificaly dedicated to a game "Diablo 4" relesed not long ago. The purpose of the website is to allow dedicated players share the items they have recieved in game and trade for in game currency with other players. The game it self does alow trading but there is no marketplace or auction house to alow item "posting".

![Screenshot of Tedoku on multiple device](./static/images/read_me/responsive.png)

![GitHub contributors](https://img.shields.io/github/contributors/Erikas-Ramanauskas/Milestone-Project-3) ![GitHub last commit](https://img.shields.io/github/last-commit/Erikas-Ramanauskas/Milestone-Project-3) ![Languages](https://img.shields.io/github/languages/count/Erikas-Ramanauskas/Milestone-Project-3) ![GitHub forks](https://img.shields.io/github/forks/Erikas-Ramanauskas/Milestone-Project-3)

---
**Table of Contents**

- [Diablo 4 Trading](#diablo-4-trading)
  - [Overview](#overview)
  - [User Experience (UX)](#user-experience-ux)
    - [First Time Visitor Goals](#first-time-visitor-goals)
    - [Returning Visitor Goals](#returning-visitor-goals)
    - [Frequent Visitor Goals](#frequent-visitor-goals)
  - [Design](#design)
    - [Colour Scheme](#colour-scheme)
    - [Typography](#typography)
    - [Imagery](#imagery)
  - [Wireframes](#wireframes)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
      - [Designs \& Wireframes](#designs--wireframes)
      - [Additional helpers](#additional-helpers)
      - [Programming Languages](#programming-languages)
      - [Libraries \& Frameworks](#libraries--frameworks)
      - [Databases](#databases)
      - [Hosting](#hosting)
      - [Version Control](#version-control)
      - [Testing](#testing)
    - [Frameworks and Programs Used](#frameworks-and-programs-used)
  - [Bugs and Solutions](#bugs-and-solutions)
    - [Main chalange faced and decitions made](#main-chalange-faced-and-decitions-made)
      - [Atempt no 1](#atempt-no-1)
      - [Atempt no 2](#atempt-no-2)
    - [Solved Bugs during developing](#solved-bugs-during-developing)
    - [Remaining Bugs](#remaining-bugs)
    - [Ideas for Future Developments](#ideas-for-future-developments)
  - [Application Ida and functionality](#application-ida-and-functionality)
    - [Game board dimentions](#game-board-dimentions)
    - [Shape creation](#shape-creation)
    - [Drag and drop](#drag-and-drop)
    - [Local storage](#local-storage)
    - [Failure](#failure)
  - [Deployment \& Local Development](#deployment--local-development)
    - [Deployment](#deployment)
    - [Local Development](#local-development)
    - [Making Local Clone](#making-local-clone)
  - [Credits](#credits)
    - [Mentor](#mentor)
    - [Codes](#codes)
  - [Acknowledgements](#acknowledgements)
  - [Copyrights](#copyrights)

---

## Overview

The website main purpose is to trade digital in game items using in game currentcy. Every registed user has an ability to post item according to the class they play, item type and unqique suffixes and affixes. Once item is posted another user can add a bids of minimum 100k per bid but never lower or the same price. Once the owner gets a bid that he is happy with he can accept the trade. Message with another player and share his Discord or Battlenet Id's. Once the trade happens in the game, both players can confirm the that they have traded in the game and they recieve trade contribution on their profile. 

## User Experience (UX)

### First Time Visitor Goals

* As a First Time Visitor, I want to be able to immediately understand the main purpose of the application, "Diablo 4 trading".
* As a First Time Visitor, I want to be able to understand were i can find traded items and prices.
* As a First Time Visitor, I want to be able to filter items by my requirements.
* As a First Time Visitor, I want the pages to be responsive to be my device, no matter it's size.
* As a First Time Visitor, I want to be easily register and post my own items.

### Returning Visitor Goals

* As a Returning Visitor, I want to be able to comunicate with other users with messages.
* As a Returning Visitor, I want to see my own and other user profiles.
* As a Returning Visitor, I want to be able make my own settings for Class I am playing.
* As a Returning Visitor, I want to be able make my own settings for game mode I am playing.
* As a Returning Visitor, I want to be able see the items i have posted previously by going to my profile.
* As a Returning Visitor, I want to be able to see other user posted items on their website.
* As a Returning Visitor, I want to be able to see and acsses to a messages that i have sent and recieve.

### Frequent Visitor Goals

* As a Frequent Visitor, I want to be able easily filter items by class, item type, game mode, and precise affix customisation.
* As a Frequent Visitor, I want to be able to keep improving trade score to build up reputation of trusted trader.
* As a Frequent Visitor, I want to be able to acsses all messages and see when they were recieved.


## Design

### Colour Scheme

* The main colours came from some play around **teal accent-3** from [Materialise](https://materializecss.com/color.html) colour choices and using **grey darken-3** 

* All other colours were generated using [Adobe colour wheal](https://color.adobe.com/create/color-wheel) opposite orrange and gold colours as well as green for diferent parts of the website

* Only exception to th above were bacground colours in messages.htm with **teal accent-2** and **teal accent-1** alternating between 2 to have each line to stand out from bacground and surounding lines.
  
* I decided to leave background plain as with many diferent color components it would make the website to busy.

### Typography

- Due to website is mostly heavy with text and writen information and no immages it is important for reader to be easily read it. I chose Roboto as a main font for all the text and Lora font for the headers. All of it added with 1px letter spacing.

### Imagery

- There are no images in the website apart from logo that was generated in [FontBolt](https://www.fontbolt.com/font/diablo-font/) and [Background remove](https://www.remove.bg/upload). Additionaly preloader was generated by [Icons8](https://icons8.com/preloaders/)

## Wireframes

* Desktop home page
* ![Home page / offers (desktop)](./assets/readme-images/wireframes/home-page.webp)
* Mobile home page
* ![Home page / offers (mobile)](./assets/readme-images/wireframes/home-page-phone.webp)
* Create offer page
* ![Create offer page (desktop)](./assets/readme-images/wireframes/profile.webp)
* Mobile Create offer page
- ![Create offer page (mobile)](./assets/readme-images/wireframes/base-board.webp)
* Messages page
- ![Messages page (desktop)](./assets/readme-images/wireframes/gameplay.webp)
- Mobile Messages page
- ![Mobile Messages page](./assets/readme-images/wireframes/base-board.webp)
* Message page
* ![Message page](./assets/readme-images/wireframes/game-components.webp)
- Mobile Message page
- ![Mobile Message page](./assets/readme-images/wireframes/button-layout.webp)
* Profile page
- ![Profile page](./assets/readme-images/wireframes/phone-landscape.webp)
* Register page
- ![Register page](./assets/readme-images/wireframes/phone-portrait.webp)
* Log in page
* ![Log in page](./assets/readme-images/wireframes/phone-portrait.webp)

## Features

| # | Feature | Desirability | Importance | Viability | Delivered |
| :---: | :--- | :---: | :---: | :---: | :---: |
| | Navigation | | | | |
| --- | --- | --- | --- | --- | --- |
| 1 | Offer page | 5 | 5 | 5 | ✅ |
| 2 | Request page | 3 | 3 | 3 | ❌ |
| 3 | Create offer page | 5 | 5 | 5 | ✅ |
| 4 | Messages page | 5 | 5 | 4 | ✅ |
| 5 | Individual message page | 5 | 3 | 4 | ✅ |
| 6 | Profile page | 4 | 3 | 3 | ✅ |
| 7 | Item page | 5 | 5 | 5 | ✅ |
| 8 | Log in page | 5 | 5 | 5 | ✅ |
| 9 | Register page | 5 | 5 | 5 | ✅ |
| 10 | Messages link displays unread message number | 4 | 4 | 5 | ✅ |
| 11 | Scrolling on messages display pop up with latest messages | 3 | 4 | 4 | ❌ |
| -- | --- | --- | --- | --- | --- |
| | Offers page feautures | | | | |
| --- | --- | --- | --- | --- | --- |
| 12 | All offers loaded on page load | 5 | 5 | 5 | ✅ |
| 13 | Filter functionality to narrow down the list of offers | 5 | 5 | 5 | ✅ |
| 14 | Ability to go in to individual item profile | 5 | 5 | 5 | ✅ |
| 15 | Ability to go to other users profile | 5 | 5 | 5 | ✅ |
| 16 | Statistics of last trades on the side | 3 | 3 | 3 | ✅ |
| 17 | Filter functionality auto setup acording to user profile. | 5 | | | ✅ |
| -- | --- | --- | --- | --- | --- |
| | Profile page and Profile Edit | | | | |
| --- | --- | --- | --- | --- | --- |
| 18 | Ability to see personal and other people profile | 5 | 5 | 5 | ✅ |
| 19 | Personal profile has ability to be eddited | 5 | 5 | 5 | ✅ |
| 20 | Class can be eddited | 4 | 4 | 5 | ✅ |
| 21 | Game type can be eddited hardcore/ season | 4 | 4 | 5 | ✅ |
| 22 | Ability to add personal Battlenet id | 5 | 5 | 5 | ✅ |
| 23 | Ability to add personal Discord id | 5 | 5 | 5 | ✅ |
| 24 | Both ids only visable to to the owner | 4 | 4 | 5 | ✅ |
| 25 | User profile also displaying how many trades was made by user. | 5 | 5 | 4 | ✅ |
| 26 | Visiting other people profile ""message"" button is vissable and functioning | 5 | 5 | 4 | ✅ |
| 27 | User profile settings functions as helpers for filter options and item create options | 5 | 5 | 5 | ✅ |
| -- | --- | --- | --- | --- | --- |
| | Offer creation page functionality | | | | |
| --- | --- | --- | --- | --- | --- |
| 28 | Creation of item starting with class and game type buttons prefiled from profile | 5 | 5 | 5 | ✅ |
| 29 | Once item is selected Suffixes and Affixes butons are generated | 5 | 5 | 5 | ✅ |
| 30 | Once Affix buttons are seleceted (up to 4) the range is selected. | 5 | 5 | 5 | ✅ |
| 31 | If more than 4 affixes seleceted the 5th one will indicate that choice is unavialable | 3 | 4 | 5 | ✅ |
| 32 | The price button is starting at 100k and able to increse by 100k or 1m | 5 | 5 | 5 | ✅ |
| 33 | Add item buton is disabled untill 4 affixes are selected | 5 | 5 | 5 | ✅ |
| 34 | Suffix affixes autoselects the first one and if more options avialable user can change. | 5 | 5 | 5 | ✅ |
| 35 | If different item is selected the affixes that matches stays and others changes | 5 | 5 | 5 | ✅ |
| -- | --- | --- | --- | --- | --- |
| | Individual offer page | | | | |
| --- | --- | --- | --- | --- | --- |
| 36 | Offer page displaying offer details | 5 | 5 | 5 | ✅ |
| 37 | Page also displayes initial price and by who item is created | 5 | 5 | 5 | ✅ |
| 38 | For the owner of offer ""no bids made"" message displayed if bids are not made yet | 5 | 5 | 5 | ✅ |
| 39 | If bids are made ""accept offer buttons apears"" | 5 | 5 | 5 | ✅ |
| 40 | Owner also has delete button with confirmation for offer | 5 | 5 | 5 | ✅ |
| 41 | Owner after accepting bid, has button to accept trade | 5 | 5 | 5 | ✅ |
| 42 | Offer page displaying every bid by other users and when it was made | 5 | 5 | 5 | ✅ |
| 43 | For visitor bid functionality is vissable and functioning | 5 | 5 | 5 | ✅ |
| 44 | For visitor if their offer is accepted by the owner instead of bid, accept trade button is shown | 5 | 5 | 5 | ✅ |
| -- | --- | --- | --- | --- | --- |
| | Messages page | | | | |
| --- | --- | --- | --- | --- | --- |
| 45 | Messages list is layed out vertical format | 5 | 5 | 5 | ✅ |
| 46 | Every even message is different background color from odd messages | 5 | 5 | 5 | ✅ |
| 47 | Visual indication wich messages have not been read by the user | 5 | 5 | 5 | ✅ |
| 48 | Message info displayes username, time, and message it self | 5 | 5 | 5 | ✅ |
| 49 | Last message displayed and cut off it it does not fit in the screen | 5 | 5 | 5 | ✅ |
| 50 | If offer is accepted custom message is displayed | 5 | 5 | 5 | ✅ |
| -- | --- | --- | --- | --- | --- |
| | individual message page | | | | |
| --- | --- | --- | --- | --- | --- |
| 51 | All past messages vissable with the newest one being at the bottom. | 5 | 5 | 5 | ✅ |
| 52 | Main message screen is scrolled individualy | 5 | 5 | 5 | ✅ |
| 53 | Message send fuctionality added at the bottom | 5 | 5 | 5 | ✅ |
| 54 | Recieved messages showed on left in different color | 5 | 5 | 5 | ✅ |
| 55 | Sent messages displayed on right in different color | 5 | 5 | 5 | ✅ |
| 56 | Share id's button with modal confirmation | 5 | 5 | 5 | ✅ |
| 57 | Share id's button automaticaly sending message with personal id's | 5 | 5 | 5 | ✅ |
| 58 | Id's messages looks sliglty different | 5 | 5 | 5 | ✅ |
| 59 | When offer accepted, unique message is sent with item link and price accepted. | 5 | 5 | 5 | ✅ |
| -- | --- | --- | --- | --- | --- |
| | No loged in user restrictions | | | | |
| --- | --- | --- | --- | --- | --- |
| 60 | Profile button is not vissable | 5 | 5 | 5 | ✅ |
| 61 | messages button is not vissable | 5 | 5 | 5 | ✅ |
| 62 | Create offer button links to log in page | 5 | 5 | 5 | ✅ |
| 63 | Register button vissable | 5 | 5 | 5 | ✅ |
| 64 | Log in button visable | 5 | 5 | 5 | ✅ |
| 65 | Clicking other user profile link leads to log in page | 5 | 5 | 5 | ✅ |
| 66 | Clicking on bid button leads to log in page | 5 | 5 | 5 | ✅ |

## Technologies Used

### Languages Used

#### Designs & Wireframes

- [Figma](https://www.figma.com/) was used to create wireframes

#### Additional helpers

- [Google sheets](https://drive.google.com/drive/folders/1OLCTh5KtMTvXfx9U45FlNVfcStfZ6Db5) 2 sheets have been used.one to gather and rework database of item affixes [link](https://docs.google.com/spreadsheets/d/13bXVxjCteAYxh9K5A2vyceVEUQsKByxaTxm2bozIFCs/edit?usp=drive_web&ouid=118192088859168429060)  and other parameters and another for quicker testing and feutures coding [link](https://docs.google.com/spreadsheets/d/1in7fgqgPXNS0XWtpCu7ox2mpkWDGmuAPJVuSlucCqfk/edit#gid=0)

#### Programming Languages

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

#### Libraries & Frameworks

[Materialize](https://materializecss.com/navbar.html)
[jQuery](https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white)
[Font Awesome](https://img.shields.io/badge/Font%20Awesome%20-%23339AF0.svg?&style=for-the-badge&logo=Font%20Awesome&logoColor=FFFFFF)
[Google Fonts](https://fonts.google.com/) fonts used to import main fonts for the page.
[Favicon](https://favicon.io/favicon-converter/) was used to create favicon.
[Flask](https://flask.palletsprojects.com/en/2.3.x/)
[Jinja](https://jinja.palletsprojects.com/en/3.1.x/)



#### Databases

![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)

#### Hosting

![GitHub Pages](https://img.shields.io/static/v1?style=for-the-badge&message=GitHub+Pages&color=222222&logo=GitHub+Pages&logoColor=FFFFFF&label=)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white) !

#### Version Control

[Git](https://git-scm.com/) was used for version control.
[Visual studio code](https://code.visualstudio.com/) Used for several fucntion testing
[CodeAnywere](https://codeanywhere.com/) was used as online IDE for GitHub and the terminal was used to add and commit to Git and push to GitHub. 
[GitHub](https://github.com/) was and is being used as repository of the project source code and for deploying the site/ application.

#### Testing

- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) was used to test the code and debug the code during the development process.

- [W3C Markup](https://validator.w3.org/) Validation was used to test HTML code
- [W3C CSS](https://jigsaw.w3.org/css-validator/) Validation Service was used to test CSS code

### Frameworks and Programs Used


* 
  







## Bugs and Solutions

### Main chalange faced and decitions made

Before going in to individual smaller bugs one issue and soliution requires its own separate topic: Drag and Drop **multiple** components.

*Note I had 2 attemps at solving the whole drag and drop functionality atempt no 1 was writen after I sorted it using mainly drag and drop event listeners for PC ounly, however when I started working on it again to set it up for touch functionality I reprogramed it to work with pointer event listeners instead that solved most if not all problems I had in first attempt*

#### Atempt no 1

* Due to a nature of the game one of the requirements for the code is to create a shapes of multiple squares and have them interact with game board individualy.
* While drag and drop functionality was new for me (not in the course) I reasearched few vidoes but the one that was my main source of information was by [Traversy Media](https://www.youtube.com/watch?v=C22hQKE_32c&t=360s) with added info from [MDN database](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API). I used this as my louchpad of drag and drop "playground" which after few trial and error was simple enough for single element.
* How ever problems started when I tried to do 2 things: Drag more than one element and scale element I am dragging.
* [Drag and Drop API](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API) has its onwn listener functions quite similar to mouse events and one of events drag over was my hope to be a triger for each of the shapes I am draging, however there was no posibility of draging multiple sibling elements.
* One of the ways I tried was using *dispatchEvent()* function but it completley crashed browser due to events boucing between siblings.
* Another idea sugested by a friend to attach the shapes to a mouse cursor using: *position:absolute* and width height properties. However at that moment I relised it is not needed, as it alow user to be flexible and click anywere he wants on the shape without having pices to snap around.
* Another issue was to do with practicaly all *mouse* events not trigering during the drag and right after dragdrop. To my understadning all of mouse events are transfered to drag functions. I had to adopt a mix of both for the final result.
* My soliution was to capture mouse position when it is clicked on one of the shapes. In turn I captured a parent div > and taken its children > recorded all X and Y cordinates and calculated center of each shape boxes. This way using *dragover* listener that gave me current mouse position, I was able to calculate all active boxes of the shape while draging their parent.
* Additionaly I captured all game board dropboxes coordinates at the start of drag of all 4 of their edges and using simple conditional testing I was able to check when ever draggable box center enters the squares, and used same principal of functionality to place them in while I did not directly appended the children as in the video (that would coused parent div to go inside of one of boxes only)

* Lastly the issue I had that once something is beign dragged it CAN NOT be modified via css.
* This was important for me to do as my game board is 9x9 squares and on the side I wanted to fit 3 or even 4 game shapes that could be as big as 4x4. Taking that together it is 12 or even 16 squares each in the same space as game board *check early wireframes*. this means I had to make them smaller than game board sqaures and scale them up as the player pick them up. *That is how original game I got an idea from works*
* I have been searching multiple ways to achieve this, via *scale*, changing width and height, transforming, creating element bigger and fitting in the smaller box yet the design of draggable "shadow element" did not change.
* On top of it any element that is parent of draggable element transfers background color to dragable element and no traditional css rule has changed that, causing the same "grandparent" colour to stay on invisible *inactive* squares and edges were border radius was present. The only element background color was not takign was "body".
* Since I spend a large portion of time on these 2 problems and one of them was solved I decided to change a desing of the game and create shapes of the same size as the game board by fitting less of them or rearanging the layout as well as adding no backgroudn to parent divs.
* this is something I would like to revisit in a future and build up my orriginal vision.

#### Atempt no 2

* Once I returned to drag and drop functionality weeks later to make it responsive on touch screens as well I researched videos about events that works with touch screens and stuck on [Web Dev Simplified](https://www.youtube.com/watch?v=MhUCYR9Tb9c) as my main reference. However drag events were still not working with touch.

* I discovered [this video](https://www.youtube.com/watch?v=GU3lQTbwUZc&t=275s). The main idea was to atach anything I am tryign to drag to a mouse after the click with *position:absolute and left+right*. Same idea I have goten from friend Olegas (who is js/react developer) however I dismised it early on before. I used this idea this time to try to make pointer events being main caller for both touch and mouse events. And managed to figure out 90% of code idea my self.

* The Brekathough hapened when I found this [article](https://javascript.info/mouse-drag-and-drop) That essentialy contained everything I have figured out up to that point and more to solve this puzzle. The final piece missing was this code that I took from article:

````
 ball.ondragstart = function() {
 return false;
};
````

* All of previous problems were solved essentialy with pointer video and this article makign game function on both touch and mouse events. As well as no longer bound to drag events allowing me to edit css if I wish so and removing weird bug that would not record shape centers and cousing shape to disapear uncontrolable.

* if I have to work with drag and drop or I recomend anyone to do it [Web Dev Simplified](https://www.youtube.com/watch?v=MhUCYR9Tb9c) and [article](https://javascript.info/mouse-drag-and-drop) is ideal guide for this type of purpose.

### Solved Bugs during developing

* There were a bug that coused the bigger shapes of 4 width or height to split up and take over 5 leaving 1 as a gap. this is due to js maths and resizing and causing the drop area being bigger than a shapes squares. When retrieving data of shapes X and Y I added to the top and left 1% (multiplied by 1.01) as well as divided right and bottom edges by the same. This seems to solve the problem, yet the player will have to more accurate on droping shapes than innitialy.

* Several resizing issues were detected when changing direction in the phone mode, and especialy when resizing sreen size while testing in responsive mode. Main issue was that shapes and buttons mostly relied on game board dimentions. During resize event listener the order of functions were not in order and changing them around *gameBoardAndScreenDimentions();* first and *setShapesContainerSize();* after seem to solve the problem

* Initialy I had event listeners added to a dragEnd listener *if* section which checks if shape was droped in the game board thus creating new shape and at the end adding new event listeners. However there is an existing bug that sometimes the droped shape does not apear on the game board and new shape is created insted but no event listeners are added to new shape making the shape unusable for the remaining of the game. Instead I created spearated function and called after *if* statement and to reset all event listeners every time drop down is perfomed. **Solved with atempt no 2 of drag and drop**

* Home page design was relatively smooth apart a few lineup problems that were solved using bootrstap classes and mainly sticking with mb-5 and row/col classes. However one isue that at the 2 examples of combination the text was wraping diferenly since one had a longer text. This automaticaly pushed one of pictures lower than the previous one at certain sceen breakpoints. Simple soliution I found is to place invisible span text at 1400 px when the breaking of the text start so it would treat it as extra word and snap aditional rows together at the same breakpoints. How ever I would love to find out if the is simple css soliution to conect 2 elements and comand them to be same size.

* Within game screen window I have added 2 buttons for rotation and used Font awesome icons. However a regular use of them complicated a size of them and on diffenrent screens they did not responded how I wanted. There were to many situations I had to work with to make them right. I decided to try out svg file instead but FA icons requires premium account. Eventualy I meved on to creating my own icons using simle google drawings that I am well familliar with and downloaded them as as svg file and used a code from it alowing me to customize them and add in property that worked for all screen sizes

* Navigation bar responsivnes using botstrap nav-bar to be open when on smaller devices and not being able to close, I spend some time tryign to figured out why it was hapening untill I simpley deleted and started over from 0 with navigation bar when I realised I linked botstrap twice. Both of starting from scratch and deleting extra link solved an issues.

* navigation bar bootstrap class sticky was not working either how I wanted so I used a JS code i knww from Udemy course.

* **Moved from remainign bugs** There is a rare occouring bug that when the shape is droped in the game field sometimes it does not regiter but a new shape is created instead anyway. It hapens rarely and I am not sure why it hapens or how to create the bug manualy or how to solve it at the moment. **Solved with drag and drop atempt no 2**

### Remaining Bugs

* Sometimes when draging one shape a second active game shape moves in to a place of active shape but moves right back once first shape is droped. This does not actualy effect the game play just a visual clutter

* If screen size is changed after dragin a shape and placing it back the shape retains dimentions of original screen size. This is not a problem in most cases apart in practice it could be a problem with galaxy fold if player does this and opens or closes the phone.

* Testing on phone model One Plus it seems the overflow-x: hidden; does not work and the screen can be dragged left and right a bit

### Ideas for Future Developments

* Future developments to improve on the existing game:
  * Return to original idea of having 3 shapes for the game as additional future. Expanding on this idea there could be an option to customise players gameplay with multiple shapes up to 4
  * Animation affects for placing shapes and destroying shapes
  * Reward system unlocking different "Skins" for the game board and background for example when player reaches certain amount of points, makes large combo of 6 or more, Gets destruction streak and many more could be added. Skins essentialy changes a colours of game board and game pieces.
  * Reward player with additional sounds to replace originals.
  * Highscores screen were you can see other players top 10 or even top 100 and compete every week.
  * Multiple functionalities changign the game play
    * Fliping shapes in mirror insted of rotating
    * Rewarding players for makign a streak instead of combination
    * Randomly deleting squares and creating other onces
    * Creatign random squares that rewards extra points or rotation points
    * Creatign random squares that blocks a destruction for x amount of moves
    * Creating new random shape set after shape is droped.
    * Giving a timer for the game and rewarding extra time every time destruction is done (like chess blitz)
    * Making player versus player game
  * All of ideas above could be combined in to a random ruleset given for players every week encouraging them to fight for best scores every week and creatign more replayibility.

## Application Ida and functionality

### Game board dimentions

* Since the game board is always square I had to account for a space from top and bottom for meniu buttons, score as well as shapes. I wanted to ensure that mobile users are able to play game either verticaly and horizontaly unlike the game I got the idea from. main function looks for the min between landscape and portrait and determines wich way the board and everything else needs to lay out.

* Because the board is 9 squares I added 1/2 square distance as a boarder around making everythign else some sort of division by 10 and multiplication by X depending how I wanted everything to be layered.

* One note on this that I would like to improve the code and instead create variables in javascript and do all the math instead on CSS. However this would require some time to investigate and figure out for me.

* Game board squared for later use are called in columns rows and square classes durign redering with some math. This helps later to find wich columns rows or squares are fully filled.

* Additionaly resize event listener changes the game board depening on the screen size as well as record all open game dropbox squares for later when pointerMove and pointerUp functions are called. This is to ensure fresh data is kept if window changed dimentions

### Shape creation

* In order to create shapes I wanted first of all a tool to create them. I used my skills in google sheets to create [this](https://docs.google.com/spreadsheets/d/1rQbG19eHYj0ltU_YNrQAcVxWLgIqnsbVytKtXd3tatI/edit) spreadhseet that alows me to easily create shapes object with true/false values. It essentialy detects how far the shape goes (always starting shape from top left corner) and determines if it is 1x1, 2x2, 3x3, or 4x4 square. This is important to keep in the squares always as other functions manipulate it easier.

* Once I got an array ready it is all about manipulating and selectg them. randomInt(min,max) function alowed me to get random number betwen 2 given digits. Using this I chose random number betwen 0-1000. I assing each shape dificulity a procentage in thousands Starting with Easy(910), medium(60) and hard(30). Then chose random number. If it rolls anywere between 0-910 it is easy shape, then if it rolls more than 910, else if statement then looks if it is not bigger than easy+medium (970) resulting in medium shape, then last else automaticaly allings with hard. Lastly since each shape dificulity contains ten I go with randomInt(0-9) and get random shape from list of 10.

* Then it comes given shape manipulation. There are 2 things. Miroring the shape, esentialy fliping verticaly and rotation. 2 functions created to handle that as per my plan I made in quick google drawing and simply rearanging the the order of the shape array. As for rotationg shapes the function does it clockwise but if done 3 times it is a same if done anticlockwise

 ![Mirror rearangment](./assets/readme-images/Shapes%20mirroring%20arrangement.webp)
 ![Rotation](./assets/readme-images/Shapes-rotation-arrangement.webp)

* Finaly the array is rendered and added shape-window element and given a class of draggable * shape width that are prepared with different measurments to ensure shape always stays in the center.

* For a new shapes to apear the functionality is implemented that the % of the easy/medium/hard shapes would be adjusted every turn. To ensure that it does nto get very dificult right away from my math knoweladge I knew if I make formula with power of **0<x<1** it will create [diminishing return](https://docs.google.com/spreadsheets/d/1i6MG8unq6J_bRvPEdR8JG7CDxI9pEpCv1-BizUnFuhA/edit#gid=0) starting with fast increcement and slowly adding less and less to a % of medium and hard shapes. It took a bit of gameplay between my friends to tune the nubers down but it can be easily adjusted again. I also added turn treshold to start trigering this formula in action to delay dificulity from the start and allowing player for window of oportunity at the beginign to build up some combos.

### Drag and drop

* I mostly explained the isues and idea of drag and drop within bug section. However notibly 3 functions of pointerDown / ponterMove / pointerUp works along side each other to practicaly set everything off in the game that hapens.

* pointerDown runs functions that once clicked on the shape it records active shapes centers in to object, as well as ads new static dimentions instead of % (this creates bug mentioned earlier) to the shape and finaly alowing the shape to be draged.

* pointerMove mostly works with checking shapesBoxesCoordinates versus dropBoxesCenters to find an equal match and once all squares find its partner the highlight class is given to mark dropable locations for the shapes and deleted every time pointer move event is called again so it ensures that highlight class is not left over. (As I wrote this I think this could be a good idea for painting program or game that you draw or contol with mouse movement)

* Drag Center Concept
* ![Drag centers concept](./assets/images/dragable-squares-location-concept.png)

* Additionaly highlightTiles() checks if player has matching squares of 9 or more and highlights in red that the shapes could be destroyed.

* pointerUp is were the magic happens. Most of functionality is run right after player lifts mouse/finger and there are 2 ways: either drop shape in right place or not. It runs the same function as pointerMove checkign for avialabe squares

* In case the shape is droped in the wrong place the shape simply returns back and nothing hapens. However if the shape is droped in the game board multiple things hapens:

* The game creates new shape insted using the proces I described before
* The game checks if the shape is creating a 9 or more group using same highlightTiles() function and trigers destruction of the shapes (Esentialy changes classes)
* The game also check for end game takeing both shapes array, creatign matrix out of it. Deleting uneceseraly rows and colums and then runign every posibility agaisnt game board via trigerGameOverCheck() function. This also includes creating aditional matrixes for each varition of ucrrent shapes in case the player has turns left essentialy detecting when player has no more moves.

* In all of above procces 2 audios played, one for placing the shape and one for destroying squares.

* Additionaly droped shapes also runs multiple functions calulationg points for current and top scores as well adding rotation points if player deserved them.

### Local storage

* I wanted to ensure that the player is able to leave and return to the game when ever pleses and not forced to play entire game as high level and patience players may take much longer time. In order to do this I used local storage to be activated every time the shape is droped.

* Local storage serves 2 purpose: load up and replace empty board on page load, and fill shapes and points when the wensite is loaded again as well as load up high score in the hiscore window.

### Failure

* I may call it this way but we all know that learning something is never a failure.

* During a call with mentor Gareth I mentioned the idea that I wanted highscores for players to see, he gave me an idea to use google sheets API to set it up as database to record top 10 or more players in every category. However I failed to make Google Sheets API work for me. I dont believe it was programing issue but more of seting up and account so google would alow me to upload data. Something in the settings that I did not fully understand from their documentation caused API inacsessible. Since is spend to much time on it already I decided to drop that feature until further I learn backend and server managment.

## Deployment & Local Development

### Deployment

* The project was deployed to GitHub Pages using the following steps:

1. Login or signup to GitHub and locate the GitHub Repository [GitHub Repository](https://github.com/Erikas-Ramanauskas/Milestone-Project-3).
2. On the repository page, navigate to Settings and click on it.
3. Within the Settings page, under Source choose Branch: main, then /root and click Save.
4. After about a minute, the site is published.

### Local Development

* How to Fork
To fork the repository, use the following steps:

1. Login or signup to Github and locate the repository.
2. Click the Fork button in the top right corner

### Making Local Clone

1. Login or signup to GitHub and locate the GitHub Repository [GitHub Repository](https://github.com/Erikas-Ramanauskas/Milestone-Project-3).
2. Under the repository name, click "clone" or "download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open the terminal in your preferred code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type git clone, and then paste the URL you copied in Step 3.
6. Press Enter. Your clone will be created.

## Credits

### Mentor

* Gareth was fenomenal in helping and advicing on my creativity plan and gave helpfull tips and inspiration with this project. Masive thank-you to him

### Codes

* Credit to [Jonas Schmedtmann](https://www.udemy.com/user/jonasschmedtmann/) udemy Course that I learned midjority of javascript before starting Code institute course. Notable code taken apart general lessons I learned:

* randomInt() function
* Entire index.js file, creating apearing sections on scroll as well as sticky navigation bar
* Local stotage functionality

* Credit and thanks to numerous tutorials on YouTube by seasoned developers.
  * Thanks to [Web Dev Simplified](https://www.youtube.com/@WebDevSimplified) for a number of code lessons in various topics;
  * Thanks to [Kevin Powell](https://www.youtube.com/@KevinPowell) for a number of code lessons in various nainly CSS designs that I learned for this and previous project;
  
## Acknowledgements

[Tripledot Studios](https://apps.apple.com/us/developer/tripledot-studios/id1191319103) game: [Woodoku](https://apps.apple.com/us/app/woodoku-wood-block-puzzles/id1496354836) is were I pucked up idea and general rule set for this game.

Added my own twist to game rules and dificulity levels

## Copyrights

[Erikas Ramanauskas, 2023](https://www.linkedin.com/in/erikas-ramanauskas)

Visit [TSTING.md](TESTING.md)
