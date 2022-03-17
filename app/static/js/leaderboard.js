// PPP Mode: Ivan Mijacika, Qina Liu, Justin Morrill, Noakai Aronesty
// SoftDev pd2
// P02 -- Snake++

let py_data = fetch('/leaderboard_data')
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
