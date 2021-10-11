// to generate html grid /////////////////////////////////////////////////////////////

var grid = document.getElementById('sudokuGrid');
const gridContainer = document.getElementById('gridContainer');

puzzle2 = '003020600900305001001806400008102900700000008006708200002609500800203009005010300';

const createGrid = (value, index) =>
	`<div 
id='${index}'
class='square
${value !== '0' ? 'clue' : 'canEdit'}
${Math.floor(index / 9) % 3 === 2 && Math.floor(index / 9) !== 8 ? 'bottomborder' : ''} 
${(index - Math.floor(index / 9) * 9) % 3 === 2 && index - Math.floor(index / 9) * 9 !== 8 ? 'rightborder' : ''}
'>
${value !== '0' ? value : ''}
</div>`;
const gridHTML = [ ...puzzle2 ].map((value, index) => createGrid(value, index)).join``;

grid.innerHTML = gridHTML;
var cells = grid.getElementsByTagName('div');

// grid highlighting functions //////////////////////////////////////////////////////

if (window.innerWidth > 550) {
	// hover doesn't work on mobile devices
	grid.addEventListener('mouseover', hoverHighlightCell);
	grid.addEventListener('mouseout', hoverHighlightCell);
}
grid.addEventListener('click', selectCell);

function calcPos(cell) {
	num = Number(cell.id);
	row = Math.floor(num / 9);
	col = num % 9;
	return [ row, col ];
}

function hoverHighlightCell(event) {
	if (event.target.classList.contains('square')) {
		highlightCell(event.target, 'grey');
	}
}

function highlightCell(cell, colour) {
	var targetRow;
	var targetCol;
	var checkRow;
	var checkCol;
	targetRow = calcPos(cell)[0];
	targetCol = calcPos(cell)[1];
	for (i = 0; i < 81; i++) {
		checkRow = calcPos(cells[i])[0];
		checkCol = calcPos(cells[i])[1];
		if (checkRow === targetRow || checkCol === targetCol) {
			cells[i].classList.toggle(colour);
		}
	}
}

var lastSelected = '';
const numButtons = document.getElementById('numButtonsContainer').getElementsByClassName('numButton');

function selectCell(event) {
	console.log('selected', event.target);
	if (lastSelected !== '' && lastSelected !== event.target) {
		//ie if new cell is selected
		lastSelected.classList.toggle('selected'); //toggles the last selected cell off
		highlightCell(lastSelected, 'pink'); //selects the new cell
	} else if (lastSelected === event.target) {
		//if clicked same cell as last time, it will be toggled off
		event.target.classList.toggle('selected');
		highlightCell(event.target, 'pink');
		lastSelected = '';
		for (i = 0; i < 9; i++) {
			numButtons[i].classList.toggle('selected');
		}
		return;
	} else {
		for (i = 0; i < 9; i++) {
			numButtons[i].classList.toggle('selected');
		}
	}
	event.target.classList.toggle('selected');
	highlightCell(event.target, 'pink');
	lastSelected = event.target;
}

// responsive sizing /////////////////////////////////////////////////////////////////////

function resizeGrid() {
	var dimension = Math.floor(gridContainer.clientWidth / 10);
	if (dimension > 45) {
		dimension = 45;
	}
	for (i = 0; i < 81; i++) {
		cells[i].style.height = String(dimension) + 'px';
		cells[i].style.width = String(dimension) + 'px';
	}
	return dimension;
}

window.addEventListener('resize', resizeGrid);
resizeGrid();

// number pad /////////////////////////////////////////////////////////////////

const outerButtonsContainer = document.getElementById('outerButtonsContainer');
outerButtonsContainer.addEventListener('click', buttonHandler);

function buttonHandler(event) {
	console.log(event.target);
	if (event.target.classList.contains('numButton')) {
		enterNum(event.target);
	} else if (event.target.id === 'clearButton') {
		clearCell();
	} else if (event.target.id === 'noteButton') {
		makeNote();
	} else if (event.target.id === 'hintButton') {
		hint();
	} else if (event.target.id === 'clearGridButton') {
		clearGrid();
	} else if (event.target.id === 'gameSettingsButton') {
		console.log('game settings');
	} else if (event.target.id === 'tutorialButton') {
		tutorial();
	} else if (event.target.id === 'autoCheckButton') {
		autoCheck();
	} else if (
		event.target.id === 'timerButton' ||
		event.target.id === 'timerText' ||
		event.target.id === 'pauseIcon'
	) {
		pause();
	}
}

function enterNum(targetButton) {
	for (i = 0; i < 81; i++) {
		if (cells[i].classList.contains('selected') && cells[i].classList.contains('canEdit')) {
			cells[i].textContent = targetButton.textContent;
		}
	}
}

function clearCell() {
	for (i = 0; i < 81; i++) {
		if (cells[i].classList.contains('selected') && cells[i].classList.contains('canEdit')) {
			cells[i].textContent = '';
		}
	}
}

function makeNote() {
	console.log('makeNote');
	for (i = 0; i < 81; i++) {
		if (cells[i].classList.contains('selected') && cells[i].classList.contains('canEdit')) {
			cells[i].classList.toggle('note');
		}
	}
}

function hint() {
	console.log('hint');
}

function clearGrid() {
	console.log('clear grid');
	for (i = 0; i < 81; i++) {
		if (cells[i].classList.contains('canEdit')) {
			cells[i].textContent = '';
		}
	}
}

function tutorial() {
	console.log('tutorial');
}

function autoCheck() {
	console.log('autocheck');
}

// timer ///////////////////////////////////////////////////////////////////

timervariable = setInterval(timer, 1000);
count = 0;
var mins = '';
var seconds = '';
timerText = document.getElementById('timerText');
pauseIcon = document.getElementById('pauseIcon');

function timer() {
	count++;
	mins = String(Math.floor(count / 60));
	seconds = String(count % 60);
	if (mins.length === 1) {
		mins = '0' + mins;
	}
	if (seconds.length === 1) {
		seconds = '0' + seconds;
	}
	timerText.textContent = mins + ':' + seconds;
}

function pause() {
	if (grid.style.display === 'none') {
		//unpause
		pauseIcon.setAttribute('src', 'https://iili.io/RbJUAb.png'); //pause icon
		timervariable = setInterval(timer, 1000);
		gridContainer.style.height = '';
		grid.style.display = '';
	} else {
		//pause
		pauseIcon.setAttribute('src', 'https://iili.io/RbkA7a.png'); //play icon
		clearInterval(timervariable);
		gridContainer.style.height = String(grid.clientHeight) + 'px';
		grid.style.display = 'none';
	}
}
