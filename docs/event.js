/*
 * @Author: wangzheng
 * @Date: 2020-07-16 23:22:53
 * @FilePath: \html\event.js
 */ 

function create_answer() {
    if (is_duplicate) {
        for (let index = 0; index < 4; index++) {
            answer[index] = Math.floor(Math.random() * 6);
        }
    } else {
        var testArray = [0, 1, 2, 3, 4, 5];
        if (!Array.prototype.derangedArray) {
            Array.prototype.derangedArray = function () {
                for (var j, x, i = this.length; i; j = parseInt(Math.random() * i), x = this[--i], this[i] = this[j], this[j] = x);
                return this;
            };
        }
        answer = testArray.derangedArray()
        answer.splice(4);
    }
}

function add_balls(e, iu) {
    if (is_over) {
        return false;
    }
    while (row < 4) {
        if (result[row] < 0) {
            if (row == 0) {
                draw_ball.moveTo(col * 110 + 100, 177);
            }
            draw_ball.arc(col * 110 + 70, row * 79 + 177, 30, 0, Math.PI * 2);
            draw_ball.drawImage(ball, iu * 60, 0, 60, 60, col * 110 + 40, 79 * row + 147, 60, 60);
            result[row] = iu;
            while (result[row] >= 0) {
                row += 1;
            }
            break;
        }
        row = row + 1
    }
}

function del_balls(e, col_d, row_d) {
    draw_ball.clearRect(col_d * 110 + 40, row_d * 79 + 147, 60, 60);
    draw_ball.drawImage(empty, 0, 0, 60, 60, col_d * 110 + 40, row_d * 79 + 147, 60, 60);
    result[row_d] = -1;
}

function showresult() {
    if (row != 4) {
        return false;
    }
    console.log("result:" + result);
    var correct = 0;
    var sub_correct = 0;
    var r = result.concat();
    for (let index = 0; index < 4; index++) {
        if (result[index] == answer[index]) {
            correct = correct + 1;
        }
        if (r.some(x => x == answer[index])) {
            sub_correct += 1;
            r.splice(r.findIndex(item => item === answer[index]), 1);
        }
    }
    sub_correct -= correct;
    var nail_arr = new Array(correct).fill(1).concat(new Array(sub_correct).fill(0))
    for (let index = 0; index < nail_arr.length; index++) {
        draw_ball.drawImage(nail, (1 - nail_arr[index]) * 26, 0, 26, 26, col * 110 + 39 + index % 2 * 33, parseInt(index / 2) * 33 + 40, 26, 26);
    }
    if (correct == 4) {
        draw_ball.drawImage(res, 80, 0, 80, 80, 960, 40, 80, 80);
        showanswer();
        alert("成功");
    }
    col += 1;
    row = 0;
    result = new Array(-1, -1, -1, -1);
    if (col > 7) {
        is_over = true;
        alert("结束");
    }
}

function showanswer() {
    for (let index = 0; index < answer.length; index++) {
        draw_ball.drawImage(ball, answer[index] * 60, 0, 60, 60, 970, index * 79 + 147, 60, 60);
    }
}