<<<<<<< Updated upstream
/*
 * @Author: wangzheng
 * @Date: 2020-07-16 23:22:53
 * @FilePath: \html\click.js
 */ 

a.onclick = a.oncontextmenu = (e) => {
    return false;
}

a.onmousedown = (e) => {
    if (e.button != 0) {
        return false;
    }
    xd = e.pageX - a.getBoundingClientRect().left - document.documentElement.scrollLeft - document.body
        .scrollLeft;
    yd = e.pageY - a.getBoundingClientRect().top - document.documentElement.scrollTop - document.body
        .scrollTop;
    if (draw_ball.isPointInPath(xd, yd)) {
        if (yd > 500) {
            var idown = parseInt((xd - 135) / 90)
            draw_ball.drawImage(ball, idown * 60, 60, 60, 60, 135 + idown * 90, 500, 60, 60)
        } else {
            col_d = parseInt((xd - 40) / 110);
            row_d = parseInt((yd - 147) / 79);
            // i_col = parseInt(yu)
            if (col_d == col) {
                del_balls(e, col_d, row_d);
                row = Math.min(row_d, row);
            }
        }
    }
    if (xd > 750 && xd < 810 && yd > 500 && yd < 560) {
        //ok
        draw_ball.drawImage(button, 0, 60, 60, 60, 750, 500, 60, 60);
        is_ok = true;
    }
    if (xd > 825 && xd < 885 && yd > 500 && yd < 560) {
        //restart
        draw_ball.drawImage(button, 60, 60, 60, 60, 825, 500, 60, 60);
        is_restart = true;
    }
    if (xd > 900 && xd < 960 && yd > 500 && yd < 560) {
        //answer
        draw_ball.drawImage(button, 120, 60, 60, 60, 900, 500, 60, 60);
        is_answer = true;
    }
    if (xd > 975 && xd < 1035 && yd > 500 && yd < 530) {
        is_duplicate_down = true;

    }
    return false;
};
a.onmouseup = (e) => {
    if (e.button != 0) {
        return false;
    }
    if (draw_ball.isPointInPath(xd, yd)) {
        if (yd > 500) {
            var idown = parseInt((xd - 135) / 90)
            draw_ball.drawImage(ball, idown * 60, 0, 60, 60, 135 + idown * 90, 500, 60, 60)
        }
    }
    xu = e.pageX - a.getBoundingClientRect().left - document.documentElement.scrollLeft - document.body.scrollLeft;
    yu = e.pageY - a.getBoundingClientRect().top - document.documentElement.scrollTop - document.body.scrollTop;
    if (draw_ball.isPointInPath(xu, yu)) {
        var iu = parseInt((xu - 135) / 90)
        if (idown == iu && yu > 500 && xu < 650) {
            add_balls(e, iu);
        }

    }
    if (xu > 750 && xu < 810 && yu > 500 && yu < 560) {
        //ok
        draw_ball.drawImage(button, 0, 0, 60, 60, 750, 500, 60, 60);
        if (is_ok) {
            showresult(result);
        }

    }
    if (xu > 825 && xu < 885 && yu > 500 && yu < 560) {
        //restart
        draw_ball.drawImage(button, 60, 0, 60, 60, 825, 500, 60, 60);
        if (is_restart) {
            restart();
        }
    }
    if (xu > 900 && xu < 950 && yu > 500 && yu < 560) {
        //answer
        draw_ball.drawImage(button, 120, 0, 60, 60, 900, 500, 60, 60);
        if (is_answer) {
            showanswer();
        }
    }
    if (xu > 975 && xu < 1035 && yu > 500 && yu < 530) {
        //switch
        if (is_duplicate_down) {
            is_duplicate = !is_duplicate;
            restart();
        }
    }
    return false;
=======
/*
 * @Author: wangzheng
 * @Date: 2020-07-16 23:22:53
 * @FilePath: \html\click.js
 */ 

a.onclick = a.oncontextmenu = (e) => {
    return false;
}

a.onmousedown = (e) => {
    if (e.button != 0) {
        return false;
    }
    xd = e.pageX - a.getBoundingClientRect().left - document.documentElement.scrollLeft - document.body
        .scrollLeft;
    yd = e.pageY - a.getBoundingClientRect().top - document.documentElement.scrollTop - document.body
        .scrollTop;
    if (draw_ball.isPointInPath(xd, yd)) {
        if (yd > 500) {
            var idown = parseInt((xd - 135) / 90)
            draw_ball.drawImage(ball, idown * 60, 60, 60, 60, 135 + idown * 90, 500, 60, 60)
        } else {
            col_d = parseInt((xd - 40) / 110);
            row_d = parseInt((yd - 147) / 79);
            // i_col = parseInt(yu)
            if (col_d == col) {
                del_balls(e, col_d, row_d);
                row = Math.min(row_d, row);
            }
        }
    }
    if (xd > 750 && xd < 810 && yd > 500 && yd < 560) {
        //ok
        draw_ball.drawImage(button, 0, 60, 60, 60, 750, 500, 60, 60);
        is_ok = true;
    }
    if (xd > 825 && xd < 885 && yd > 500 && yd < 560) {
        //restart
        draw_ball.drawImage(button, 60, 60, 60, 60, 825, 500, 60, 60);
        is_restart = true;
    }
    if (xd > 900 && xd < 960 && yd > 500 && yd < 560) {
        //answer
        draw_ball.drawImage(button, 120, 60, 60, 60, 900, 500, 60, 60);
        is_answer = true;
    }
    if (xd > 975 && xd < 1035 && yd > 500 && yd < 530) {
        is_duplicate_down = true;

    }
    return false;
};
a.onmouseup = (e) => {
    if (e.button != 0) {
        return false;
    }
    if (draw_ball.isPointInPath(xd, yd)) {
        if (yd > 500) {
            var idown = parseInt((xd - 135) / 90)
            draw_ball.drawImage(ball, idown * 60, 0, 60, 60, 135 + idown * 90, 500, 60, 60)
        }
    }
    xu = e.pageX - a.getBoundingClientRect().left - document.documentElement.scrollLeft - document.body.scrollLeft;
    yu = e.pageY - a.getBoundingClientRect().top - document.documentElement.scrollTop - document.body.scrollTop;
    if (draw_ball.isPointInPath(xu, yu)) {
        var iu = parseInt((xu - 135) / 90)
        if (idown == iu && yu > 500 && xu < 650) {
            add_balls(e, iu);
        }

    }
    if (xu > 750 && xu < 810 && yu > 500 && yu < 560) {
        //ok
        draw_ball.drawImage(button, 0, 0, 60, 60, 750, 500, 60, 60);
        if (is_ok) {
            showresult(result);
        }

    }
    if (xu > 825 && xu < 885 && yu > 500 && yu < 560) {
        //restart
        draw_ball.drawImage(button, 60, 0, 60, 60, 825, 500, 60, 60);
        if (is_restart) {
            restart();
        }
    }
    if (xu > 900 && xu < 950 && yu > 500 && yu < 560) {
        //answer
        draw_ball.drawImage(button, 120, 0, 60, 60, 900, 500, 60, 60);
        if (is_answer) {
            showanswer();
        }
    }
    if (xu > 975 && xu < 1035 && yu > 500 && yu < 530) {
        //switch
        if (is_duplicate_down) {
            is_duplicate = !is_duplicate;
            restart();
        }
    }
    return false;
>>>>>>> Stashed changes
}