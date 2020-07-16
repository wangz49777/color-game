<<<<<<< Updated upstream
/*
 * @Author: wangzheng
 * @Date: 2020-07-16 23:22:53
 * @FilePath: \html\init.js
 */ 

draw_ball = a.getContext("2d");
is_duplicate = false;

function restart() {
    draw_ball.clearRect(0, 0, 1080, 600);
    is_over = false;
    col = 0;
    row = 0;
    result = new Array(-1, -1, -1, -1);
    is_ok = false;
    is_restart = false;
    is_answer = false;
    is_duplicate_down = false;
    answer = new Array(0, 1, 2, 3);
    create_answer();
    console.log("answer:" + answer);
    setTimeout(function () {
        for (let index = 0; index < 8; index++) {
            draw_ball.drawImage(frame, 0, 0, 100, 358, 110 * index + 20, 120, 100, 358);
            draw_ball.drawImage(res, 0, 0, 80, 80, 110 * index + 30, 30, 80, 80);
        }
        draw_ball.drawImage(frame, 0, 0, 100, 358, 950, 120, 100, 358);
        draw_ball.drawImage(res, 160, 0, 80, 80, 960, 40, 80, 80);
        draw_ball.drawImage(tool, 50, 480)
        for (let index = 0; index < 6; index++) {
            draw_ball.drawImage(ball, index * 60, 0, 60, 60, 135 + index * 90, 500, 60, 60)
        }
        for (let index = 0; index < 3; index++) {
            draw_ball.drawImage(button, index * 60, 0, 60, 60, 750 + 75 * index, 500, 60, 60)
        }
        if (is_duplicate) {
            draw_ball.drawImage(flag, 0, 0, 120, 120, 975, 500, 60, 60);
        } else {
            draw_ball.drawImage(flag, 120, 0, 120, 120, 975, 500, 60, 60);
        }
        draw_ball.beginPath();
        for (let index = 0; index < 6; index++) {
            draw_ball.arc(165 + index * 90, 530, 30, 0, Math.PI * 2);
        }
    }, 10);
}
=======
/*
 * @Author: wangzheng
 * @Date: 2020-07-16 23:22:53
 * @FilePath: \html\init.js
 */ 

draw_ball = a.getContext("2d");
is_duplicate = false;

function restart() {
    draw_ball.clearRect(0, 0, 1080, 600);
    is_over = false;
    col = 0;
    row = 0;
    result = new Array(-1, -1, -1, -1);
    is_ok = false;
    is_restart = false;
    is_answer = false;
    is_duplicate_down = false;
    answer = new Array(0, 1, 2, 3);
    create_answer();
    console.log("answer:" + answer);
    setTimeout(function () {
        for (let index = 0; index < 8; index++) {
            draw_ball.drawImage(frame, 0, 0, 100, 358, 110 * index + 20, 120, 100, 358);
            draw_ball.drawImage(res, 0, 0, 80, 80, 110 * index + 30, 30, 80, 80);
        }
        draw_ball.drawImage(frame, 0, 0, 100, 358, 950, 120, 100, 358);
        draw_ball.drawImage(res, 160, 0, 80, 80, 960, 40, 80, 80);
        draw_ball.drawImage(tool, 50, 480)
        for (let index = 0; index < 6; index++) {
            draw_ball.drawImage(ball, index * 60, 0, 60, 60, 135 + index * 90, 500, 60, 60)
        }
        for (let index = 0; index < 3; index++) {
            draw_ball.drawImage(button, index * 60, 0, 60, 60, 750 + 75 * index, 500, 60, 60)
        }
        if (is_duplicate) {
            draw_ball.drawImage(flag, 0, 0, 120, 120, 975, 500, 60, 60);
        } else {
            draw_ball.drawImage(flag, 120, 0, 120, 120, 975, 500, 60, 60);
        }
        draw_ball.beginPath();
        for (let index = 0; index < 6; index++) {
            draw_ball.arc(165 + index * 90, 530, 30, 0, Math.PI * 2);
        }
    }, 10);
}
>>>>>>> Stashed changes
restart();