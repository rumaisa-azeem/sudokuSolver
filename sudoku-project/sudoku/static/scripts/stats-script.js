console.log('script connected')

function timeString(time) {
  if (time === 'no data') {
    return 'no data'
  }
    mins = Math.floor(time/60)
    secs = time%60
    return mins.toString() +'m ' + secs.toString() + 's'
}

fetch('/returnstats', {
    method: "GET",
    headers: {
      "X-Requested-With": "XMLHttpRequest",
    }
  })
  .then(response => response.json())
  .then(data => {
    console.log(data);
    const gameData = data['data']
    document.getElementById("shortestE").innerHTML = timeString(gameData.minSolveTime_E);
    document.getElementById("shortestM").innerHTML = timeString(gameData.minSolveTime_M);
    document.getElementById("shortestH").innerHTML = timeString(gameData.minSolveTime_H);
    document.getElementById("shortestO").innerHTML = timeString(gameData.minSolveTime);
    document.getElementById("avgE").innerHTML = timeString(gameData.avgSolveTime_E);
    document.getElementById("avgM").innerHTML = timeString(gameData.avgSolveTime_M);
    document.getElementById("avgH").innerHTML = timeString(gameData.avgSolveTime_H);
    document.getElementById("avgO").innerHTML = timeString(gameData.avgSolveTime);
    document.getElementById("totalE").innerHTML = gameData.totalGames_E;
    document.getElementById("totalM").innerHTML = gameData.totalGames_M;
    document.getElementById("totalH").innerHTML = gameData.totalGames_H;
    document.getElementById("totalO").innerHTML = gameData.totalGames;
    document.getElementById("hintsE").innerHTML = gameData.avgHintsCount_E;
    document.getElementById("hintsM").innerHTML = gameData.avgHintsCount_M;
    document.getElementById("hintsH").innerHTML = gameData.avgHintsCount_H;
    document.getElementById("hintsO").innerHTML = gameData.avgHintsCount;
  });

