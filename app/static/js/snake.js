// PPP Mode: Ivan Mijacika, Qina Liu, Justin Morrill, Noakai Aronesty
// SoftDev pd2
// P02 -- Snake++

// import * as LinkedList from LinkedList

class Node {
    /* One segemnt of the snake */
    constructor(element) {
        this.element = element;
        this.next = null
    }
}

class LinkedList {
    /* The snake object itself */
    constructor() {
        this.head = null;
        this.size = 0;
    }

    // adds an element at the end of list
    add(element) {
        // creates a new node
        var node = new Node(element);
        var current;

        // if list is Empty add the element and make it head
        if (this.head == null)
            this.head = node;
        else {
            current = this.head;

            // iterate to the end of the list
            while (current.next) {
                current = current.next;
            }

            // add node
            current.next = node;
        }
        this.size++;
    }

    // insert element at the position index of the list
    insertAt(element, index) {
        if (index < 0 || index > this.size)
            return console.log("Please enter a valid index.");
        else {
            // creates a new node
            var node = new Node(element);
            var curr, prev;

            curr = this.head;

            // add the element to the first index
            if (index == 0) {
                node.next = this.head;
                this.head = node;
            } else {
                curr = this.head;
                var it = 0;

                // iterate over the list to find the position to insert
                while (it < index) {
                    it++;
                    prev = curr;
                    curr = curr.next;
                }

                // adding an element
                node.next = curr;
                prev.next = node;
            }
            this.size++;
        }
    }

    // removes an element from the specified location
    removeFrom(index) {
        if (index < 0 || index >= this.size)
            return console.log("Please Enter a valid index");
        else {
            var curr, prev, it = 0;
            curr = this.head;
            prev = curr;

            // deleting first element
            if (index === 0) {
                this.head = curr.next;
            } else {
                // iterate over the list to the position to removce an element
                while (it < index) {
                    it++;
                    prev = curr;
                    curr = curr.next;
                }

                // remove the element
                prev.next = curr.next;
            }
            this.size--;

            // return the remove element
            return curr.element;
        }
    }

    // removes a given element from the list
    removeElement(element) {
        var current = this.head;
        var prev = null;

        // iterate over the list
        while (current != null) {
            // comparing element with current element if found then remove the and return true
            if (current.element === element) {
                if (prev == null) {
                    this.head = current.next;
                } else {
                    prev.next = current.next;
                }
                this.size--;
                return current.element;
            }
            prev = current;
            current = current.next;
        }
        return -1;
    }


    // finds the index of element
    indexOf(element) {
        var count = 0;
        var current = this.head;

        // iterate over the list
        while (current != null) {
            // compare each element of the list with given element
            if (current.element === element)
                return count;
            count++;
            current = current.next;
        }

        // not found
        return -1;
    }

    // checks the list for empty
    isEmpty() {
        return this.size == 0;
    }

    // gives the size of the list
    size_of_list() {
        console.log(this.size);
    }


    // prints the list items
    printList() {
        var curr = this.head;
        var str = "";
        while (curr) {
            str += curr.element + " ";
            curr = curr.next;
        }
        console.log(str);
    }

}

class Apple {
    /* The apple */
    constructor(coordinates) {
        this.coordinates = coordinates;
    }
}

var c = document.getElementById('slate');
var ctx = c.getContext("2d");

// true if snake has changed its direction in a given frame
var directChanged = false;

let clear = (e) => {
    /* clears canvas */
    console.log("clear invoked...");
    ctx.clearRect(0, 0, c.offsetWidth, c.offsetHeight);;
};

var drawCanvas = () => {
    /* draws game board */
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
}
drawCanvas()

/* These variables can have values of -50, 0 or 50 */
var changeX = 0;
var changeY = 0;

/* initiate snake */
var snake = new LinkedList();
snake.add([150, 250]);
snake.add([200, 250]);
snake.add([250, 250]);
snake.add([300, 250]);
console.log(snake);

