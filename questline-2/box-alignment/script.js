const boxContainer = document.getElementById('box-container');
const btnHorizontal = document.getElementById('btn-horizontal');
const btnVertical = document.getElementById('btn-vertical');
btnHorizontal.addEventListener('click', () => {
  boxContainer.classList.remove('layout-vertical');
  boxContainer.classList.add('layout-horizontal');

  btnHorizontal.classList.add('active');
  btnVertical.classList.remove('active');
});
btnVertical.addEventListener('click', () => {
  boxContainer.classList.remove('layout-horizontal');
  boxContainer.classList.add('layout-vertical');

  btnVertical.classList.add('active');
  btnHorizontal.classList.remove('active');
});