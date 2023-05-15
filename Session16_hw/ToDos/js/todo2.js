const todoForm = document.querySelector("#todo-form");
const todoList= document.querySelector("#todo-list");
const submitBtn = document.querySelector(".sumitBtn");
const todotList = []


function getTodoFromLocalStorage() {
    return JSON.parse(localStorage.getItem("todos")) || [];
}



function saveTodoToLocalStorage(){
    window.localStorage.setItem("todos", usernameI);
}


function addTodo() {
    const todos = getTodoFromLocalStorage();
    const newTodo = document.querySelector('#content');
    todos.push(newTodo.value);
    saveTodoToLocalStorage();
    newTodo.value = '';
}



function deleteTodo(index) {
    const todos = getTodoFromLocalStorage();
    todos.splice(index, 1);
    saveTodoToLocalStorage(todos);
}



function renderTodos() {
    const todos = getTodosFromLocalStorage();
    todoList.innerHTML = "";
    todos.forEach((todo, index) => {
      const li = document.createElement("li");
      li.textContent = todo;
  
      const button = document.createElement("button");
      button.textContent = "삭제";
      button.addEventListener("click", () => {
        removeTodo(index);
      });
  
      li.appendChild(button);
      todoList.appendChild(li);
    });
  };



function init() {
    const savedUsername = localStorage.getItem("username");
    if (savedUsername) {
        usernameInput.value = savedUsername;
    }

    todoForm.addEventListener("submit", (event) => {
        event.preventDefault();
        addTodo();
    });

    renderTodos();
    };

init();