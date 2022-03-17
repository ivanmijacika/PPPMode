// PPP Mode: Ivan Mijacika, Qina Liu, Justin Morrill, Noakai Aronesty
// SoftDev pd2
// P02 -- Snake++


let py_data = () => {
    fetch('/leaderboard_data')
    .then(function(response){
        return response.json();
    })
    .then(data => {
        console.log(data);
        let users = data.pop();
        console.log(users);
        let scores = data.pop();
        console.log(scores);
    })
}

let dropdown = document.getElementById("modes")

let getMode = () => {
    console.log(dropdown.value)
    py_data()
}
dropdown.addEventListener('click', getMode)

let table = document.getElementById("table")
console.log(table)
