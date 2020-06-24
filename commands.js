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

    close() {

        this.shell("pkill " + this.title);

    }

    save(content, file, operation) {

        if (operation) {

            switch (operation) {

                case ("add"):
                    fetch("http://127.0.0.1:5000/add", {

                        method: 'POST',

                        body: content + ", " + file

                    });

                case ("subtract"):
                    fetch("http://127.0.0.1:5000/subtract", {

                        method: 'POST',

                        body: content + ", " + file

                    });

            }

        } else {

            fetch("http://127.0.0.1:5000/save", {

                method: 'POST',

                body: content + ", " + file

            });

        }

    }

    saveAs(content, promptText) {

        if (promptText) {

            this.file = prompt(promptText);

        } else {

            this.file = prompt("Filename");

        }

        fetch("http://127.0.0.1:5000/save", {

            method: 'POST',

            body: content + ", " + this.file

        });

    }

    shell(command) {

        fetch("http://127.0.0.1:5000/shell", {

            method: 'POST',

            body: command

        });

    }

    quit() {

        this.shell("killall python3");

    }

}

var checkCtrlQ = function(e) {

    if (event.ctrlKey && event.key == "q") {

        new HTMLWindow();

    }

}

window.onkeypress = checkCtrlQ
