class HTMLWindow {

    constructor(width, height, decoration, title, file, icon) {

        if (width == null) {

            this.quit();

        } else {

            this.title = title;

            fetch("http://127.0.0.1:5000/new", {

                method: 'POST',

                body: width + " " + height + " " + decoration + " " + title + " " + file + " " + icon

            });

        }

    }

    save(content, file) {

        fetch("http://127.0.0.1:5000/filesave", {

            method: 'POST',

            body: content + ", " + file

        });

    }

    shell(command) {

        fetch("http://127.0.0.1:5000/shell", {

            method: 'POST',

            body: command

        });

    }

    close() {

        fetch("http://127.0.0.1:5000/close", {

            method: 'POST',

            body: this.title

        });

    }

    quit() {

        this.shell("killall flask");
        this.shell("killall python3");

    }

}

window.onkeypress = function(e) {

    if (event.ctrlKey && event.key == "q") {

        new HTMLWindow();

    }

}