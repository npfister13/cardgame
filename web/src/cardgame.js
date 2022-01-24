
/* 
  Although this class will get much more complicated, it is relatively short for now
  Look at the InputBar and especially Player classes below to see some tips about using
  Classes in JS

  The actual start of the game kicks off near the bottom of the page, in the "startGame"
  function.
*/
class CardGame{
  constructor(gameData){
    console.log('>> the game instance has been instantiated!');
    this.ready = false;

    this._deck = gameData;

    this._inputBar = new InputBar('#player-input', this.receiveInput);

    this.playerOne = new Player('#player-one', 'Bill');
    this.playerTwo = new Player('#player-two', 'Ted');
  }
  
  reset(){
    console.log('game.reset()');

    //- if you create new players, they aint got no cards, thats kinda like starting over, right?
    this.playerOne = new Player('#player-one', 'Bill');
    this.playerTwo = new Player('#player-two', 'Ted');
  }

  onDefineDeck(deck){
    console.log('>> the game data has been loaded!', deck);
    this._deck = deck;

    this.ready = true;
    this.dealCards();
  }

  getRandomCard(){
    /* ex, deck has 2 cards, therefore the valid indexes to get are "0" and "1"
      - make a random number from 0 - the length of the deck. Math.random() makes a random number from 0 - 1
      >>> .65 * 2 = 1.3
      - floor the number to get an integer within your range
      >>> Math.floor(1.3) = 1
    */
    var randomIndex = Math.floor(Math.random()*this._deck.length);
    return this._deck[randomIndex];
  }

  getRandomHand(numCards){
    var cards = [];
    for(var i = 0; i < numCards; i++){
      cards.push(this.getRandomCard());

      //- perhaps remove that card from the this._deck?
    }

    return cards;
  }

  dealCards(){
    var playerOneHand = this.getRandomHand(5);
    this.playerOne.setCards(playerOneHand);

    var playerTwoHand = this.getRandomHand(5);
    this.playerTwo.setCards(playerTwoHand);
  }

  logDeck(){
    console.log('Here are all the possible cards:', this._deck);
  }

  receiveInput(inputText){
    console.log('CardGame received input: ', inputText);
  }
}


/* A very simple class, keeps this junky code out of your normal game class */
class InputBar{
  constructor(domSelector, onValueChange){
    var element = document.querySelector(domSelector);

    element.addEventListener('keyup', function(e){
      if(e.key === 'Enter'){
        //- send the input back to the game
        onValueChange(element.value);

        //- clear the input after hitting enter
        element.value = '';
      }
    });
  }
}

/* as the player object gets more complicated, you may want to build "Card" and other things into classes as well */
class Player{
  constructor(domSelector, givenName){
    /*
      the "this" reserved word refers to "this instance of a Player", it allows you to
      create any number of players, and each player can have its own name, etc. 99% of the time
      when working within a JS class, use "this." when accessing properties or calling other methods
      within the class

      the "_underscore" helps denote which properties you would like to keep "private"
      within this class. It doesn't do anything special in this current setup, it's just a
      convention to help you organize your code.

      In this example, "name" is intended to be easily accessed from the outside, via "player.name",
      where as _cards and _element are only accessed within this class
    */
    this.name = givenName;
    this._cards = [];

    /* this is how to ask the browser for a reference to the actual render HTML element on screen */
    this._element = document.querySelector(domSelector);

    /* Render the players with what data we have so far, to at least make them show up */
    this.render();
  }

  /* 
    when using clasess, its usually better to access things via methods, rather than 
    accessing them directly (ex, game calling "player.cards = []" )

    Since a special method was called, you have the option to do extra things, that 
    the outside user wouldn't have to worry about, like re-rendering all the cards
  */
  setCards(cards){
    this._cards = cards;
    this.render();
  }

  /*
    Most modern javascript programs will "render" html to a dom element over and
    over again. This gives you the control to update the visuals whenever you want,
    and always have them based on your up-to-date data
  */
  render(){
    this._element.innerHTML = `
      <h4>${this.name}</h4>
      <div class="player-cards">
        ${this.renderCards()}
      </div>
    `;
  }

  
  /*
    There are many ways to approach this, but sometimes you may want to break up your
    rendering code, so that its easy to read and make changes to. Another approach is
    to move "card" into its own class, with its own render method
  */
  renderCards(){
    var output = '';
    for(var i = 0; i < this._cards.length; i++){
      output += `
        <div class="card click_">
          <span>${this._cards[i].name}</span>
          <span>HP: ${this._cards[i].hp}</span>
          <span>STR: ${this._cards[i].str}</span>
        </div>
      `;
    }

    return output;
  }
}




/* 
  These three functions are not defined in a class. They exist in the global scope, they can
  be called from anywhere. In general, this is messy, but it is simple

  The call that to "startGame" is farther down in a bunch of confusing stuff
*/


//since this is global, you can open the developer console in chrome, and enter "game.logDeck();"
var game;

function startGame(gameData){
  /* create an instance of the game, passing it the JSON info we already loaded and parsed */
  game = new CardGame(gameData);
}

/*
  These are uh, lets call them "global click handlers". If you look at index.html, you will see
  the buttons calling these directly. Eventually, this is a little messy, but its very simple
  and easy to use for right now
*/
function dealCards(){
  if(game) game.dealCards();
}

function reset(){
  if(game) game.reset();
}




/*
  SPOOKY DANGER ZONE

  Although there isn't a lot here, and some of the things happening are very important to know, 
  some of these things could be quite confusing and distracting when first learning JS
*/


/*
  Do not worry about this too much now, just know that the addListener for 'load' is important to make sure
  the webpage is ready before you start running this specific JS code

  "when the browser says it's ready, load the game"
  
  Some of the function calls are "asynchronous", you cant rely on your code executing in order, line-by-line here,
  any amount of time could pass between when you request the file and when you receive it, in the meantime, the rest
  of your code will be executing without this stuff
*/
window.addEventListener('load', loadGame);

/*
  This next block probably wont make a lick of sense. It's using some javascript-specific concept that
  are important, but not right now. If you are interested look up "closures", which is more or less
  passing a function to another function
*/
function loadGame(){
  loadGameData(function(gameData){
    startGame(gameData)
  });
}

/*
  Don't dig too much in this, just notice that it is loading a JSON file, and at some point calling
  the "callback" that we passed to it, with whatever JSON data was parsed in
*/
 function loadGameData(callback){
  console.log('>> loading game data...');
  var instance = this;
  var xhr = new XMLHttpRequest();
  xhr.open('GET', './assets/monsters.json');
  xhr.send(null);

  xhr.onreadystatechange = function () {
    var DONE = 4; // readyState 4 means the request is done.
    var OK = 200; // status 200 is a successful return.
    if (xhr.readyState === DONE) {
      if (xhr.status === OK) {
        console.log('>> ...game data was loaded');
        // console.log('>> json file was loaded with response:', xhr.responseText);
        //- the response is just text, so parse it into a JSON object
        var gameData = JSON.parse(xhr.responseText);
        callback(gameData);
      } else {
        console.log('Error loading deck: ' + xhr.status); // An error occurred during the request.
      }
    }
  };
}


