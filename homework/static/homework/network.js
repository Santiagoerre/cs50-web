document.addEventListener('DOMContentLoaded', function() {
    document.querySelector("#edit_form").style.display = 'none';
    document.querySelectorAll('#done').forEach(function(button) {
        let idd = button.name;
        button.onclick = function() {
            fetch("homework/done", {
                method: "POST",
                    body: JSON.stringify({
                        done: "yes",
                        id: idd,
            })
        })
        .then(result => {
            location.reload();
            // Print result
            console.log(idd);
        })
        }
    
    })
    document.querySelectorAll('#not_done').forEach(function(button) {
        let idd = button.name;
        button.onclick = function() {
            fetch("homework/done", {
                method: "POST",
                    body: JSON.stringify({
                        done:"no",
                        id: idd,
            })
        })
        .then(result => {
            location.reload();
            // Print result
            console.log(idd);
        })
        }
    
    })

    document.querySelectorAll('#edit').forEach(function(button) {
        button.onclick = function() {
            document.querySelector("#edit_form").style.display = 'block';
            let idd = button.name;

            fetch(`/edit/${idd}`)
            .then(response => response.json())
            .then(homework => {
                console.log(homework);

                document.querySelector("#fname").value = homework.title;
                document.querySelector("#class").value = homework.class;
                document.querySelector("#due_date").value = homework.due_date;
                document.querySelector("#link").value = homework.link;
            })


            
        }
    })
    document.querySelector('#edit_form').addEventListener('click', edit);
    

    function edit(homework) {
        title = document.querySelector("#fname").value;
        clas = document.querySelector("#class").value;
        due_date = document.querySelector("#due_date").value;
        link = document.querySelector("#link").value;
        id = document.querySelector("#edit_form_submit").name;
        idd = id
        fetch("/edit", {
            method: 'POST',
            body: JSON.stringify({
                title: title,
                clas: clas,
                due_date: due_date,
                link: link,
                id: id
            })
          })
          console.log("posted");
    }
});