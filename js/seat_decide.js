class Table {
    // 描画するテーブルのデータを格納するモデル

    constructor() {
        this.x = 20
        this.y = 20
        this.w = 150
        this.h = 50
    }
}

const canvas_w = 1000
const canvas_h = 400

let tables = []
let selected_table = null // 現在選択中のテーブル

// true: 編集モード, false: 座席決めモード
let mode = true

const edit_checkbox = document.getElementById("edit")
const decide_checkbox = document.getElementById("decide")

edit_checkbox.addEventListener("change", () => {
    if (edit_checkbox.checked) {
        mode = true
        if (tables.length >= 1) {
            selected_table = tables[tables.length-1]
        }
    }
})

decide_checkbox.addEventListener("change", () => {
    if (decide_checkbox.checked) {
        mode = false
        selected_table = null
    }
})

const createTable = () => {
    if (!mode) {
        return
    }

    table = new Table()
    tables.push(table)
    selected_table = table
}

const deleteTable = () => {
    if (!mode) {
        return
    }

    tables = tables.filter(table => table !== selected_table)
    selected_table = tables[tables.length-1]
}

const rotateTable = () => {
    if (!mode) {
        return
    }

    const w = selected_table.w
    const h = selected_table.h

    selected_table.w = h
    selected_table.h = w
}

let grasping_table = false
const getSelectTable = (mouse_x, mouse_y) => {
    tables.forEach((table) => {
        if (
            mouse_x >= table.x &&
            mouse_x <= table.x + table.w &&
            mouse_y >= table.y &&
            mouse_y <= table.y + table.h
        ) {
            selected_table = table
            grasping_table = true
            return
        }
    })
}

function setup() {
    createCanvas(canvas_w, canvas_h)
}

function draw() {
    background("#ffffff")
    fill("#16a34a")
    noStroke()
    rect(canvas_w-50, 0, 50, canvas_h)

    tables.forEach((table) => {
        if (table === selected_table) {
            fill("#F87272")
        } else {
            fill(220)
        }
        strokeWeight(2)
        stroke(200)
        rect(table.x, table.y, table.w, table.h)
    })

    if (mode) {
        if (
            mouseIsPressed &&
            mouseX >= 0 &&
            mouseX <= canvas_w &&
            mouseY >= 0 &&
            mouseY <= canvas_h
        ) {
            if(!grasping_table) {
                getSelectTable(mouseX, mouseY)
            }
            selected_table.x = mouseX - (selected_table.w / 2)
            selected_table.y = mouseY - (selected_table.h / 2)
        } else {
            grasping_table = false
        }
    }
}
