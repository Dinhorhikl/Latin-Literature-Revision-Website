function clearTasks() {
    var ul = document.getElementById("tasks");
    while (ul.firstChild) {
        $.ajax({
            url : '/delete-task',
            method : 'POST',
            data : { taskID_py : ul.firstChild.id },
            dataType : 'text',
            success : function(data) {
            }
        });
        ul.removeChild(ul.firstChild);
    }
    updateTasksDone()
}

function updateTasksDone() {
    document.getElementById("ntaskNum").innerText = $("#tasks > .ndone").length + $("#tasks > .done").length
    document.getElementById("dtaskNum").innerText = $("#tasks > .done").length
}

window.onload = updateTasksDone();