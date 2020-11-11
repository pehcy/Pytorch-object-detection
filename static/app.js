var validate = Array(2).fill(false);

window.addEventListener('DOMContentLoaded', function() {
  const fieldInputs = ["__browse-file", "__entity-name"].map(_ => document.getElementById(_))
  for (const [index, elem] of fieldInputs.entries()) {
    elem.addEventListener('input', e => {
      validate[index] = e.value || e.target ? true : false;
      if (validate[0] && validate[1] === true) {
        const btnSubmit = document.getElementsByTagName('button')[0];
        btnSubmit.classList.replace('btn-outline-secondary', 'btn-outline-primary');
        btnSubmit.disabled = false;
      }
    }, false)
  };
})