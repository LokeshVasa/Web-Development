container.style.height="100px";
container.style.width="100px";
container.style.backgroundColor="yellow";

const para=document.createElement('p');

para.innerText="Hello I am Jagadeesh";
para.style.color="blue";
para.style.fontWeight="bold";

container.appendChild(para);

const para2=document.createElement('p');

para2.innerText="Hello from JS";
para2.style.color="red";
para2.style.fontWeight="bold";
para2.style.backgroundColor="black";

container.appendChild(para2);