var drawSnake = () => {
    /* draws the snake based on the current positions of each of its segments */
    ctx.fillStyle = "#327fa8";

    let head = snake.head
    while (head.next != null) {
        ctx.fillRect(head.element[0] + 1, head.element[1] + 1, 48, 48);
        head = head.next
    }
    ctx.fillStyle = "#0f3142";
    ctx.fillRect(head.element[0] + 1, head.element[1] + 1, 48, 48);
}
drawSnake()

var begin = () => {
    /* play game! Triggered on arrow keypress */
    console.log('and so it begins...')
    ticker()
}

var animeSnake = () => {
    /* This is one iteration of the snake game */
    clear(c);
    drawCanvas();
    let head = snake.head
    while (head.next != null) {
        // console.log(head.element)
        // console.log(head.next.element)

        head.element[0] += head.next.element[0] - head.element[0]
        head.element[1] += head.next.element[1] - head.element[1]

        head = head.next;
    }
    head.element[0] += changeX
    head.element[1] += changeY
    drawSnake();
}

/* function for comparing arrays in js */
const equals = (a, b) => JSON.stringify(a) === JSON.stringify(b);

function noDuplicates(array) {
    /* function for checking duplicates in an array in js. Used for snake contact with itself */
    console.log(array.length);
    noDupes = true
    for (var i = 1; i < array.length; i++) {
        if (equals(array[0], array[i])) {
            noDupes = false;
            break;
        }
    }
    return noDupes;
}

var ticker = () => {
    /* Recursive function for animating snake. I didn't use animation frames because I needed to delay the snake at
    every frame and animation frames can't do that */
    setTimeout(function onTick() {
        directChanged = false;

        animeSnake();

        // Make sure the snake isn't dead; stop it if it is
        let tail = snake.head
        let elements = [];
        while (tail.next != null) {
            console.log(tail.element)
            elements.push([tail.element[0], tail.element[1]]);
            tail = tail.next;
        }
        console.log(tail.element)
        elements.push([tail.element[0], tail.element[1]]);

        console.log(elements)
        // Call ticker again for recursive animation. The delay is 120ms */
        if (tail.element[0] > -1 && tail.element[0] < 1200 && tail.element[1] > -1 && tail.element[1] < 600 && noDuplicates(elements)) {
            ticker()
        }
    }, 120)
}

document.onkeydown = function (event) {
    /* Change direction on arrow keypress */

    // make sure the snake's directino has not already been changed that frame
    if (!directChanged) {
        switch (event.keyCode) {
            case 37:
                console.log("Left key is pressed.");
                if (!(changeX == 0 && changeY == 0)) {
                    if (changeX == 0) {
                        if (changeX == 0) {
                            changeX = -50;
                            changeY = 0;
                            directChanged = true;
                        }
                    }
                }
                break;
            case 38:
                console.log("Up key is pressed.");
                if (changeX == 0 && changeY == 0) {
                    changeX = 0;
                    changeY = -50;
                    directChanged = true;
                    begin();
                }
                if (changeY == 0) {
                    if (changeY == 0) {
                        changeX = 0;
                        changeY = -50;
                        directChanged = true;
                    }
                }
                break;
            case 39:
                console.log("Right key is pressed.");
                if (changeX == 0 && changeY == 0) {
                    changeX = 50;
                    changeY = 0;
                    directChanged = true;
                    begin()
                }
                if (changeX == 0) {
                    changeX = 50;
                    changeY = 0;
                    directChanged = true;
                }
                break;
            case 40:
                console.log("Down key is pressed.");
                if (changeX == 0 && changeY == 0) {
                    changeX = 0;
                    changeY = 50;
                    directChanged = true;
                    begin();
                }
                if (changeY == 0) {

                    if (changeY == 0) {
                        changeX = 0;
                        changeY = 50;
                        directChanged = true;
                    }
                }
                break;
        }
    }
};