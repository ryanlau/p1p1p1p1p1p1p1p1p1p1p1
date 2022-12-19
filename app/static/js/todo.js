todos = Array.from(document.getElementsByClassName("todo-item"))

todos.forEach(todo => {
    todo.addEventListener('click', (e) => {
        const data = new FormData()
        
        
        data.append("id", e.target.id)
        data.append("status", e.target.checked)


        console.log(data);

        fetch("/api/todos/update", {
            method: "POST",
            body: data
        })
    })
});