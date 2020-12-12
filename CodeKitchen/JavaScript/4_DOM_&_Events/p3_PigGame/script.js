'use strict';

//======================================= Selecting elements ==========================================
const diceEl = document.querySelector('.dice');
const score0El = document.querySelector('#score--0');
const score1El = document.getElementById('score--1'); //Faster than querySelector.
const current0El = document.getElementById('current--0');
const current1El = document.getElementById('current--1');
const player0El = document.querySelector('.player--0');
const player1El = document.querySelector('.player--1');
const btnNew = document.querySelector('.btn--new');
const btnRoll = document.querySelector('.btn--roll');
const btnHold = document.querySelector('.btn--hold');

//======================================= Game Initilization ==========================================
let scores, currScore, activePlayer, playState;
//=======================================  Functions  ==========================================
const init = function () {
  // Game re-initialize.
  score0El.textContent = score1El.textContent = 0;
  current0El.textContent = current1El.textContent = 0;
  diceEl.classList.add('hidden');

  scores = [0, 0];
  currScore = 0;
  activePlayer = 0;
  playState = true;

  // make player-1 as active.
  player0El.classList.add('player--active');
  player1El.classList.remove('player--active');

  // remove winner class.
  player0El.classList.remove('player--winner');
  player1El.classList.remove('player--winner');
};

init();

const switchPlayer = function () {
  document.getElementById(`current--${activePlayer}`).textContent = 0;
  currScore = 0;
  activePlayer = activePlayer === 0 ? 1 : 0;
  player0El.classList.toggle('player--active');
  player1El.classList.toggle('player--active');
};
// Dice Roll Function
const diceRoll = function () {
  return Math.trunc(Math.random() * 6) + 1;
};

//======================================= Button Click Events ===================================

// Dice Roll Functionality
btnRoll.addEventListener('click', function () {
  if (playState) {
    const dice = diceRoll();

    //show score on dice
    diceEl.classList.remove('hidden');
    diceEl.src = `dice-${dice}.png`;

    if (dice !== 1) {
      //add dic-roll to c.score
      currScore += dice;
      document.getElementById(
        `current--${activePlayer}`
      ).textContent = currScore;

      // show the new current score.
    } else {
      // switch player
      switchPlayer();
    }
  }
});

// Hold Functionality
btnHold.addEventListener('click', function () {
  if (playState) {
    //Add curr.score to active players total score.
    scores[activePlayer] += currScore;
    document.getElementById(`score--${activePlayer}`).textContent =
      scores[activePlayer];

    if (scores[activePlayer] >= 30) {
      //current player wins.
      document
        .querySelector(`.player--${activePlayer}`)
        .classList.add('player--winner');

      document
        .querySelector(`.player--${activePlayer}`)
        .classList.remove('player--active');

      //finish game
      playState = false;
      diceEl.classList.add('hidden');
    } else {
      //switch player.
      switchPlayer();
    }
  }
});

// Reset Functionality
btnNew.addEventListener('click', init);
