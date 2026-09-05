
const items = [
  "Iambatman",
  "On a mission",
  "Html,css,js",
  "S1AIE26131",
  "R K Navaneeth",
  "OBSESSION IS UNSTOPPABLE"
];


const listContainer = document.getElementById("content-list");


items.forEach((itemText, index) => {
  const listItem = document.createElement("li");
  listItem.className = "list-item";

 
  const badge = document.createElement("span");
  badge.className = "badge";
  badge.textContent = `${index + 1}`;

 
  const textSpan = document.createElement("span");
  textSpan.textContent = itemText;

  
  listItem.appendChild(badge);
  listItem.appendChild(textSpan);
  listContainer.appendChild(listItem);
});