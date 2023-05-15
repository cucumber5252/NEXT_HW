const todoForm = document.querySelector("#todo-form");
const todoList= document.querySelector("#todo-list");
const submitBtn = document.querySelector(".sumitBtn");
const todoContent = document.querySelector("#content");

let emptyList = [];
const listKey = "listKey";



function submitAddTodo(event){
    event.preventDefault();
    const content = {
        text: todoContent.value,
        id: Date.now(),
    };

    todoContent.value = '';

    emptyList.push(content);

    paintTodo(content);
    saveTodos();
}



function paintTodo(new_comment){
    const each_comment = document.createElement('li');
    each_comment.id = new_comment.id;

    const each_comment_span = document.createElement('span');
    const each_comment_button = document.createElement('button');
    each_comment_button.innerText = "X";
    each_comment_button.addEventListener("click", deleteTodo);

    each_comment.appendChild(each_comment_span);
    each_comment.appendChild(each_comment_button);

    each_comment_span.innerText = new_comment.text;


    todoList.appendChild(each_comment);
}




function deleteTodo(event){
    const li = event.target.parentElement;
    li.remove();

    emptyList = emptyList.filter( (todo) => todo.id !== parseInt(li.id));

    saveTodos();
}




function saveTodos(){
    window.localStorage.setItem(listKey, JSON.stringify(emptyList));
}




todoForm.addEventListener("submit", submitAddTodo);


const completedList = window.localStorage.getItem(listKey);

if (completedList !== null){
    const obj = JSON.parse(completedList);
    obj.forEach((todo) => {
        paintTodo(todo);
    });
    
    todoList.appendChild(obj);
};