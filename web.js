let taskInput=document.getElementById('taskInput');
let pendingTaskslist=document.getElementById('pendingTasks');
let completedTaskslist=document.getElementById('completedTasks');
//let heading=document.getElementById('heading');
//let words=document.getElementById('words');
addtask.style.position='absolute';
addtask.style.top='20px';
addtask.style.top.left='50px';
//pendingTaskslist.style.top='100px';
//pendingTaskslist.style.left='50px';
//completedTaskslist.style.top='200px';
//completedTaskslist.style.left='50px';
//title.style.textAlign='center';
//words.style.textAlign='center';

function addtask(){
    let taskName=taskInput.value.trim();

    if(taskName!==''){
        let listItem=document.createElement('li');
        listItem.textContent=taskName;
        let completeButton=document.createElement('button');
        completeButton.textContent='Complete';
        completeButton.style.backgroundColor='white';
        completeButton.style.color='pink';
        completeButton.addEventListener('click',()=>{
       listItem.remove();
//=function() 
        //listItem.remove();
        completedTaskslist.appendChild(listItem);});
    listItem.appendChild(completeButton);
         //completeButton.textContent="Completed"
    pendingTaskslist.appendChild(listItem);
    taskInput.value='';
    }
}