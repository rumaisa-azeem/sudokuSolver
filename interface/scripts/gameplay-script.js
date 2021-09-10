const gridContainer = document.getElementById('sudokuGridContainer')

let gridHTML = '<table id="sudokuGrid">'
for (i=0; i<81; i++) {
	//loop to generate html table for sudoku grid
	row = Math.floor(i/9)
	cell = i-(Math.floor(i/9)*9)
	if (i%9===0) {
		gridHTML += '<tr>'
	}
	gridHTML += '<td'
	if (row===2 || row===5) {
		gridHTML += ' class="bottomborder'
		if (cell===2 || cell===5) {
			gridHTML += ' rightborder"'
		} else {
			gridHTML += '"'
		}
	} else if (cell===2 || cell===5) {
		gridHTML += ' class="rightborder"'
	}
	gridHTML +=  ` id="${i}"></td>`
	
	if ((i+1)%9===0) {
		gridHTML += '</tr>'
	}
}
gridHTML += '</table>'

gridContainer.innerHTML = gridHTML
grid = document.getElementById('sudokuGrid')
grid.addEventListener('click', () => console.log(event.target))

