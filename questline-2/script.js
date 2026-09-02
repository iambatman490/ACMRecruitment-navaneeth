let count = 0;
const counterValue = document.getElementById('counter-value');
const incrementBtn = document.getElementById('increment-btn');
const decrementBtn = document.getElementById('decrement-btn');
const resetBtn = document.getElementById('reset-btn');
function updateDisplay() {
  counterValue.textContent = count;
}
incrementBtn.addEventListener('click', () => {
  count++;
  updateDisplay();
});
decrementBtn.addEventListener('click', () => {
  count--;
  updateDisplay();
});
resetBtn.addEventListener('click', () => {
  count = 0;
  updateDisplay();
});