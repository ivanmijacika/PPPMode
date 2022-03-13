// PPP Mode: Ivan Mijacika, Qina Liu, Justin Morrill, Noakai Aronesty
// SoftDev pd2
// P02 -- Snake++

// import * as LinkedList from LinkedList

var c = document.getElementById('slate');
let startbutton = document.getElementById('startbutton')

var ctx = c.getContext("2d");
let requestID;

// var snake = new LinkedList()
// snake.add(10)
// console.log(snake)

var changeX = 1;
var changeY = 0;
var posX = 250;
var posY = 250;

ctx.fillStyle = "#37C543";
ctx.fillRect(0, 0, 1200, 600);

for (let i = 0; i <= 1200; i += 100) {
    for (let j = 0; j <= 600; j += 100) {
        ctx.fillStyle = "#199B24";
        ctx.fillRect(i, j, 50, 50);
    }
}
for (let i = 50; i <= 1200; i += 100) {
    for (let j = 50; j <= 600; j += 100) {
        ctx.fillStyle = "#199B24";
        ctx.fillRect(i, j, 50, 50);
    }
}