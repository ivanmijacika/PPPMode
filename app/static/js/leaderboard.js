// PPP Mode: Ivan Mijacika, Qina Liu, Justin Morrill, Noakai Aronesty
// SoftDev pd2
// P02 -- Snake++


// users, scores in the leaderboard table
let items = document.getElementsByTagName("td");
let update_data = (users, scores) => {
    // items goes through what's in the table (1 user, 1 score per row)
    // row goes through the data arrays 
    let row = 0;
    for (let i = 0; i < items.length; i += 2){
        items[i].innerHTML = users[row];
        items[i+1].innerHTML = scores[row];
        row++;
    }
}

// comms with python to update 
let py_data = (mode) => {
    fetch('/leaderboard_data', {
        // sends selected mode to python
        headers: { 'Content-Type': 'application/json'},
        method: 'POST',
        body: JSON.stringify({"mode": mode})
    })
    .then(function(response){
        // gets back db data for mode in list with scores and users
        return response.json();
    })
    .then(data => {
        // updates leaderboard table with data 
        console.log(data);
        let users = data.pop();
        console.log(users);
        let scores = data.pop();
        console.log(scores);
        update_data(users, scores);
    })
}

// when dropdown is changed/new mode is selected, calls fxn to get data
let dropdown = document.getElementById("modes")
let getMode = () => {
    mode = dropdown.value
    console.log(mode)
    py_data(mode)
}
dropdown.addEventListener('click', getMode)

// when page is first loaded, starts off with basic mode data 
py_data('basic')