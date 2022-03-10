// PPP Mode: Ivan Mijacika, Qina Liu, Justin Morrill, Noakai Aronesty
// SoftDev pd2
// P02 -- Snake++

var c = document.getElementById('slate');

var ctx = c.getContext("2d");

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