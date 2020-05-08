class CardGame{
  constructor(cards){
    this._cards = cards;
  }

  logCards(){
    console.log('Here are all the cards:', this._cards);
  }
}


var game = new CardGame([ 'card1', 'card2' ]);
game.logCards();