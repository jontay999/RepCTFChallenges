
const LEVELS = [
    [
        [
            "xxxxxxxxxxxxxx",
            "xxxx x  x xxxx",
            "xxx  g  b  xxx",
            "xx   x  x   xx",
            "xx   b  g   xx",
            "xxg        bxx",
            "xxxg      bxxx",
            "xxxx      xxxx",
            "xxxxxxxxxxxxxx",
        ],
        [
            {
                x: 5,
                y: 4,
                dir: "up",
            },
            {
                x: 8,
                y: 4,
                dir: "up",
            },
        ],
    ],
    [
        [
            "xxxxxxxxxxxxxx",
            "x   gr       x",
            "x   00 1     x",
            "x    x x xxxxx",
            "x            x",
            "x  x  x      x",
            "x        x  rx",
            "xx   x     gxx",
            "x          xxx",
            "xxxxxxxxxxxxxx",
        ],
        [
            {
                x: 11,
                y: 7,
                dir: "down",
            },
            {
                x: 12,
                y: 6,
                dir: "down",
            },
        ],
    ],
    [
        [
            "xxxxxxxxxxxxxx",
            "xx   0001233rx",
            "xx   0411233xx",
            "xx   444122xxx",
            "xx     xxxxxxx",
            "xr     xxxxxxx",
            "xx     xxxxxxx",
            "xx     xxxxxxx",
            "xx     xxxxxxx",
            "xxxxxxxxxxxxxx",
        ],
        [
            {
                x: 1,
                y: 5,
                dir: "up",
            },
        ],
    ],
    [
        [
            "xxxxxxxxxxxxxx",
            "xg0    g1gx  x",
            "x 3g    1 x  x",
            "x444    2 x  x",
            "xg g   ggg   x",
            "xxx     xxx  x",
            "xxx     xxx  x",
            "xxx     xxx  x",
            "xxx          x",
            "xxxxxxxxxxxxxx",
        ],
        [
            {
                x: 1,
                y: 1,
                dir: "right",
            },
            {
                x: 3,
                y: 2,
                dir: "left",
            },
            {
                x: 1,
                y: 4,
                dir: "up",
            },
            {
                x: 3,
                y: 4,
                dir: "up",
            },
            {
                x: 8,
                y: 4,
                dir: "up",
            },
            {
                x: 7,
                y: 1,
                dir: "right",
            },
            {
                x: 9,
                y: 1,
                dir: "left",
            },
        ],
    ],
];
const CHALLENGE_LEVEL = LEVELS[1]

class Stage {
    constructor(mapData) {
        this.jellies = [];
        this.moveHistory = [];
        this.numMonochromaticBlocks = 0;
        this.numColors = 0;
        if (mapData[0] instanceof Array) {
            this.anchors = mapData[1];
            this.map = mapData[0];
        }
        console.log(this.map)
        this.loadMap(this.map, this.anchors);
        this.checkForMerges();
    }

    loadMap(mapData, anchors) {
        const colors = {};
        this.cells = [];
        mapData.forEach((row, y) => {
            const cellRow = [];
            row.split('').forEach((cell, x) => {
                let color = null;
                if (cell === 'x') {
                    cellRow.push(new Wall());
                } else if (cell === 'r') {
                    color = 'red';
                } else if (cell === 'g') {
                    color = 'green';
                } else if (cell === 'b') {
                    color = 'blue';
                } else if (/[0-9]/.test(cell)) {
                    color = `black${cell}`;
                }

                if (color) {
                    const jellyCell = new JellyCell(color);
                    const jelly = new Jelly(this, jellyCell, x, y);
                    this.jellies.push(jelly);
                    this.numMonochromaticBlocks++;
                    if (!colors[color]) {
                        this.numColors++;
                    }
                    colors[color] = 1;
                    cellRow.push(jellyCell);
                } else if (cell !== 'x') {
                    cellRow.push(null);
                }
            });
            this.cells.push(cellRow);
        });
        // this.placeAnchors(anchors);
    }

    trySlide(jelly, direction) {
        const jellies = [jelly];
        if (this.checkFilled(jellies, direction, 0)) {
            return;
        }
        this.move(jellies, direction, 0);
        this.checkFall(() => this.checkForMerges());
    }

    move(jellies, dx, dy) {
        jellies.forEach(jelly => {
            jelly.cellCoords().forEach(([x, y, cell]) => {
                this.cells[y][x] = null;
            });
        });

        jellies.forEach(jelly => {
            jelly.updatePosition(jelly.x + dx, jelly.y + dy);
        });

        jellies.forEach(jelly => {
            jelly.cellCoords().forEach(([x, y, cell]) => {
                this.cells[y][x] = cell;
            });
        });
    }

    checkFilled(jellies, dx, dy) {
        let done = false;
        while (!done) {
            done = true;
            for (const jelly of jellies) {
                if (jelly.immovable) {
                    return true;
                }
                for (const [x, y, cell] of jelly.cellCoords()) {
                    const nextCell = this.cells[y + dy][x + dx];
                    if (!nextCell) {
                        continue;
                    }
                    if (!nextCell.jelly) {
                        return true;
                    }
                    if (jellies.includes(nextCell.jelly)) {
                        continue;
                    }
                    jellies.push(nextCell.jelly);
                    done = false;
                    break;
                }
                if (!done) {
                    break;
                }
            }
        }
        return false;
    }

    checkFall(cb) {
        let moved = false;
        let tryAgain = true;
        while (tryAgain) {
            tryAgain = false;
            for (const jelly of this.jellies) {
                const jellySet = [jelly];
                if (!this.checkFilled(jellySet, 0, 1)) {
                    this.move(jellySet, 0, 1);
                    tryAgain = true;
                    moved = true;
                }
            }
        }
        cb();
    }

    checkForMerges() {
        let merged = false;
        while (this.doOneMerge()) {
            merged = true;
        }
        if (merged) {
            this.checkForCompletion();
        }
    }

    checkForCompletion() {
        if (this.numMonochromaticBlocks <= this.numColors) {
            console.log("Congratulations! Level completed.");
            return true;
        }
    }

    doOneMerge() {
        for (const jelly of this.jellies) {
            for (const [x, y, cell] of jelly.cellCoords()) {
                const directions = [
                    [1, 0, "right"],
                    [0, 1, "down"]
                ];
                for (const [dx, dy, direction] of directions) {
                    const other = this.cells[y + dy][x + dx];
                    if (!(other instanceof JellyCell)) {
                        continue;
                    }
                    if (cell[`merged_${direction}`]) {
                        continue;
                    }
                    if (other.color !== cell.color) {
                        continue;
                    }
                    if (jelly !== other.jelly) {
                        this.jellies = this.jellies.filter(j => j !== other.jelly);
                    }
                    if (cell.colorMaster !== other.colorMaster) {
                        this.numMonochromaticBlocks--;
                    }
                    cell.mergeWith(other, direction);
                    cell[`merged_${direction}`] = true;
                    return true;
                }
            }
        }
        return false;
    }
}

class Wall { }

class JellyCell {
    constructor(color) {
        this.color = color;
        this.x = 0;
        this.y = 0;
        this.colorMaster = this;
        this.colorMates = [this];
    }

    mergeWith(other, direction) {
        if (other instanceof Wall) {
            this.jelly.immovable = true;
        }
        if (other instanceof JellyCell && this.color === other.color && this.colorMaster !== other.colorMaster) {
            const otherMaster = other.colorMaster;
            otherMaster.colorMates.forEach(cell => {
                cell.colorMaster = this.colorMaster;
            });
            this.colorMaster.colorMates.push(...otherMaster.colorMates);
        }
        if (other instanceof JellyCell && this.jelly !== other.jelly) {
            return this.jelly.merge(other.jelly);
        }
    }
}

class Jelly {
    constructor(stage, cell, x, y) {
        this.x = x;
        this.y = y;
        cell.jelly = this;
        this.cells = [cell];
        this.immovable = false;
    }

    cellCoords() {
        return this.cells.map(cell => [this.x + cell.x, this.y + cell.y, cell]);
    }

    updatePosition(x, y) {
        this.x = x;
        this.y = y;
    }

    merge(other) {
        const dx = other.x - this.x;
        const dy = other.y - this.y;
        other.cells.forEach(cell => {
            this.cells.push(cell);
            cell.x += dx;
            cell.y += dy;
            cell.jelly = this;
        });
        if (other.immovable) {
            this.immovable = true;
        }
        other.cells = null;
    }
}




module.exports = { Jelly, JellyCell, Wall, Stage, CHALLENGE_LEVEL };